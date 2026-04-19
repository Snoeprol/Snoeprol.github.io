---
layout: post
title: "A Short Note on the Doppler Effect"
subtitle: "What do you hear when an ambulance drives towards you faster than the speed of sound?"
categories: [science]
tags: [physics, waves]
---

I was wandering around the forest when I thought about the following scenario:

Say an ambulance drives towards you, we know (or just looked up) what happens to the pitch of the sounds. 

The sounds speeds up (or the frequency increases). Now what happens when an ambulance comes towards you faster than the speed of sound?

To answer this question let's draw out the scenarios. Below, the **red dot** is the ambulance, the **green square** is you, and wavefront color encodes emission age very explicitly:

- **cyan = OLDER emission**
- **orange = NEWER emission**

Speeds are in units where the speed of sound is \(c\).

> Each animation has **synchronized audio**. Browsers block autoplay with sound,
> so the videos start muted — **tap the speaker overlay** on any video to enable
> sound; it will restart from the beginning so the siren arrival lines up with
> the first wavefront reaching the observer. A yellow ring + “HEARING” label
> flashes on the observer when sound is currently arriving.

<style>
.doppler-video { position: relative; display: block; max-width: 100%; margin: 0 0 1em; }
.doppler-video video { width: 100%; height: auto; display: block; border-radius: 4px; background: #2A2D2F; }
.doppler-tap {
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  gap: 0.5em;
  background: rgba(0,0,0,0.45);
  color: #fff;
  border: 0; cursor: pointer;
  font: 600 1.05rem/1.2 system-ui, sans-serif;
  border-radius: 4px;
  transition: background 120ms ease;
}
.doppler-tap:hover { background: rgba(0,0,0,0.6); }
.doppler-tap[hidden] { display: none; }
.doppler-tap .icon { font-size: 1.6rem; line-height: 1; }
.doppler-think {
  border: 1px dashed #6B7280;
  background: rgba(255,255,255,0.04);
  padding: 1em 1.1em;
  border-radius: 6px;
  margin: 1em 0;
}
.doppler-think p { margin: 0 0 0.8em; }
.doppler-reveal {
  display: inline-flex; align-items: center; gap: 0.5em;
  background: #FACC15; color: #1f2937;
  border: 0; cursor: pointer;
  font: 600 0.95rem/1 system-ui, sans-serif;
  padding: 0.65em 1em; border-radius: 4px;
  transition: filter 120ms ease;
}
.doppler-reveal:hover { filter: brightness(0.95); }
.doppler-hidden { display: none !important; }
</style>

### Standing still

The source stays put; wavefronts are nested circles spaced evenly in time. The siren reaches you delayed by \(d/c\); pitch unchanged.

<div class="doppler-video">
  <video controls autoplay muted loop playsinline preload="auto" poster="/assets/img/doppler/standing_still.gif">
    <source src="/assets/img/doppler/standing_still.mp4" type="video/mp4">
    Your browser does not support video. <a href="/assets/img/doppler/standing_still.gif">View GIF</a>.
  </video>
  <button class="doppler-tap" type="button" aria-label="Tap to hear sound">
    <span class="icon">🔊</span><span>Tap to hear sound</span>
  </button>
</div>

### Moving away at the speed of sound (\(v = c\))

The ambulance recedes as fast as the waves propagate along the line of motion. Audio arrives at **half speed** (pitch dropped an octave) because each emission travels an extra \(c\,\Delta t\) before reaching you.

<div class="doppler-video">
  <video controls autoplay muted loop playsinline preload="auto" poster="/assets/img/doppler/away_mach1.gif">
    <source src="/assets/img/doppler/away_mach1.mp4" type="video/mp4">
    Your browser does not support video. <a href="/assets/img/doppler/away_mach1.gif">View GIF</a>.
  </video>
  <button class="doppler-tap" type="button" aria-label="Tap to hear sound">
    <span class="icon">🔊</span><span>Tap to hear sound</span>
  </button>
</div>

### Toward you at the speed of sound (\(v = c\))

Now the ambulance approaches at exactly \(c\). All wavefronts emitted while approaching arrive at the observer at the **same instant**. In the audio you hear silence, then a single compressed **shock burst** containing all of the buildup at once.

<div class="doppler-video">
  <video controls autoplay muted loop playsinline preload="auto" poster="/assets/img/doppler/toward_mach1.gif">
    <source src="/assets/img/doppler/toward_mach1.mp4" type="video/mp4">
    Your browser does not support video. <a href="/assets/img/doppler/toward_mach1.gif">View GIF</a>.
  </video>
  <button class="doppler-tap" type="button" aria-label="Tap to hear sound">
    <span class="icon">🔊</span><span>Tap to hear sound</span>
  </button>
</div>

### Toward you faster than sound (\(v = 2c\))

Before scrolling, **stop and think for a second**: the ambulance now moves toward you *faster* than its own sound. What do the wavefronts look like, and — more interestingly — what do you actually *hear*?

- Which waves reach you first: the ones emitted far away, or the ones emitted nearby?
- The source is going from "barely heard" to "screaming past" — does the pitch go up, down, or something stranger?

<div class="doppler-think">
  <p>Got a guess? Reveal the animation and the synced audio below.</p>
  <button class="doppler-reveal" type="button" data-target="reveal-toward-mach2">
    <span>👀</span><span>Reveal the answer</span>
  </button>
</div>

<div class="doppler-video doppler-hidden" id="reveal-toward-mach2">
  <video controls autoplay muted loop playsinline preload="auto" poster="/assets/img/doppler/toward_mach2.gif">
    <source src="/assets/img/doppler/toward_mach2.mp4" type="video/mp4">
    Your browser does not support video. <a href="/assets/img/doppler/toward_mach2.gif">View GIF</a>.
  </video>
  <button class="doppler-tap" type="button" aria-label="Tap to hear sound">
    <span class="icon">🔊</span><span>Tap to hear sound</span>
  </button>
</div>

<p class="doppler-hidden" data-revealed-with="reveal-toward-mach2">
  Past \(c\), the source <strong>outruns</strong> earlier wavefronts and the envelope forms a Mach cone. The siren turns off after a while, but already-emitted waves keep propagating. The audio mapping is \(t_e = d_0/c - t_{obs}\) on the pre-crossing branch, which is <strong>literally the source audio reversed in time</strong>. So you hear the siren played backwards, starting at the moment the shock front reaches you.
</p>

<script>
(function () {
  function init() {
    document.querySelectorAll('.doppler-video').forEach(function (wrap) {
      var v = wrap.querySelector('video');
      var b = wrap.querySelector('.doppler-tap');
      if (!v || !b) return;
      function enableSound() {
        v.muted = false;
        try { v.volume = 1.0; } catch (e) {}
        try { v.currentTime = 0; } catch (e) {}
        var p = v.play();
        if (p && p.catch) p.catch(function () {});
        b.hidden = true;
      }
      b.addEventListener('click', enableSound);
      v.addEventListener('volumechange', function () {
        if (!v.muted) b.hidden = true;
      });
    });

    document.querySelectorAll('.doppler-reveal').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var id = btn.getAttribute('data-target');
        if (!id) return;
        document.getElementById(id) && document.getElementById(id).classList.remove('doppler-hidden');
        document.querySelectorAll('[data-revealed-with="' + id + '"]').forEach(function (el) {
          el.classList.remove('doppler-hidden');
        });
        var holder = btn.closest('.doppler-think');
        if (holder) holder.remove();
      });
    });
  }
  if (document.readyState !== 'loading') init();
  else document.addEventListener('DOMContentLoaded', init);
})();
</script>

### Colored arrivals: standing still vs \(v = 2c\)

Each vertical line is a wave arrival at the observer, colored by emission age (**cyan = older, orange = newer**).  
The top strip in each panel is the emitted color order; the bottom vertical lines are what you observe in time.

Compare **standing still** (arrivals keep the same ordering as emission) with **toward at \(2c\)** (arrivals can reorder relative to emission index).

![Stacked vertical wave arrivals: standing still vs toward at 2c](/assets/img/doppler/arrival_wavefronts_still_vs_2c.png)

For the supersonic case, parts of the arrival sequence can run “backwards” relative to emission order, which is one way to think about why the perceived waveform can sound scrambled compared with what left the siren.

**Code:** [Python script for the figures and video (gist)](https://gist.github.com/Snoeprol/9f224c9e484e2925205c1a3151d46738).