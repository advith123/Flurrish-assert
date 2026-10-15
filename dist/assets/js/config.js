/* Flourrish — site configuration. Edit this file only. */
window.FLOURRISH_CONFIG = {
  // WhatsApp business number (digits only, with country code)
  whatsapp: '919944070397',
  // Default pre-filled WhatsApp message
  whatsappMessage: 'Hello Flourrish Asset Management, I would like to discuss property management for my property in India.',
  // Enquiry form endpoint. '/api/enquiry' is handled by functions/api/enquiry.js (Cloudflare Pages)
  // or server/server.js (Node). Set to '' to route enquiries over WhatsApp instead, or to a
  // Formspree URL such as 'https://formspree.io/f/YOUR_FORM_ID'. When the site is opened from
  // disk (file://) the form always falls back to WhatsApp.
  formEndpoint: '/api/enquiry',
  // Email shown on the site
  email: 'admin.flourrishassets@gmail.com'
};
