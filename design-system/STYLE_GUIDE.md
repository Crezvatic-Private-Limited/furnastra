# Furnastra Homepage — Style Guide (light theme)

The **light theme** is the current design direction. It applies to the redesigned
sections at the top of `Furnastra Homepage v2.dc.html`, from the header down to
Applications. The sections below Applications still use the **old dark theme**
and are being redesigned one by one. Every new or redesigned section must follow
this guide, not the old sections.

---

## 1. Colour tokens

| Token | Hex | Use |
|---|---|---|
| **Primary purple / indigo (brand)** | `#4D4D9F` | All section headings (H1/H2), card titles on light cards, outline buttons, active tabs |
| Navy | `#2A3373` | Dark cards, dark buttons, lead/strong text, timeline circles |
| Deep navy | `#1C2258` | Photo overlay gradients (`rgba(28,34,88,…)`), glass pills |
| **Orange accent (brand)** | `#F59067` | Primary buttons, eyebrow labels, category labels, accent word in headings, dots, lines |
| Orange hover | `#E97F52` | Hover state of orange buttons |
| Light orange | `#F7B79C` | Accent text on dark/photo backgrounds |
| Pale orange | `#F3C9B3` | Inactive timeline line |
| Orange tint | `#FCEFE8` | Icon tile background on white cards |
| Page light bg | `#F4F5FA` | Hero, Manufacturing, light cards, CTA panel |
| Lavender 1 | `#EEF0FB` | Alternate light cards, chips on white |
| Lavender 2 | `#E9EBFA` / `#ECEDF8` | Decorative thick rings |
| Border | `#E4E7EF` | Card borders, dividers |
| Grid line | `#E3E6F0` | Background grid pattern |
| Ring dashed | `#C9CFEF` | Dashed rotating rings, inactive outlines |
| Light indigo | `#D7DEFF` | Secondary text on navy |
| Body text | `#5B5F63` | Paragraphs |
| Muted | `#6B7280` | Mono captions, "/ 04" style counters |
| White | `#FFFFFF` | Text on orange/navy, white cards |

**Legacy, do not use in new work:** `#959EA9` (old muted),
`#C0C8D4` and Outfit font colours. These only appear in the old dark sections.

**Orange cards:** use **white text** on `#F59067`. The user chose white over navy.

---

## 2. Typography

Fonts load from Google Fonts in `<helmet>`: **Raleway** (400–800) and
**JetBrains Mono** (500). `body` sets `font-variant-numeric:lining-nums`, because
Raleway's default old-style figures look uneven.

**Do not use Outfit or "Nexa"** in new work. They are legacy.

| Role | Spec |
|---|---|
| H1 / H2 (all section headings) | Raleway **600**, `font-size:clamp(30px,3.6vw,52px)`, `line-height:1.16`, `letter-spacing:-0.015em`, colour `#4D4D9F`. The last word or phrase is often in orange `#F59067`, e.g. "…is here.", "Let's Talk.", "Excellence." Sentence or title case; **never all caps**. |
| Hero H1 | Same spec. Two lines locked with `white-space:nowrap` spans: "Components Engineered / for Healthcare Furniture." |
| Eyebrow (section label) | JetBrains Mono, `11.5px`, `letter-spacing:0.12em`, uppercase, `#F59067`. **No numbering**: write "OUR STORY", not "02 — OUR STORY". |
| Hero-style eyebrow | Sparkle icon (see §5) + Raleway 500, `letter-spacing:0.06em`, `#F59067` |
| Lead line | Raleway 500, `clamp(18px,1.55vw,22px)`, `#2A3373` |
| Body | Raleway 400, `clamp(15.5px,1.2vw,17.5px)`, `line-height:1.65–1.7`, `#5B5F63` |
| Card title (large) | Raleway 600, `clamp(36px,3.4vw,52px)` |
| Card title (small) | Raleway 600, `clamp(18px,1.6vw,30px)` depending on tile |
| Category label | `11.5–12px`, weight 600, `letter-spacing:0.08em`, uppercase, `#F59067` (white on orange or navy) |
| Chips | `11.5–12px`, weight 600, pill `border-radius:999px`, padding `5–6px 10–11px`; on white: bg `#EEF0FB`, text `#4D4D9F`; on dark or photo: `rgba(255,255,255,.16)` + 1px `rgba(255,255,255,.22)` border |
| Big numbers / stats | Raleway 500–600, lining nums, `clamp(28px,3vw,60px)` |
| Mono tags / captions | JetBrains Mono `10–10.5px`, `letter-spacing:0.08–0.12em` |

---

## 3. Buttons

All buttons: `border-radius:12px`, weight **500**, `letter-spacing:0.03em`,
`font-size:clamp(15px,1.2vw,17px)` (16px typical), a trailing arrow
`<span>→</span>`, `gap:14px`, `white-space:nowrap`. Hover is set with the
framework's `style-hover="…"` attribute.

