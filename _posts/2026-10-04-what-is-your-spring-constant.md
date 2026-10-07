---
layout: post
title: "What Is Your Spring Constant?"
subtitle: "I am 190 cm standing and a bit more lying down. That is enough to work out how stiff I am."
image: /assets/img/spring-constant/hero.jpg
categories: [science]
tags: [physics]
---

You are longer lying down than standing up.

Standing, gravity pushes you together: your own weight sits on your spine, your hips and your knees. Lying down it doesn't. So you get shorter when there is a force on you and longer again when the force is gone. That's a spring, right? And if I am a spring, I want to know my spring constant.

<!--more-->

### What you need

Three numbers:

- your mass $$m$$
- your length lying down $$L_0$$ (nothing pushing on you)
- your height standing $$L$$ (gravity pushing on you)

And then the difference, $$\Delta = L_0 - L$$. That is how much gravity squeezes you.

I am 190 cm standing and 92 kg. I have not measured myself lying down (yet), so I looked it up. Somebody measured eight people through the whole day, and their height went up and down by 19.3 mm on average, which is 1.1% of their height. For me 1.1% is 2.1 cm, so let's say I am 192.1 cm lying down.

The same study says more than half of it is gone in the first hour after getting out of bed. So the squeeze is slow, and that tells you how to measure it: lying down in the morning before you get up, standing in the evening. Do both a minute apart and you will find less.

### First try: Hooke's law

A spring you push on with force $$F$$ gets shorter by $$x$$:

$$
F = k\,x
$$

The force is my weight $$mg$$ and the shortening is $$\Delta$$, so

$$
k = \frac{mg}{\Delta} = \frac{92 \times 9.81}{0.021} \approx 43\ \text{kN/m}
$$

Done? Not really.

### Second try: you carry yourself

My feet carry all 92 kg. My neck only carries my head. So not every part of me gets squeezed the same. Every slice of me only feels what is on top of it.

![A stack of eight cushions with the bottom ones squashed flat, next to the same eight cushions lying in a row](/assets/img/spring-constant/stack.webp){:width="1600" height="894" loading="lazy"}

Eight of the same cushions. In the stack the bottom one carries seven others and the top one carries nothing. Next to each other they are longer than the stack is tall.
{:.figcaption}

