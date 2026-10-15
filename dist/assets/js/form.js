/* Flourrish — enquiry form. Validates, then posts to the configured endpoint
   or opens WhatsApp with the enquiry pre-filled when no endpoint is set. */
(function () {
  'use strict';

  var cfg = window.FLOURRISH_CONFIG || {};

  document.querySelectorAll('form[data-enquiry]').forEach(function (form) {
    var status = form.querySelector('.form-status');
    var submitBtn = form.querySelector('button[type="submit"]');
    var pending = false;

    /* Country → calling code */
    var country = form.querySelector('select[name="country"]');
    var code = form.querySelector('input[name="phone_code"]');
    if (country && code) {
      var syncCode = function () {
        var opt = country.options[country.selectedIndex];
        var c = opt ? opt.getAttribute('data-code') : '';
        if (c) code.value = c;
      };
      country.addEventListener('change', syncCode);
      if (!code.value) syncCode();
    }

    var setFieldError = function (input, message) {
      var field = input.closest('.field');
      if (!field) return;
      var err = field.querySelector('.error');
      field.classList.toggle('is-invalid', !!message);
      if (err) err.textContent = message || '';
      input.setAttribute('aria-invalid', message ? 'true' : 'false');
    };

    var showStatus = function (type, message) {
      if (!status) return;
      status.className = 'form-status is-' + type;
      status.textContent = message;
      status.setAttribute('role', type === 'error' ? 'alert' : 'status');
    };

    var validate = function () {
      var ok = true;
      var firstBad = null;
      form.querySelectorAll('[data-required]').forEach(function (input) {
        var value = input.type === 'checkbox' ? input.checked : input.value.trim();
        var msg = '';
        if (!value) {
          msg = input.getAttribute('data-required') || 'This field is required.';
        } else if (input.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value)) {
          msg = 'Enter a valid email address.';
        } else if (input.name === 'phone' && value.replace(/\D/g, '').length < 7) {
          msg = 'Enter a phone or WhatsApp number with at least 7 digits.';
        }
        setFieldError(input, msg);
        if (msg) { ok = false; if (!firstBad) firstBad = input; }
      });
      if (firstBad) firstBad.focus();
      return ok;
    };

    form.querySelectorAll('[data-required]').forEach(function (input) {
      input.addEventListener('input', function () {
        if (input.closest('.field') && input.closest('.field').classList.contains('is-invalid')) setFieldError(input, '');
      });
      input.addEventListener('change', function () { setFieldError(input, ''); });
    });

    var collect = function () {
      var data = {};
      Array.prototype.forEach.call(form.elements, function (el) {
        if (!el.name || el.type === 'submit' || el.type === 'button') return;
        if (el.type === 'checkbox') data[el.name] = el.checked ? 'yes' : 'no';
        else data[el.name] = el.value.trim();
      });
      return data;
    };

    var whatsappText = function (d) {
      var lines = [
        'Hello Flourrish Asset Management, I would like to discuss property management.',
        '',
        'Name: ' + d.name,
        'Country of residence: ' + d.country,
        'Phone / WhatsApp: ' + (d.phone_code ? d.phone_code + ' ' : '') + d.phone,
        d.email ? 'Email: ' + d.email : null,
        'Property location: ' + d.property_location,
        'Property type: ' + d.property_type,
        'Occupancy: ' + d.occupancy,
        'Service required: ' + d.service,
        d.properties_count ? 'Number of properties: ' + d.properties_count : null,
        'Preferred contact: ' + d.contact_method,
        d.details ? 'Details: ' + d.details : null
      ].filter(function (l) { return l !== null; });
      return lines.join('\n');
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (pending) return;
      if (!validate()) {
        showStatus('error', 'Please check the highlighted fields.');
        return;
      }
      var data = collect();
      if (data.company_website) return; /* honeypot filled by a bot */
      delete data.company_website;

      var endpoint = cfg.formEndpoint || form.getAttribute('data-endpoint') || '';
      if (window.location.protocol === 'file:') endpoint = '';
      var wa = (cfg.whatsapp || '').replace(/\D/g, '');

      if (!endpoint) {
        /* No backend configured: hand the enquiry to WhatsApp. */
        if (!wa) { showStatus('error', 'Enquiries cannot be sent right now. Email us instead.'); return; }
        var url = 'https://wa.me/' + wa + '?text=' + encodeURIComponent(whatsappText(data));
        showStatus('info', 'Opening WhatsApp with your enquiry filled in. Press send in WhatsApp to deliver it.');
        window.open(url, '_blank', 'noopener');
        return;
      }

      pending = true;
      submitBtn.disabled = true;
      var originalLabel = submitBtn.textContent;
      submitBtn.textContent = 'Sending…';
      showStatus('info', 'Sending your enquiry…');

      fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (res) {
        return res.json().catch(function () { return {}; }).then(function (data) {
          if (!res.ok || data.ok === false) {
            if (data && data.fields) Object.keys(data.fields).forEach(function (name) {
              var input = form.querySelector('[name="' + name + '"]');
              if (input) setFieldError(input, data.fields[name]);
            });
            var err = new Error((data && data.error) || ('HTTP ' + res.status)); err.shown = !!(data && data.error); throw err;
          }
          return data;
        });
      }).then(function () {
        form.reset();
        if (country && code) code.value = '';
        showStatus('success', 'Thank you. Your enquiry has been sent. We will contact you by your preferred method during business hours (9:00 AM–7:00 PM IST).');
        status.focus && status.focus();
      }).catch(function (err) {
        showStatus('error', err && err.shown ? err.message : 'Your enquiry could not be sent. Your details are still filled in below — try again, or message us on WhatsApp.');
      }).finally(function () {
        pending = false;
        submitBtn.disabled = false;
        submitBtn.textContent = originalLabel;
      });
    });
  });
})();
