/* Shared enquiry handling: validation, rate-limit key, email payload.
   Used by functions/api/enquiry.js (Cloudflare Pages) and server/server.js (Node). */

export const LIMITS = { name: 100, email: 160, phone: 25, phone_code: 6, country: 60, property_location: 80, property_type: 60, occupancy: 60, service: 80, contact_method: 20, details: 2000 };
const REQUIRED = ['name', 'email', 'phone', 'country', 'property_location', 'property_type', 'occupancy', 'service', 'contact_method'];
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export function validate(body) {
  const errors = {};
  if (!body || typeof body !== 'object') return { ok: false, errors: { body: 'Invalid request body' } };
  if (typeof body.company_website === 'string' && body.company_website.trim()) return { ok: false, spam: true, errors: {} };
  const clean = {};
  for (const [k, max] of Object.entries(LIMITS)) {
    const v = body[k] == null ? '' : String(body[k]).trim();
    if (v.length > max) errors[k] = `Too long (max ${max} characters)`;
    clean[k] = v.slice(0, max);
  }
  for (const k of REQUIRED) if (!clean[k]) errors[k] = 'Required';
  if (clean.email && !EMAIL_RE.test(clean.email)) errors.email = 'Invalid email';
  if (clean.phone && clean.phone.replace(/\D/g, '').length < 7) errors.phone = 'Invalid phone number';
  const count = body.properties_count == null || body.properties_count === '' ? '' : Number(body.properties_count);
  if (count !== '' && (!Number.isInteger(count) || count < 1 || count > 50)) errors.properties_count = 'Must be between 1 and 50';
  clean.properties_count = count === '' ? '' : String(count);
  clean.consent = body.consent === 'yes' || body.consent === true ? 'yes' : 'no';
  if (clean.consent !== 'yes') errors.consent = 'Consent is required';
  return { ok: Object.keys(errors).length === 0, errors, clean };
}

export function emailPayload(clean, { to, from, replyTo }) {
  const rows = [
    ['Name', clean.name], ['Email', clean.email], ['Phone / WhatsApp', `${clean.phone_code} ${clean.phone}`.trim()],
    ['Country of residence', clean.country], ['Property location', clean.property_location], ['Property type', clean.property_type],
    ['Occupancy', clean.occupancy], ['Service required', clean.service], ['Number of properties', clean.properties_count || '—'],
    ['Preferred contact', clean.contact_method], ['Details', clean.details || '—'], ['Consent', clean.consent],
  ];
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const text = rows.map(([k, v]) => `${k}: ${v}`).join('\n');
  const html = `<h2 style="font-family:sans-serif">New property enquiry</h2><table style="font-family:sans-serif;border-collapse:collapse">${rows.map(([k, v]) => `<tr><td style="padding:6px 12px 6px 0;color:#666">${esc(k)}</td><td style="padding:6px 0">${esc(v).replace(/\n/g, '<br>')}</td></tr>`).join('')}</table>`;
  return { from, to: [to], reply_to: replyTo || clean.email, subject: `Enquiry: ${clean.property_type} in ${clean.property_location} — ${clean.name}`, text, html };
}

export async function sendViaResend(payload, apiKey) {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { Authorization: `Bearer ${apiKey}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error(`Email provider responded ${res.status}: ${(await res.text()).slice(0, 200)}`);
  return res.json();
}

export const json = (data, status = 200, extra = {}) =>
  new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store', ...extra } });
