// Illustrations for the post "What is your spring constant?", generated through OpenRouter.
// Usage: node scripts/generate_spring_constant_art.mjs [name ...]
// Key from OPENROUTER_API_KEY or ~/.config/openrouter/key.
// Original PNGs land in _art-src/spring-constant/ (not in git); the site serves the compressed copies
// from assets/img/spring-constant/. Needs ffmpeg for the conversion.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const KEY = process.env.OPENROUTER_API_KEY || fs.readFileSync(path.join(os.homedir(), '.config/openrouter/key'), 'utf8').trim();
const MODEL = process.env.MODEL || 'google/gemini-3.1-flash-image';
const ROOT = path.join(path.dirname(new URL(import.meta.url).pathname), '..');
const SRC = path.join(ROOT, '_art-src', 'spring-constant');
const OUT = path.join(ROOT, 'assets', 'img', 'spring-constant');

const STYLE = 'Flat vector editorial illustration with clean geometric shapes and thick rounded outlines in warm off-white (#e8e4da). Fills only in teal (#4fb1ba) and warm amber (#f2a73b). Solid dark charcoal background (#2a2d2f) filling the whole picture, no frame, no border. Subtle paper grain, no gradients, generous empty space. Absolutely no text, no letters, no numbers, no labels, no formulas, no watermark.';
const PERSON = 'a friendly, simple cartoon person with a round head and no facial details';

const ASSETS = {
  hero: `The same person shown twice: ${PERSON}. On the left the person stands upright and barefoot with their back against a wall, a small flat block resting on top of the head like a height measurement. On the right the same person lies flat on their back on the floor, and is visibly a little longer lying down than standing up. In both figures the spine is drawn as a clearly visible coiled metal spring running from the hips to the neck, as if the body were see-through: tight and compressed in the standing figure, relaxed and stretched in the lying figure. ${STYLE}`,
  stack: `Left: a tall vertical stack of eight identical soft round cushions standing on the floor. The cushions at the bottom are squashed almost flat by the weight of all the cushions above them, the cushions in the middle are squashed a little, and the cushion on top is not squashed at all and stays plump and tall. Right: the same eight cushions lying side by side in one row on the floor, every one of them plump and full height, so the row is clearly longer than the stack is tall. ${STYLE}`,
  planets: `Three scenes side by side, separated by thin vertical lines, each with the same person: ${PERSON}, with a clearly visible coiled metal spring for a spine. Left scene: standing on the grey cratered Moon under a black sky, the person is tallest and the spring is loose and stretched. Middle scene: standing on Earth next to a small tree, the person is of medium height. Right scene: standing on an enormous striped gas giant planet with swirling bands, the person is clearly shorter and squashed, the spring tightly compressed. One thin dashed horizontal line at the head height of the Moon person runs across all three scenes, so the height difference is easy to see. ${STYLE}`,
  sitting: `Two views of the same person side by side: ${PERSON}. Left view: the person stands upright. Inside the body two coiled metal springs are visible, one above the other: a thin spring in the torso from the hips to the neck, and a second, much thicker spring in the legs from the feet to the hips. Both springs are compressed. Right view: the person sits upright on a simple stool with the legs hanging relaxed. Only the thin torso spring is compressed, the thick leg spring is drawn loose and relaxed. ${STYLE}`,
};

// The hero is also the post's social card, so it is a JPEG; the rest are WebP.
function convert(name, raw) {
  const scale = ['-y', '-loglevel', 'error', '-i', raw, '-vf', 'scale=1600:-2:flags=lanczos'];
  if (name === 'hero') execFileSync('ffmpeg', [...scale, '-q:v', '3', path.join(OUT, 'hero.jpg')]);
  else execFileSync('ffmpeg', [...scale, '-c:v', 'libwebp', '-quality', '84', path.join(OUT, `${name}.webp`)]);
}

const names = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(ASSETS);
fs.mkdirSync(SRC, { recursive: true });
fs.mkdirSync(OUT, { recursive: true });
const LEDGER = path.join(SRC, 'spend.json');
let spent = fs.existsSync(LEDGER) ? JSON.parse(fs.readFileSync(LEDGER, 'utf8')).usd : 0;

for (const name of names) {
  const prompt = ASSETS[name];
  if (!prompt) { console.log(name, 'unknown asset'); continue; }
  const res = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: { Authorization: `Bearer ${KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: MODEL, modalities: ['image', 'text'], image_config: { aspect_ratio: '16:9' }, messages: [{ role: 'user', content: prompt }] }),
  });
  const j = await res.json();
  const url = j.choices?.[0]?.message?.images?.[0]?.image_url?.url;
  if (!url) { console.log(name, 'no image', JSON.stringify(j).slice(0, 400)); continue; }
  const [, mime, b64] = url.match(/^data:(image\/\w+);base64,(.*)$/);
  const ext = mime.split('/')[1] === 'jpeg' ? 'jpg' : mime.split('/')[1];
  const raw = path.join(SRC, `${name}.${ext}`);
  fs.writeFileSync(raw, Buffer.from(b64, 'base64'));
  convert(name, raw);
  spent += j.usage?.cost ?? 0;
  fs.writeFileSync(LEDGER, JSON.stringify({ usd: Number(spent.toFixed(4)) }) + '\n');
  console.log(name, '->', path.relative(ROOT, raw), `cost $${j.usage?.cost ?? NaN}`, `running total $${spent.toFixed(3)}`);
}
console.log(`total spent on this post so far $${spent.toFixed(4)}`);
