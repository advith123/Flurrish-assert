/* Flourrish — shared behaviour. No dependencies. */
(function () {
  'use strict';

  var cfg = window.FLOURRISH_CONFIG || {};

  /* Header: shadow + compact logo after scrolling */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* Mobile navigation */
  var toggle = document.querySelector('.menu-toggle');
  var mobileNav = document.getElementById('mobile-nav');
  if (toggle && mobileNav) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      mobileNav.classList.toggle('is-open', open);
      document.body.classList.toggle('nav-open', open);
      if (open) {
        var first = mobileNav.querySelector('a');
        if (first) first.focus();
      }
    };
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mobileNav.classList.contains('is-open')) {
        setOpen(false);
        toggle.focus();
      }
    });
    mobileNav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 960 && mobileNav.classList.contains('is-open')) setOpen(false);
    });
  }

  /* WhatsApp links: build from config so the number lives in one place */
  var waNumber = (cfg.whatsapp || '').replace(/\D/g, '');
  if (waNumber) {
    document.querySelectorAll('[data-wa]').forEach(function (a) {
      var custom = a.getAttribute('data-wa');
      var text = custom && custom.length ? custom : (cfg.whatsappMessage || '');
      a.href = 'https://wa.me/' + waNumber + (text ? '?text=' + encodeURIComponent(text) : '');
      a.target = '_blank';
      a.rel = 'noopener';
    });
  }

  /* FAQ filter */
  var faqSearch = document.querySelector('[data-faq-search]');
  var faq = document.querySelector('[data-faq]');
  if (faqSearch && faq) {
    var items = Array.prototype.slice.call(faq.querySelectorAll('details'));
    faqSearch.addEventListener('input', function () {
      var q = faqSearch.value.trim().toLowerCase();
      var visible = 0;
      items.forEach(function (d) {
        var match = !q || d.textContent.toLowerCase().indexOf(q) !== -1;
        d.hidden = !match;
        if (match) visible++;
        if (q && match) d.open = true;
      });
      faq.classList.toggle('is-empty', visible === 0);
    });
  }

  /* Populate any "property location" select from the shared areas list */
  var areas = window.FLOURRISH_AREAS || [];
  document.querySelectorAll('select[data-areas]').forEach(function (sel) {
    areas.forEach(function (group) {
      var og = document.createElement('optgroup');
      og.label = group.zone;
      group.areas.forEach(function (name) {
        var opt = document.createElement('option');
        opt.value = name; opt.textContent = name;
        og.appendChild(opt);
      });
      sel.appendChild(og);
    });
    var other = document.createElement('option');
    other.value = 'Other / not listed'; other.textContent = 'Other / not listed';
    sel.appendChild(other);
  });

  /* Current year in footer */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