Say I am the same everywhere from bottom to top (I am not, but let's go). Let $$s$$ run from 0 at my feet to 1 at the top of my head. The slice at $$s$$ carries everything above it, so $$(1 - s)\,mg$$. Add up all the slices:

$$
\Delta = \frac{1}{k}\int_0^1 (1 - s)\,mg\;ds = \frac{mg}{2k}
$$

So on average a slice carries half my weight. That 2 was missing in the first try:

$$
k = \frac{mg}{2\Delta} \approx 21.5\ \text{kN/m}
$$

More than 21 newton for every millimetre. A coil spring in the suspension of a car is a few tens of kN/m, so I am about as stiff as one corner of a small car.

### Now what happens with a different g?

In this model the squeeze goes with $$g$$. Twice the gravity, twice the squeeze. With $$g_E$$ for gravity on Earth, my height anywhere else is

$$
L(g) = L_0 - \Delta\,\frac{g}{g_E}
$$

![The same person with a spring for a spine on the Moon, on Earth and on a gas giant, shorter each time](/assets/img/spring-constant/planets.webp){:width="1600" height="894" loading="lazy"}

Me in three places. The drawing exaggerates, the table doesn't.
{:.figcaption}

| Where | Gravity (Earth = 1) | Squeeze | My height |
|:--|--:|--:|--:|
| In orbit | 0 | 0 cm | 192.1 cm |
| Moon | 0.17 | 0.3 cm | 191.8 cm |
| Mars | 0.38 | 0.8 cm | 191.3 cm |
| Earth | 1 | 2.1 cm | 190.0 cm |
| Jupiter | 2.53 | 5.3 cm | 186.8 cm |

So on the Moon I am 1.8 cm taller than at home, and on Jupiter (if it had a floor) 3.2 cm shorter.

In orbit the model just gives me my lying length back. Real astronauts do better than that: NASA says they can grow up to 3% in space, which would be almost 6 cm for me. A spring can't do that. I'll come back to it.

### Now sit down

Standing, the load goes through my upper body and then through my legs. Two springs on top of each other, and what they lose adds up. Sitting, my weight goes into the chair and my legs carry nothing. So sitting takes the leg spring out.

![A person standing with a spring in the torso and thicker springs in the legs, and the same person sitting with the leg springs relaxed](/assets/img/spring-constant/sitting.webp){:width="1600" height="894" loading="lazy"}

Standing loads both springs. Sitting only the top one.
{:.figcaption}

That means you can split yourself in two with a second measurement. Sitting height: from the seat to the top of your head, sitting up straight. And the same thing with no load: lie on your back with your legs up against a wall, and measure from the wall to the top of your head. The difference is $$\Delta_s$$. What is left is for the legs:

$$
\Delta_l = \Delta - \Delta_s
$$

About two thirds of your mass is above your hips. Call that $$m_u$$ and the rest $$m_l$$. The upper body carries itself, same story as before:

$$
k_{\text{spine}} = \frac{m_u\,g}{2\,\Delta_s}
$$

The legs carry the whole upper body, plus on average half of themselves:

$$
k_{\text{legs}} = \frac{\left(m_u + \tfrac{1}{2}m_l\right) g}{\Delta_l}
$$

I have not measured this one either, so as an example: say 1.6 of my 2.1 cm is in the upper body. Then $$k_{\text{spine}} \approx 19$$ kN/m and $$k_{\text{legs}} \approx 150$$ kN/m. The legs are eight times stiffer. Makes sense when you think about what is in there: big bones with a bit of cartilage in between, against a stack of 23 soft discs.

### The one without mass

A mass on a spring bounces with frequency $$f = \frac{1}{2\pi}\sqrt{k/m}$$. Put in the first try, $$k = mg/\Delta$$, and the mass drops out:

$$
f = \frac{1}{2\pi}\sqrt{\frac{g}{\Delta}} \approx 3.4\ \text{Hz}
$$

For the second try, the thing that carries itself, the lowest bounce is

$$
f = \frac{1}{4}\sqrt{\frac{k}{m}} = \frac{1}{4}\sqrt{\frac{g}{2\Delta}} \approx 3.8\ \text{Hz}
$$

So a few hertz, and all you need is a tape measure and $$g$$. Now the nice part: people have put volunteers on a shaking seat, and the body resonates up and down at roughly 4 to 6 Hz. That is a lot closer than this model deserves.

### Where it goes wrong

I am not a spring. Three things:

**It is slow.** The discs between your vertebrae are cushions filled with water. With load on them they slowly lose water, and at night they take it back. That is the 19.3 mm from before, and it is why the time of day matters more than how well you hold the tape measure. A better model is a spring with a damper next to it. It also explains the astronauts: after weeks without any load the discs swell more than one night in bed gives you.

**Posture.** Standing, your spine curves more than lying down. So part of $$\Delta$$ is just geometry.

**It is not linear.** The model says a fighter pilot in a 9 g turn gets 19 cm shorter. No.

### Your turn

These are my numbers. Put in yours.

<style>
.sk-calc { border: 1px solid rgba(128,128,128,.45); border-radius: 8px; padding: 1.1em; margin: 1.5em 0; }
.sk-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(118px, 1fr)); gap: .9em 1.1em; align-items: end; }
.sk-field { display: flex; flex-direction: column; gap: .2em; font-size: .85em; margin: 0; }
.sk-in { display: flex; align-items: baseline; gap: .4em; border-bottom: 2px solid #4fb1ba; }
.sk-in input { flex: 1; min-width: 0; width: 100%; background: transparent; color: inherit; border: 0; font-family: inherit; font-size: 1.3rem; font-weight: 600; padding: .1em 0; }
.sk-in input:focus-visible { outline: 2px solid #4fb1ba; outline-offset: 3px; }
.sk-in i { font-style: normal; opacity: .7; }
.sk-warn { margin: 1em 0 0; color: #f2a73b; }
.sk-out { display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 1em 1.1em; margin: 1.4em 0 0; }
.sk-big { display: flex; flex-direction: column; }
.sk-num { font-size: 1.9rem; font-weight: 700; line-height: 1.1; color: #f2a73b; font-variant-numeric: tabular-nums; }
.sk-unit { font-size: .8em; opacity: .75; }
.sk-cap { font-size: .85em; margin-top: .15em; }
.sk-gbox { margin-top: 1.4em; padding-top: 1.1em; border-top: 1px solid rgba(128,128,128,.35); }
.sk-grow { display: flex; justify-content: space-between; align-items: baseline; gap: 1em; }
.sk-grow output { font-variant-numeric: tabular-nums; font-weight: 600; }
.sk-calc input[type="range"] { width: 100%; accent-color: #4fb1ba; margin: .4em 0; }
.sk-presets { display: flex; flex-wrap: wrap; gap: .4em; margin: .3em 0 .8em; }
.sk-presets button { border: 1px solid rgba(128,128,128,.55); background: transparent; color: inherit; border-radius: 999px; padding: .25em .85em; font: inherit; font-size: .85em; cursor: pointer; }
.sk-presets button:hover { border-color: #4fb1ba; }
.sk-presets button[aria-pressed="true"] { background: #4fb1ba; border-color: #4fb1ba; color: #14262a; }
.sk-height { margin: 0; }
.sk-height strong { color: #f2a73b; font-variant-numeric: tabular-nums; }
.sk-plot { width: 100%; height: 260px; display: block; margin-top: .8em; }
</style>

<div class="sk-calc" id="sk-calc">
  <div class="sk-grid">
    <label class="sk-field"><span>Mass</span><span class="sk-in"><input id="sk-m" type="number" inputmode="decimal" min="1" step="0.5" value="92"><i>kg</i></span></label>
    <label class="sk-field"><span>Lying length</span><span class="sk-in"><input id="sk-l0" type="number" inputmode="decimal" min="1" step="0.1" value="192.1"><i>cm</i></span></label>
    <label class="sk-field"><span>Standing height</span><span class="sk-in"><input id="sk-l" type="number" inputmode="decimal" min="1" step="0.1" value="190"><i>cm</i></span></label>
    <label class="sk-field"><span>Sitting, lying down</span><span class="sk-in"><input id="sk-s0" type="number" inputmode="decimal" min="1" step="0.1" value="100.6"><i>cm</i></span></label>
    <label class="sk-field"><span>Sitting, upright</span><span class="sk-in"><input id="sk-s" type="number" inputmode="decimal" min="1" step="0.1" value="99"><i>cm</i></span></label>
  </div>
  <p class="sk-warn" id="sk-warn" hidden>Your lying length has to be larger than your standing height, otherwise there is no spring to measure.</p>
  <div class="sk-out">
    <div class="sk-big"><span class="sk-num" id="sk-k">21.5</span><span class="sk-unit">kN/m</span><span class="sk-cap">all of you</span></div>
    <div class="sk-big"><span class="sk-num" id="sk-ks">18.8</span><span class="sk-unit">kN/m</span><span class="sk-cap">your spine</span></div>
    <div class="sk-big"><span class="sk-num" id="sk-kl">150</span><span class="sk-unit">kN/m</span><span class="sk-cap">your legs</span></div>
    <div class="sk-big"><span class="sk-num" id="sk-f">3.8</span><span class="sk-unit">Hz</span><span class="sk-cap">your bounce</span></div>
  </div>
  <div class="sk-gbox">
    <div class="sk-grow"><label for="sk-g">Pick your gravity</label><output id="sk-gout" for="sk-g">1.00 × Earth</output></div>
    <input id="sk-g" type="range" min="0" max="3" step="0.005" value="1">
    <div class="sk-presets" id="sk-presets"></div>
    <p class="sk-height">There you stand <strong id="sk-lg">190.0 cm</strong> tall.</p>
    <svg class="sk-plot" id="sk-plot" role="img" aria-label="Your height against gravity: a straight line going down"></svg>
  </div>
</div>

<script>
(function () {
  function init() {
    var root = document.getElementById('sk-calc');
    if (!root || root.getAttribute('data-ready')) return;
    root.setAttribute('data-ready', '1');
    // The theme's link handler chokes on clicks that are not on a link; keep ours to ourselves.
    root.addEventListener('click', function (e) { e.stopPropagation(); });

    var G = 9.81, NS = 'http://www.w3.org/2000/svg';
    var PLACES = [['Orbit', 0], ['Moon', 0.165], ['Mars', 0.378], ['Earth', 1], ['Jupiter', 2.53]];
    var $ = function (id) { return document.getElementById(id); };
    var num = function (id) { var v = parseFloat(String($(id).value).replace(',', '.')); return isFinite(v) ? v : NaN; };
    var show = function (id, v, d) { $(id).textContent = isFinite(v) && v > 0 ? v.toFixed(d) : '–'; };

    var presets = $('sk-presets');
    PLACES.forEach(function (p) {
      var b = document.createElement('button');
      b.type = 'button';
      b.textContent = p[0];
      b.setAttribute('data-g', p[1]);
      b.addEventListener('click', function () { $('sk-g').value = p[1]; update(); });
      presets.appendChild(b);
    });

    function el(parent, name, attrs, text) {
      var e = document.createElementNS(NS, name);
      for (var a in attrs) e.setAttribute(a, attrs[a]);
      if (text != null) e.textContent = text;
      parent.appendChild(e);
      return e;
    }

    function draw(L0, dcm, gr) {
      var svg = $('sk-plot');
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      var W = Math.max(260, svg.clientWidth || 520), H = 260;
      svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
      var left = 46, right = 16, top = 26, bottom = 34;
      var yMax = L0 + dcm * 0.45, yMin = L0 - dcm * 3.45;
      var X = function (g) { return left + g / 3 * (W - left - right); };
      var Y = function (h) { return top + (yMax - h) / (yMax - yMin) * (H - top - bottom); };
      var soft = { stroke: 'currentColor', 'stroke-opacity': 0.22, 'stroke-width': 1, fill: 'none' };
      var i, g, h;
      for (i = 0; i <= 3; i++) {
        h = L0 - dcm * i;
        soft.d = 'M' + left + ' ' + Y(h) + 'H' + (W - right);
        el(svg, 'path', soft);
        el(svg, 'text', { x: left - 8, y: Y(h) + 4, 'text-anchor': 'end', 'font-size': 12, fill: 'currentColor', 'fill-opacity': 0.8 }, h.toFixed(1));
        el(svg, 'text', { x: X(i), y: H - 12, 'text-anchor': i === 0 ? 'start' : i === 3 ? 'end' : 'middle', 'font-size': 12, fill: 'currentColor', 'fill-opacity': 0.8 }, i + ' g');
      }
      el(svg, 'text', { x: left - 8, y: 14, 'text-anchor': 'end', 'font-size': 12, fill: 'currentColor', 'fill-opacity': 0.8 }, 'cm');
      el(svg, 'path', { d: 'M' + X(0) + ' ' + Y(L0) + 'L' + X(3) + ' ' + Y(L0 - 3 * dcm), stroke: '#4fb1ba', 'stroke-width': 2.5, fill: 'none', 'stroke-linecap': 'round' });
      PLACES.forEach(function (p) {
        g = p[1]; h = L0 - dcm * g;
        var below = p[0] === 'Moon';
        el(svg, 'circle', { cx: X(g), cy: Y(h), r: 4, fill: '#f2a73b' });
        el(svg, 'text', { x: X(g) + (below ? 0 : 5), y: Y(h) + (below ? 20 : -9), 'text-anchor': below ? 'middle' : 'start', 'font-size': 12, fill: 'currentColor' }, p[0]);
      });
      h = L0 - dcm * gr;
      el(svg, 'circle', { cx: X(gr), cy: Y(h), r: 8, fill: 'none', stroke: '#f2a73b', 'stroke-width': 2.5 });
    }

    function update() {
      var m = num('sk-m'), L0 = num('sk-l0'), L = num('sk-l'), S0 = num('sk-s0'), S = num('sk-s');
      var gr = parseFloat($('sk-g').value);
      var d = (L0 - L) / 100, ok = m > 0 && d > 0;
      $('sk-warn').hidden = ok || !(isFinite(L0) && isFinite(L));
      var ds = (S0 - S) / 100, dl = d - ds, mu = m * 2 / 3, ml = m - mu;
      var sit = ok && ds > 0 && dl > 0;
      show('sk-k', ok ? m * G / (2 * d) / 1000 : NaN, 1);
      show('sk-ks', sit ? mu * G / (2 * ds) / 1000 : NaN, 1);
      show('sk-kl', sit ? (mu + ml / 2) * G / dl / 1000 : NaN, 0);
      show('sk-f', ok ? 0.25 * Math.sqrt(G / (2 * d)) : NaN, 1);
      $('sk-gout').textContent = gr.toFixed(2) + ' × Earth';
      $('sk-lg').textContent = ok ? (L0 - (L0 - L) * gr).toFixed(1) + ' cm' : '–';
      [].forEach.call(presets.children, function (b) {
        b.setAttribute('aria-pressed', String(Math.abs(parseFloat(b.getAttribute('data-g')) - gr) < 0.005));
      });
      if (ok) draw(L0, L0 - L, gr);
    }

    ['sk-m', 'sk-l0', 'sk-l', 'sk-s0', 'sk-s', 'sk-g'].forEach(function (id) { $(id).addEventListener('input', update); });
    window.addEventListener('resize', update);
    update();
  }
  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
</script>

The spine and legs numbers assume that two thirds of your mass is above your hips. The bounce is the second formula.

### Where the numbers come from

- Tyrrell, Reilly and Troup, [Circadian variation in stature and the effects of spinal loading](https://pubmed.ncbi.nlm.nih.gov/4002039/), Spine, 1985. The 19.3 mm.
- Scientific American, [Strange but True: Astronauts Get Taller in Space](https://www.scientificamerican.com/article/astronauts-get-taller-in-space/). The 3%.
