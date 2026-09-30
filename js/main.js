/* ==========================================================================
   Flourrish Asset Management — main.js
   Shared behaviour for every page. No libraries, no build step.

   1. Config
   2. Header (scroll state, active link, mobile menu)
   3. Time-zone card (home page hero)
   4. FAQ (search, topic filter, deep links)
   5. Forms -> WhatsApp (enquiry form, checklist request)
   6. WhatsApp quick details (location, property type, service)
   ========================================================================== */
(function () {
  'use strict';

  /* 1. Config ------------------------------------------------------------ */
  // WhatsApp number (country code + number, digits only). Alternate number is shown for calls only.
  var WHATSAPP_NUMBER = '919944070397';

  // Options used by the WhatsApp quick-details card (section 6).
  var AREAS = ['OMR', 'ECR', 'Sholinganallur', 'Perungudi', 'Thoraipakkam', 'Velachery', 'Adyar', 'Besant Nagar',
               'Medavakkam', 'Tambaram', 'Pallavaram', 'Chengalpattu', 'Other area in Chennai'];
  var PROPERTY_TYPES = ['Apartment / flat', 'Villa', 'Independent house', 'Office', 'Commercial property', 'Vacant plot / land', 'Other'];
  var SERVICES = ['Full property management', 'Find a tenant', 'Rent collection', 'Maintenance and repairs',
                  'Vacant property / land care', 'Inspections and video reports', 'Property tax and bills', 'Not sure yet'];

  function openWhatsApp(text) {
    window.open('https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
  }

  /* 2. Header ------------------------------------------------------------ */
  var header = document.querySelector('.hdr');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Highlight the current page in the navigation (body data-page="services" etc.)
  var page = document.body.getAttribute('data-page');
  if (page) {
    document.querySelectorAll('[data-nav="' + page + '"]').forEach(function (a) {
      a.classList.add('is-active');
      a.setAttribute('aria-current', 'page');
    });
  }

  var burger = document.querySelector('.burger');
  var mobileNav = document.getElementById('mnav');
  function setMenu(open) {
    if (!burger || !mobileNav) return;
    mobileNav.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    var use = burger.querySelector('use');
    if (use) use.setAttribute('href', open ? '#i-x' : '#i-menu');
  }
  if (burger && mobileNav) {
    burger.addEventListener('click', function () { setMenu(!mobileNav.classList.contains('is-open')); });
    mobileNav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 980) setMenu(false); });
  }

  /* 3. Time-zone card ---------------------------------------------------- */
  // Shows the visitor's local time next to Chennai's (Asia/Kolkata).
  var tzCard = document.getElementById('tz');
  if (tzCard && window.Intl) {
    var zone;
    try { zone = Intl.DateTimeFormat().resolvedOptions().timeZone; } catch (e) { zone = null; }
    var inIndia = !zone || /Kolkata|Calcutta/.test(zone);
    if (inIndia) tzCard.classList.add('is-local');
    var city = zone ? zone.split('/').pop().replace(/_/g, ' ') : '';
    var fmt = function (z) {
      return new Intl.DateTimeFormat('en-US', { hour: 'numeric', minute: '2-digit', timeZone: z }).format(new Date());
    };
    var tick = function () {
      document.getElementById('tz-che').textContent = fmt('Asia/Kolkata');
      if (!inIndia) {
        document.getElementById('tz-you').textContent = fmt(zone);
        document.getElementById('tz-city').textContent = city;
      }
      var hour = +new Intl.DateTimeFormat('en-GB', { hour: '2-digit', hourCycle: 'h23', timeZone: 'Asia/Kolkata' }).format(new Date());
      var daytime = hour >= 8 && hour < 20;
      document.getElementById('tz-dot').classList.toggle('is-night', !daytime);
      document.getElementById('tz-msg').textContent = inIndia
        ? (daytime ? 'Local owners get the same care, just closer. Message us and we\u2019ll reply today.'
                   : 'Message us now and we\u2019ll reply in the morning.')
        : (daytime ? 'It\u2019s working hours in Chennai. Message us and we\u2019ll reply today.'
                   : 'It\u2019s night in Chennai. Message us now and we\u2019ll reply in the morning.');
    };
    tick();
    setInterval(tick, 30000);
  }

  /* 4. FAQ --------------------------------------------------------------- */
  var search = document.getElementById('faq-q');
  var items = [].slice.call(document.querySelectorAll('.faq'));
  if (search && items.length) {
    var chips = [].slice.call(document.querySelectorAll('.chip'));
    var count = document.getElementById('faq-count');
    var empty = document.getElementById('faq-empty');
    var topic = 'all';

    var apply = function () {
      var term = search.value.trim().toLowerCase();
      var shown = 0;
      items.forEach(function (item) {
        var inTopic = topic === 'all' || item.getAttribute('data-cat').split(' ').indexOf(topic) > -1;
        var matches = !term || item.textContent.toLowerCase().indexOf(term) > -1;
        item.hidden = !(inTopic && matches);
        if (!item.hidden) shown++;
      });
      if (empty) empty.hidden = shown > 0;
      if (count) {
        count.textContent = (topic === 'all' && !term)
          ? 'Showing all ' + items.length + ' questions'
          : 'Showing ' + shown + ' of ' + items.length + ' questions';
      }
    };
    var setTopic = function (t) {
      topic = t;
      chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c.getAttribute('data-cat') === t)); });
      apply();
    };
    chips.forEach(function (c) { c.addEventListener('click', function () { setTopic(c.getAttribute('data-cat')); }); });
    search.addEventListener('input', apply);

    // Deep link: faq.html?topic=nri or faq.html#q7 opens that topic / question
    var params = new URLSearchParams(window.location.search);
    if (params.get('topic')) setTopic(params.get('topic'));
    if (/^#q\d+$/.test(window.location.hash)) {
      var target = document.querySelector(window.location.hash);
      if (target) target.open = true;
    }
  }

  /* 5. Forms -> WhatsApp ------------------------------------------------- */
  // The site has no server. Forms compose a WhatsApp message instead.
  // To use an email/form service later (Formspree, Netlify Forms…), replace these handlers.
  var enquiry = document.getElementById('enquiry-form');
  if (enquiry) {
    enquiry.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!enquiry.reportValidity()) return;
      var lines = ['Hi Flourrish, I would like a free consultation about my property.', ''];
      [].forEach.call(enquiry.elements, function (field) {
        if (field.name && String(field.value).trim()) lines.push(field.name + ': ' + String(field.value).trim());
      });
      openWhatsApp(lines.join('\n'));
      var ok = document.getElementById('enquiry-ok');
      if (ok) { ok.hidden = false; ok.focus(); }
    });
  }

  var guide = document.getElementById('guide-form');
  if (guide) {
    guide.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = document.getElementById('guide-email');
      if (email && email.value && !email.checkValidity()) { email.reportValidity(); return; }
      openWhatsApp('Hi Flourrish, please send me the free checklist: 10 things every NRI property owner in Chennai should check every month.' +
        (email && email.value ? '\nEmail: ' + email.value : ''));
    });
  }

  /* 6. WhatsApp quick details ------------------------------------------- */
  // Every WhatsApp button opens a short card first: where the property or land is,
  // what type it is and which service is needed. The answers are added to the
  // WhatsApp message so the team can reply properly. "Skip" opens WhatsApp directly.
  // Without JavaScript the links still work and carry the same three lines to fill in.
  if (window.HTMLDialogElement) {
    var opts = function (list) { return list.map(function (x) { return '<option>' + x + '</option>'; }).join(''); };
    var dlg = document.createElement('dialog');
    dlg.className = 'wa-dlg';
    dlg.setAttribute('aria-labelledby', 'wa-dlg-h');
    dlg.innerHTML =
      '<form class="wa-dlg__in" novalidate>' +
        '<button class="wa-dlg__x" type="button" data-close aria-label="Close"><svg class="i" aria-hidden="true"><use href="#i-x"/></svg></button>' +
        '<p class="wa-dlg__k"><svg class="wa" aria-hidden="true"><use href="#i-wa"/></svg>WhatsApp +91 99440 70397</p>' +
        '<h2 id="wa-dlg-h">Tell us about your property</h2>' +
        '<p class="wa-dlg__sub">Three quick details so our Chennai team can reply properly. They\u2019re added to your WhatsApp message.</p>' +
        '<label><span class="wa-l-loc">Where is the property or land?</span>' +
          '<input name="loc" list="wa-areas" required autocomplete="off" placeholder="e.g. Sholinganallur, OMR"></label>' +
        '<datalist id="wa-areas">' + AREAS.map(function (a) { return '<option value="' + a + '">'; }).join('') + '</datalist>' +
        '<label>Property type<select name="type" required><option value="">Select</option>' + opts(PROPERTY_TYPES) + '</select></label>' +
        '<label class="wa-owner">Service needed<select name="svc" required><option value="">Select</option>' + opts(SERVICES) + '</select></label>' +
        '<label class="wa-tenant" hidden>Monthly budget <span class="wa-opt">(optional)</span><input name="budget" inputmode="numeric" placeholder="\u20b9"></label>' +
        '<button class="btn btn--o" type="submit"><svg class="wa" aria-hidden="true"><use href="#i-wa"/></svg>Continue on WhatsApp</button>' +
        '<button class="wa-dlg__skip" type="button" data-skip>Skip and open WhatsApp</button>' +
      '</form>';
    document.body.appendChild(dlg);

    var form = dlg.querySelector('form');
    var pendingHref = '', baseLine = '', tenant = false;

    // "25000" -> "₹25,000"; anything else is passed through as typed.
    var formatBudget = function (v) {
      v = v.trim().replace(/^\u20b9\s*/, '');
      if (!v) return 'Not decided';
      var n = v.replace(/[,\s]/g, '');
      return /^\d+$/.test(n) ? '\u20b9' + Number(n).toLocaleString('en-IN') : '\u20b9' + v;
    };

    var setMode = function (isTenant) {
      tenant = isTenant;
      dlg.querySelector('.wa-l-loc').textContent = isTenant ? 'Where would you like to live?' : 'Where is the property or land?';
      dlg.querySelector('h2').textContent = isTenant ? 'What are you looking for?' : 'Tell us about your property';
      var owner = dlg.querySelector('.wa-owner'), ten = dlg.querySelector('.wa-tenant');
      owner.hidden = isTenant; ten.hidden = !isTenant;
      form.elements.svc.required = !isTenant;
    };

    document.addEventListener('click', function (e) {
      var link = e.target.closest('a[href*="wa.me/"]');
      if (!link) return;
      e.preventDefault();
      pendingHref = link.href;
      var text = '';
      try { text = new URL(link.href).searchParams.get('text') || ''; } catch (err) { text = ''; }
      baseLine = text.split('\n\n')[0] || 'Hi Flourrish, I would like to know more about your property management services.';
      setMode(/looking for a rental/i.test(baseLine));
      setMenu(false);
      dlg.showModal();
      form.elements.loc.focus();
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var f = form.elements, lines;
      if (tenant) {
        lines = ['Preferred location: ' + f.loc.value.trim(), 'Property type: ' + f.type.value,
                 'Monthly budget: ' + formatBudget(f.budget.value)];
      } else {
        lines = ['Property / land location: ' + f.loc.value.trim(), 'Property type: ' + f.type.value, 'Service needed: ' + f.svc.value];
      }
      openWhatsApp(baseLine + '\n\n' + lines.join('\n'));
      dlg.close();
    });
    dlg.querySelector('[data-skip]').addEventListener('click', function () {
      window.open(pendingHref, '_blank', 'noopener');
      dlg.close();
    });
    dlg.addEventListener('click', function (e) {
      if (e.target === dlg || e.target.closest('[data-close]')) dlg.close();
    });
  }
})();