| Variant | Style |
|---|---|
| Primary | bg `#F59067`, text `#FFFFFF`, hover bg `#E97F52`. Padding `clamp(14px,1.2vw,18px) clamp(22px,2vw,30px)` |
| Secondary (outline) | bg transparent or white, `1.5px solid #4D4D9F`, text `#4D4D9F`; hover: fill `#4D4D9F` + white text, or white bg |
| Dark | bg `#2A3373`, white text, hover `#4D4D9F`. Used for "DISCOVER OUR STORY" (the only uppercase button, `letter-spacing:0.06em`) |
| Header CTA | Orange, white text, sentence case "Request a quote →", radius 12px |

Never use pill-shaped (999px) buttons or square (2px) buttons in new work.

---

## 4. Layout and spacing

- **Container:** `max-width:1440px;margin:0 auto;padding:0 clamp(20px,4vw,72px)`. Every section uses this horizontal padding so left edges line up.
- **Header:** fixed, white, **86px + 2px orange bottom border = 88px**. Sections use `scroll-margin-top:88px`. The hero has `padding-top:88px`.
- **One section = one screen.** The user wants each section to fit in a single viewport. The reference viewports are **1440×900** and **≈1504×731**. Techniques:
  - vertical padding in `vh`: `clamp(28px,4.5vh,56px)` to `clamp(40px,6vh,96px)`
  - grid row heights tied to viewport height, e.g. `grid-template-rows:repeat(2,clamp(180px,calc((100vh - 88px - 250px) / 2),290px))`
  - one-line headers with the CTA button on the same row (`justify-content:space-between;align-items:flex-end`)
  - small cards use absolute-positioned images so card height never depends on image size
- **Breathing room between white sections:** bottom padding `clamp(88px,9vw,136px)`, plus an optional divider: hairline `#E4E7EF` with an orange sparkle in the centre.
- **Cards:** `border-radius:18–20px`; white cards get `border:1px solid #E4E7EF`; padding `clamp(18px,1.7vw,26px)`.
- **Bento grids:** a feature tile spanning 2 rows plus a 3×2 or 2×2 grid of small tiles. Alternate the feature tile side between sections (catalogue: left, manufacturing: right).
- **Signature corner:** large photo frames have **one** big rounded corner, `clamp(90px,9vw,140px)`, echoing the F-mark arc (Our Story image: top-left; Manufacturing photo: top-right).

---

## 5. Brand motifs (reuse these)

- **Background grid:** `background-image:linear-gradient(#E3E6F0 1px,transparent 1px),linear-gradient(90deg,#E3E6F0 1px,transparent 1px);background-size:56px 56px;opacity:0.55` on an absolute layer.
- **Pale ring:** an absolute circle with a thick border `clamp(40px,6vw,90px) solid #E9EBFA`, partly off-canvas.
- **Rotating dashed ring:** `border:1px dashed #C9CFEF` + `data-spin="80"` + a 10–12px orange dot on its edge.
- **Sparkle (4-point star) SVG**, used for eyebrows, dividers and timeline ends:
  ```html
  <svg width="18" height="18" viewBox="0 0 20 20" aria-hidden="true"><path d="M10 0c.6 5.2 4.8 9.4 10 10-5.2.6-9.4 4.8-10 10-.6-5.2-4.8-9.4-10-10C5.2 9.4 9.4 5.2 10 0Z" fill="#F59067"/></svg>
  ```
- **F-mark watermark in card corners:** a CSS mask of the logo mark:
  ```html
  <span aria-hidden="true" style="position:absolute;right:-14px;bottom:-18px;height:clamp(120px,10vw,150px);aspect-ratio:126.7/140.9;background:rgba(255,255,255,0.08);-webkit-mask:url(assets/f-mark.svg) center/contain no-repeat;mask:url(assets/f-mark.svg) center/contain no-repeat"></span>
  ```
  Tint: `#EEF0FB` on white, `rgba(255,255,255,.14)` on orange, `rgba(255,255,255,.08)` on indigo or navy.
- **Photo treatment:** always full-bleed `object-fit:cover` photos. **Never** put transparent product PNGs inside photo frames; the user said it "looks cheap". Overlay a navy gradient, e.g. `linear-gradient(180deg,rgba(28,34,88,.5) 0%,rgba(28,34,88,.05) 30%,rgba(28,34,88,.2) 55%,rgba(28,34,88,.92) 100%)`, so white text at the bottom stays readable.
- **Tags on photos:** a glass pill, `background:rgba(28,34,88,.82);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.14);border-radius:999px`, with white mono text and a 6px orange dot. Plain orange text on a photo is **not** readable.
- **Product renders** (transparent PNGs `assets/p*.png`) belong on solid-colour cards (catalogue), never on photos.

---

## 6. Motion (built into the component script)

Add these attributes to elements. They are handled in `scan()` and respect the `animate` prop.

