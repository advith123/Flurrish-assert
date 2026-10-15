/* Cloudflare Pages Function: POST /api/enquiry
   Env vars (Pages → Settings → Environment variables):
     RESEND_API_KEY   required to send mail (https://resend.com; verify the sending domain first)
     ENQUIRY_TO       recipient, default admin.flourrishassets@gmail.com
     ENQUIRY_FROM     sender on a verified domain, e.g. "Flourrish Website <enquiries@flourrishassets.com>"
     ENQUIRY_DRY_RUN  set to "1" to validate and return success without sending (for testing only)
   Optional KV binding RATE_KV enables per-IP rate limiting (5 submissions per 10 minutes). */
import { validate, emailPayload, sendViaResend, json } from './_lib/enquiry.js';

export async function onRequestPost({ request, env }) {
  if (!(request.headers.get('content-type') || '').includes('application/json')) return json({ ok: false, error: 'Expected JSON' }, 415);
  let body;
  try { body = await request.json(); } catch { return json({ ok: false, error: 'Invalid JSON' }, 400); }

  const ip = request.headers.get('cf-connecting-ip') || 'unknown';
  if (env.RATE_KV) {
    const key = `enq:${ip}`;
    const n = Number((await env.RATE_KV.get(key)) || 0);
    if (n >= 5) return json({ ok: false, error: 'Too many submissions. Please try again later or message us on WhatsApp.' }, 429, { 'Retry-After': '600' });
    await env.RATE_KV.put(key, String(n + 1), { expirationTtl: 600 });
  }

  const v = validate(body);
  if (v.spam) return json({ ok: true }); /* silently accept honeypot hits */
  if (!v.ok) return json({ ok: false, error: 'Please check the highlighted fields.', fields: v.errors }, 400);

  const to = env.ENQUIRY_TO || 'admin.flourrishassets@gmail.com';
  const from = env.ENQUIRY_FROM || 'Flourrish Website <onboarding@resend.dev>';
  if (env.ENQUIRY_DRY_RUN === '1') return json({ ok: true, dryRun: true });
  if (!env.RESEND_API_KEY) return json({ ok: false, error: 'Enquiry delivery is not configured on this site yet. Please message us on WhatsApp.' }, 503);

  try {
    await sendViaResend(emailPayload(v.clean, { to, from }), env.RESEND_API_KEY);
    return json({ ok: true });
  } catch (err) {
    console.error('enquiry send failed', err.message);
    return json({ ok: false, error: 'Your enquiry could not be delivered right now. Please try again or message us on WhatsApp.' }, 502);
  }
}

export const onRequest = (ctx) => (ctx.request.method === 'POST' ? onRequestPost(ctx) : json({ ok: false, error: 'Method not allowed' }, 405, { Allow: 'POST' }));
