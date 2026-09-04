---
layout: project
title: Vidimus
date: 2026-09-04
image: /assets/img/projects/vidimus.png
caption: A public, open-source evidence record for EU deforestation compliance.
description: >
  Vidimus reads public satellite archives over plots of land and produces a per-plot
  record of whether forest was cleared after the EU's 31 December 2020 cut-off — the core
  question behind the EU Deforestation Regulation. Before/after imagery pinned to the
  cut-off, tree-cover loss counted per pixel against the EU's own forest baseline, and an
  explicit record of every date nothing could be seen.
featured: true
links:
  - title: Live at vidimusearth.com
    url: https://vidimusearth.com
  - title: Source (AGPL-3.0)
    url: https://github.com/Snoeprol/vidimus
accent_color: 'rgb(63,143,122)'
accent_image:
  background: 'linear-gradient(to bottom, #0A0D12 0%, #10141B 100%)'
  overlay: false
---

*Vidimus* is the clause a medieval scribe added to a copied document — **we have seen** —
attesting the original was examined, at a stated place, on a stated day. It certifies the
act of looking, not that the contents are true. That distinction is the whole tool.

From 30 December 2026, EU importers of cocoa, coffee, soy, palm oil, rubber, cattle and
timber must hold the geolocation of every plot behind a shipment and be able to show the
ground was not deforested after the cut-off. Vidimus turns that into a checkable record.

### What makes it different from a red polygon on a map

- **Per pixel, not per plot.** Post-cut-off loss is intersected with the 2020 forest
  baseline pixel by pixel, so a clearing on ground that was already plantation in 2020 is
  not counted as deforestation.
- **It records when it could not see.** Cloud, no pre-cut-off imagery, a plot straddling two
  satellite tiles — each is a distinct state. *We could not observe this* never renders as
  *we observed nothing*.
- **Nothing is repaired quietly.** A self-intersecting boundary is refused with the
  coordinate where it crosses itself. Geometry is immutable once recorded; verdicts are
  versioned and append-only.
- **Every figure is re-derivable.** Layer, version, retrieval date and the commit that
  computed it travel with each number.

Over a thousand real plots across 26 countries and all seven regulated commodities, all
carrying Sentinel-2 imagery. Reading the record needs no account.

**Stack** — Next.js · PostGIS · Copernicus Sentinel-1/2 · Cloud-Optimized GeoTIFFs ·
MapLibre GL · a forensics engine that runs adversarial fixtures against itself on every
build.
