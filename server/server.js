/* Minimal Node 18+ server for hosts without Cloudflare Pages: serves ../dist and handles POST /api/enquiry.
   Run:  node server/server.js      (PORT, RESEND_API_KEY, ENQUIRY_TO, ENQUIRY_FROM, ENQUIRY_DRY_RUN as env vars)
   Put it behind nginx/Caddy for TLS. No dependencies. */
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validate, emailPayload, sendViaResend } from '../functions/api/_lib/enquiry.js';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', 'dist');
const PORT = Number(process.env.PORT || 8787);
const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.xml': 'application/xml', '.txt': 'text/plain', '.webmanifest': 'application/manifest+json', '.md': 'text/markdown' };
const hits = new Map(); /* ip -> [timestamps] */

const send = (res, status, data) => { res.writeHead(status, { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }); res.end(JSON.stringify(data)); };

http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://x');
  if (url.pathname === '/api/enquiry') {
    if (req.method !== 'POST') return send(res, 405, { ok: false, error: 'Method not allowed' });
    const ip = req.socket.remoteAddress || 'unknown';
    const now = Date.now(); const recent = (hits.get(ip) || []).filter((t) => now - t < 600000);
    if (recent.length >= 5) return send(res, 429, { ok: false, error: 'Too many submissions. Please try again later or message us on WhatsApp.' });
    recent.push(now); hits.set(ip, recent);
    let raw = ''; req.on('data', (c) => { raw += c; if (raw.length > 20000) req.destroy(); });
    req.on('end', async () => {
      let body; try { body = JSON.parse(raw); } catch { return send(res, 400, { ok: false, error: 'Invalid JSON' }); }
      const v = validate(body);
      if (v.spam) return send(res, 200, { ok: true });
      if (!v.ok) return send(res, 400, { ok: false, error: 'Please check the highlighted fields.', fields: v.errors });
      if (process.env.ENQUIRY_DRY_RUN === '1') return send(res, 200, { ok: true, dryRun: true });
      if (!process.env.RESEND_API_KEY) return send(res, 503, { ok: false, error: 'Enquiry delivery is not configured on this site yet. Please message us on WhatsApp.' });
      try {
        await sendViaResend(emailPayload(v.clean, { to: process.env.ENQUIRY_TO || 'admin.flourrishassets@gmail.com', from: process.env.ENQUIRY_FROM || 'Flourrish Website <onboarding@resend.dev>' }), process.env.RESEND_API_KEY);
        send(res, 200, { ok: true });
      } catch (err) { console.error(err.message); send(res, 502, { ok: false, error: 'Your enquiry could not be delivered right now. Please try again or message us on WhatsApp.' }); }
    });
    return;
  }
  let file = path.normalize(path.join(ROOT, url.pathname === '/' ? 'index.html' : url.pathname));
  if (!file.startsWith(ROOT)) { res.writeHead(403); return res.end(); }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!fs.existsSync(file)) { file = path.join(ROOT, '404.html'); res.statusCode = 404; }
  const ext = path.extname(file);
  res.setHeader('Content-Type', TYPES[ext] || 'application/octet-stream');
  res.setHeader('Cache-Control', ext === '.html' ? 'no-cache' : 'public, max-age=86400');
  res.setHeader('X-Content-Type-Options', 'nosniff'); res.setHeader('X-Frame-Options', 'DENY'); res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  fs.createReadStream(file).pipe(res);
}).listen(PORT, () => console.log(`Flourrish site on http://localhost:${PORT}`));