| Attribute | Effect |
|---|---|
| `data-reveal="up|scale|line"` + `data-delay="ms"` | fade/slide in on scroll (56px / 1.4s soft ease-out). The element's own inline `transition` is restored afterwards |
| `data-stagger` | card grids/lists: the children rise in one after another (56px rise, 1.4s soft ease-out, 130ms apart). It's CSS-driven: an observer sets `data-in` on the container, then `data-done` once finished so the cards' own hover transitions apply again. The attribute value is ignored. Works for up to 12 children. Add `data-rise="sm"` for an 18px lift on small text such as footer links |
| `data-float="px" data-dur="ms"` | gentle vertical float |
| `data-spin="seconds"` (negative = reverse) | continuous rotation |
| `data-count="N" data-suffix="+"` | count-up when visible (numbers ≥1000 use `en-IN` grouping) |
| `data-tilt` + `data-tilt-img` | 3D tilt card on hover |
| `data-pulse` | pulsing halo (hero dots) |
| `data-depth="N"` | mouse parallax |
| `data-count-now` + `data-count-delay="ms"` | with `data-count`: count up even when on screen at load, starting after a delay |
| `data-drive` | loop an element left→right across its parent (the Why Furnastra truck) |

**Items inside `<sc-for>` that are on screen at load:** `data-reveal`/`data-stagger` can miss them (the list renders after the first `scan()`). Use CSS keyframes with `animation-play-state:paused` and start them with an IntersectionObserver instead, as in the hero key-stats strip (`.st-grid`).

**"Writing" text reveal (hero):** put `class="hw-w"` with `style="--d:<delay>ms;--t:<duration>ms"` on a block of text inside a `.hw` container. A `260%`-wide gradient mask slides from right to left, so the text appears left→right with a soft edge. **Section headings use the same effect, scroll-triggered:** give every section's **eyebrow** `class="wr" style="--d:0ms;…"` and its **H2** `class="wr" style="--d:220ms;…"`. They stay paused until 60% visible (an IntersectionObserver sets `data-in`). Don't also put `data-reveal` on the header wrapper. Keep it to eyebrows + headings; body text, cards and buttons keep the normal `data-reveal`/`data-stagger` fade so the page doesn't feel over-animated.

`.hw`, `.st-grid` and `.wr` all get `data-static` when the `animate` prop is off.

Height changes must animate smoothly. Use the `display:grid;grid-template-rows:0fr→1fr` + `opacity` pattern (see the Brand Story timeline and the `.set-card .set-desc` CSS). **Never** toggle content with `sc-if`, because it makes the layout jump.

---

## 7. Framework notes (`.dc.html` + `support.js`)

- Markup lives in `<x-dc>`. Head/CSS goes in `<helmet>`, where the global `<style>` holds the shared classes (`.nav-link`, `.nav-dd`, `.dd-*`, `.set-row`, `.set-card`).
- Bindings: `{{ value }}`; loops: `<sc-for list="{{ items }}" as="x">`; conditionals: `<sc-if value="{{ flag }}">`; hover: `style-hover="…"`.
- Logic: `class Component extends DCLogic`, where `renderVals()` returns every bound value. Data arrays (`keyStats`, `milestones`, `callouts`, `storyData`, …) live there.
- **Only files ending in `.dc.html` render.** A temporary copy named `*.html` stays blank.
- The IDE shows CSS "errors" for `{{ }}` inside `style=""`. These are **false positives**; ignore them.
- **Gotcha:** a global `a:hover{color:#2A3373}` exists. A card built as `<a>` must pin its text colour (e.g. `a.set-card,a.set-card:hover{color:#FFFFFF}`) or the text turns navy on hover.
- The `showFlags` prop shows `[CONFIRM]` review notes. The user has asked to **remove** these notes from redesigned sections; don't add new ones.

### How to verify visually

```bash
cd /Applications/XAMPP/xamppfiles/htdocs/furnastra
python3 -m http.server 8765 &   # serve the folder
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --hide-scrollbars \
  --window-size=1440,900 --virtual-time-budget=6000 --screenshot=/tmp/shot.png \
  "http://localhost:8765/Furnastra%20Homepage%20v2.dc.html"
pkill -f "http.server 8765"
```

For sections below the fold, extract the `<section>` into a static HTML file with the
Raleway/JetBrains links, a fake 88px header and the relevant helmet CSS, then screenshot
that at 1440×900 and 1504×731. Measure the section height with
`getBoundingClientRect()` to confirm the one-screen fit.

---

## 8. Imagery

- **Stock photos** (free Unsplash licence, no attribution required) are **placeholders** until the client supplies real ones:
  - `assets/story-moulding.jpg`
  - `assets/mfg-floor.jpg`
  - `assets/setting-icu.jpg`, `assets/setting-ward.jpg`, `assets/setting-ambulance.jpg`, `assets/setting-maternity.jpg`
  - `assets/story-ward.jpg` is unused, because it shows a competitor's "GITA" branding.
- Resize photos to ≤1400px wide with `sips -Z 1400 -s formatOptions 72-78` (aim for <400 KB).
- `ref/img/*.jpg` holds renders on black backgrounds and is not usable as photos. `ref/img/j002.jpg` (the BSE photo) says "2017" and conflicts with the 2016 milestone.
