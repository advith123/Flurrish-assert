/* Flourrish — hero globe.
   Orthographic projection drawn on a 2D canvas. Land is a precomputed dot grid
   (assets/js/land-dots.js). Owner cities connect to Chennai with lifted arcs.
   No libraries. Respects prefers-reduced-motion and pauses off-screen. */
(function () {
  'use strict';

  var wrap = document.querySelector('[data-globe]');
  if (!wrap) return;
  var canvas = wrap.querySelector('canvas');
  var land = window.FLOURRISH_LAND;
  if (!canvas || !canvas.getContext || !land) { wrap.classList.add('no-canvas'); return; }
  var ctx = canvas.getContext('2d');
  if (!ctx) { wrap.classList.add('no-canvas'); return; }

  var DEG = Math.PI / 180;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Property hub and owner locations. Owner cities only say where owners live. */
  var HUB = { name: 'Chennai', lat: 13.08, lon: 80.27 };
  var OWNERS = [
    { name: 'New York', lat: 40.71, lon: -74.01 },
    { name: 'Toronto', lat: 43.65, lon: -79.38 },
    { name: 'Seattle', lat: 47.61, lon: -122.33 },
    { name: 'London', lat: 51.51, lon: -0.13 },
    { name: 'Dubai', lat: 25.20, lon: 55.27 },
    { name: 'Singapore', lat: 1.35, lon: 103.82 },
    { name: 'Sydney', lat: -33.87, lon: 151.21 }
  ];

  /* Unpack dots into unit vectors once */
  var dots = [];
  for (var i = 0; i < land.length; i += 3) {
    var la = land[i] * DEG, lo = land[i + 1] * DEG;
    dots.push({ x: Math.cos(la) * Math.cos(lo), y: Math.sin(la), z: Math.cos(la) * Math.sin(lo), india: land[i + 2] === 1 });
  }
  var toVec = function (lat, lon) {
    var la = lat * DEG, lo = lon * DEG;
    return { x: Math.cos(la) * Math.cos(lo), y: Math.sin(la), z: Math.cos(la) * Math.sin(lo) };
  };
  var slerp = function (a, b, t) {
    var d = Math.max(-1, Math.min(1, a.x * b.x + a.y * b.y + a.z * b.z));
    var om = Math.acos(d);
    if (om < 1e-6) return a;
    var s1 = Math.sin((1 - t) * om) / Math.sin(om), s2 = Math.sin(t * om) / Math.sin(om);
    return { x: a.x * s1 + b.x * s2, y: a.y * s1 + b.y * s2, z: a.z * s1 + b.z * s2 };
  };

  var hubV = toVec(HUB.lat, HUB.lon);
  var arcs = OWNERS.map(function (c, idx) {
    var v = toVec(c.lat, c.lon);
    var pts = [];
    var N = 56;
    for (var k = 0; k <= N; k++) {
      var t = k / N;
      var p = slerp(v, hubV, t);
      pts.push({ p: p, lift: 1 + 0.05 * Math.sin(Math.PI * t) });
    }
    return { city: c, v: v, pts: pts, offset: idx / OWNERS.length };
  });

  /* View state */
  var size = 0, dpr = 1, R = 0, cx = 0, cy = 0;
  var lam = 70 * DEG;            /* centre longitude */
  var phi = 14 * DEG;            /* centre latitude */
  var autoSpeed = 0.035;         /* rad / s */
  var dragging = false, lastX = 0, lastY = 0, velocity = 0, idleSince = 0;
  var visible = true, raf = 0, last = 0;
  var fpsInterval = 1000 / 60;

  var resize = function () {
    var rect = wrap.getBoundingClientRect();
    size = Math.max(200, Math.round(rect.width));
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = size * dpr;
    canvas.height = size * dpr;
    canvas.style.width = size + 'px';
    canvas.style.height = size + 'px';
    R = size * 0.46;
    cx = size / 2; cy = size / 2;
    fpsInterval = size < 480 ? 1000 / 30 : 1000 / 60;
    if (reduceMotion) draw();
  };

  /* Rotate a unit vector into view space: returns {x, y, z} where z faces the viewer */
  var sinL, cosL, sinP, cosP;
  var project = function (v) {
    var x1 = v.x * cosL + v.z * sinL;       /* rotate about Y by -lam */
    var z1 = -v.x * sinL + v.z * cosL;
    var y1 = v.y;
    var y2 = y1 * cosP - x1 * sinP;         /* tilt about Z-ish so centre latitude shows */
    var x2 = y1 * sinP + x1 * cosP;
    return { x: z1, y: y2, z: x2 };         /* screen x = z1, screen y = y2 (up), depth = x2 */
  };

  var draw = function () {
    sinL = Math.sin(lam); cosL = Math.cos(lam);
    sinP = Math.sin(phi); cosP = Math.cos(phi);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, size, size);

    /* Sphere */
    var g = ctx.createRadialGradient(cx - R * 0.35, cy - R * 0.4, R * 0.1, cx, cy, R);
    g.addColorStop(0, '#FFFFFF');
    g.addColorStop(0.7, '#F7F3EE');
    g.addColorStop(1, '#E9E2D9');
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2);
    ctx.fillStyle = g; ctx.fill();
    ctx.lineWidth = 1; ctx.strokeStyle = 'rgba(31,26,22,0.14)'; ctx.stroke();
    var shade = ctx.createRadialGradient(cx - R * 0.25, cy - R * 0.3, R * 0.55, cx, cy, R);
    shade.addColorStop(0, 'rgba(31,26,22,0)');
    shade.addColorStop(1, 'rgba(31,26,22,0.10)');
    ctx.fillStyle = shade; ctx.fill();

    /* Faint graticule for depth */
    ctx.strokeStyle = 'rgba(31,26,22,0.05)';
    ctx.lineWidth = 1;
    for (var latDeg = -60; latDeg <= 60; latDeg += 30) {
      ctx.beginPath();
      var started = false;
      for (var lonDeg = -180; lonDeg <= 180; lonDeg += 4) {
        var pr = project(toVec(latDeg, lonDeg));
        if (pr.z > 0) {
          var sx = cx + pr.x * R, sy = cy - pr.y * R;
          if (!started) { ctx.moveTo(sx, sy); started = true; } else ctx.lineTo(sx, sy);
        } else started = false;
      }
      ctx.stroke();
    }

    /* Land dots */
    var step = 1;
    var baseR = Math.max(1.1, R * 0.0072);
    for (var i = 0; i < dots.length; i += step) {
      var d = dots[i];
      var p = project(d);
      if (p.z <= 0.02) continue;
      var sx2 = cx + p.x * R, sy2 = cy - p.y * R;
      var depth = Math.min(1, p.z * 1.3);
      if (d.india) {
        ctx.fillStyle = 'rgba(251,82,6,' + (0.55 + 0.45 * depth).toFixed(2) + ')';
        ctx.beginPath(); ctx.arc(sx2, sy2, baseR * 1.55, 0, Math.PI * 2); ctx.fill();
      } else {
        ctx.fillStyle = 'rgba(31,26,22,' + (0.2 + 0.4 * depth).toFixed(2) + ')';
        ctx.beginPath(); ctx.arc(sx2, sy2, baseR, 0, Math.PI * 2); ctx.fill();
      }
    }

    /* Arcs */
    var now = performance.now() / 1000;
    arcs.forEach(function (arc) {
      ctx.beginPath();
      var drawing = false;
      var screenPts = [];
      for (var k = 0; k < arc.pts.length; k++) {
        var q = project(arc.pts[k].p);
        var lift = arc.pts[k].lift;
        var x = q.x * lift, y = q.y * lift, z = q.z * lift;
        var vis = z > 0.01;
        var sx3 = cx + x * R, sy3 = cy - y * R;
        screenPts.push(vis ? { x: sx3, y: sy3 } : null);
        if (vis) {
          if (!drawing) { ctx.moveTo(sx3, sy3); drawing = true; } else ctx.lineTo(sx3, sy3);
        } else drawing = false;
      }
      ctx.lineWidth = 1.25;
      ctx.strokeStyle = 'rgba(251,82,6,0.6)';
      ctx.stroke();

      /* Travelling pulse from owner city to Chennai */
      if (!reduceMotion) {
        var prog = (now * 0.12 + arc.offset) % 1;
        var idx = Math.round(prog * (screenPts.length - 1));
        var sp = screenPts[idx];
        if (sp) {
          ctx.fillStyle = '#FB5206';
          ctx.beginPath(); ctx.arc(sp.x, sp.y, 2.4, 0, Math.PI * 2); ctx.fill();
        }
      }

      /* Owner marker + label */
      var m = project(arc.v);
      if (m.z > 0.05) {
        var mx = cx + m.x * R, my = cy - m.y * R;
        ctx.fillStyle = 'rgba(31,26,22,' + (0.35 + 0.55 * Math.min(1, m.z)).toFixed(2) + ')';
        ctx.beginPath(); ctx.arc(mx, my, 3, 0, Math.PI * 2); ctx.fill();
        if (size >= 420 && m.z > 0.3) {
          ctx.font = '500 ' + Math.max(10, size * 0.021) + 'px Inter, system-ui, sans-serif';
          ctx.fillStyle = 'rgba(95,87,80,' + Math.min(1, (m.z - 0.3) * 2.2).toFixed(2) + ')';
          ctx.textBaseline = 'middle';
          ctx.fillText(arc.city.name, mx + 7, my - 1);
        }
      }
    });

    /* Chennai marker */
    var h = project(hubV);
    if (h.z > 0) {
      var hx = cx + h.x * R, hy = cy - h.y * R;
      var pulse = reduceMotion ? 0.5 : (now % 2) / 2;
      ctx.strokeStyle = 'rgba(251,82,6,' + (0.6 * (1 - pulse)).toFixed(2) + ')';
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.arc(hx, hy, 6 + pulse * 14, 0, Math.PI * 2); ctx.stroke();
      ctx.fillStyle = '#FB5206';
      ctx.beginPath(); ctx.arc(hx, hy, 5, 0, Math.PI * 2); ctx.fill();
      ctx.lineWidth = 2; ctx.strokeStyle = '#fff';
      ctx.beginPath(); ctx.arc(hx, hy, 5, 0, Math.PI * 2); ctx.stroke();
      if (size >= 320) {
        ctx.font = '700 ' + Math.max(11, size * 0.024) + 'px Manrope, Inter, system-ui, sans-serif';
        ctx.fillStyle = '#1F1A16';
        ctx.textBaseline = 'middle';
        ctx.fillText('Chennai', hx + 10, hy + 1);
      }
    }
  };

  var loop = function (ts) {
    raf = requestAnimationFrame(loop);
    if (!visible) return;
    if (ts - last < fpsInterval) return;
    var dt = Math.min(0.05, (ts - last) / 1000 || 0);
    last = ts;
    if (!dragging) {
      if (Math.abs(velocity) > 0.0005) {
        lam += velocity * dt * 60;
        velocity *= 0.93;
      } else if (ts - idleSince > 1800) {
        lam -= autoSpeed * dt;
      }
    }
    draw();
  };

  /* Drag to rotate */
  var onDown = function (e) {
    dragging = true; velocity = 0;
    lastX = e.clientX; lastY = e.clientY;
    canvas.setPointerCapture && canvas.setPointerCapture(e.pointerId);
  };
  var onMove = function (e) {
    if (!dragging) return;
    var dx = e.clientX - lastX;
    var dy = e.clientY - lastY;
    lastX = e.clientX; lastY = e.clientY;
    var dl = -dx / R * 0.9;
    lam += dl;
    phi = Math.max(-60 * DEG, Math.min(60 * DEG, phi + dy / R * 0.6));
    velocity = dl;
    if (reduceMotion) draw();
  };
  var onUp = function () {
    dragging = false;
    idleSince = performance.now();
  };
  canvas.addEventListener('pointerdown', onDown);
  canvas.addEventListener('pointermove', onMove);
  canvas.addEventListener('pointerup', onUp);
  canvas.addEventListener('pointercancel', onUp);
  canvas.addEventListener('pointerleave', function () { if (dragging) onUp(); });

  /* Pause when off-screen */
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
    }, { threshold: 0.05 }).observe(wrap);
  }

  if ('ResizeObserver' in window) new ResizeObserver(resize).observe(wrap);
  else window.addEventListener('resize', resize);
  resize();

  if (reduceMotion) {
    draw();
  } else {
    raf = requestAnimationFrame(loop);
  }
})();
