# Furnastra Homepage — Project Log

Working file: **`Furnastra Homepage v2.dc.html`**. The other `.dc.html` files are
the older v1 versions, kept for reference. The client is Furnastra, the healthcare
furniture components brand of Mitsu Chem Plast Ltd. The source material is in
`uploads/`: the company deck PDF, the brand manual and the sitemap .docx.

Backups from each major step are not in the repo. Use git history instead.

---

## Section order and status (top → bottom)

| # | id | Section | Status |
|---|---|---|---|
| — | header | Fixed white header: logo™, Product▾ / OEM Solutions / Manufacturing / About / Resources▾ / Contact, orange "Request a quote" | ✅ light theme |
| 01 | `#hero` | Hero (**load animation:** the sparkle spins in, then the eyebrow, each H1 line and the paragraph "write" left→right with a soft-edged mask wipe, then the buttons rise; `.hw` / `.hw-w` / `.hw-spark` / `.hw-up`, timed with `--d`/`--t`, ≈4s total): sparkle eyebrow, H1 on 2 lines, orange + outline buttons, bed render `p6.png` with 4 callouts (elbowed orange leader lines, hover spotlight), pale ring + grid. **Key stats strip** inside the hero: 35+ yrs / 30+ SKUs (orange) / 11 countries / 3 ISO (indigo), with an F-mark watermark in each card. **Entrance:** cards enter one by one, then number → unit → dot → label → note line by line, the F-mark slides in, and the numbers count up (`.st-grid` / `.st-c` / `.st-l` / `.st-m` CSS keyframes, paused until the strip is on screen; `data-count-now` + `data-count-delay`) | ✅ |
| 02 | `#brand-story` | "The next era of healthcare is here." Left: heading + 4-step vertical timeline (1990 / 2016 / 2022 / 2024, auto-advances, smooth expand) + "DISCOVER OUR STORY". Right: lead + paragraph, then one photo (shop floor) with a top-left rounded corner, a milestone glass pill, the year/title and a rotating ISO badge | ✅ fits one screen |
| 03 | `#story` | "Inside a Furnastra-built bed", a sticky scroll section | ⏸ **hidden** (`display:none`); restyled before hiding |
| 04 | `#products` | Component Catalogue: one-line heading + "View All Products"; 2-row bento (Raksha tall feature + 3×2: Sahara, Setu, Aakaar (orange), Rahat, Rudra, Jivan (navy)); a divider with a sparkle above it ; product visuals are the client's line drawings `assets/products/FARNASTRA_*.svg` (black = part Furnastra makes, grey `#d8d8d8` = rest of the furniture, not made by Furnastra). Light cards show them as drawn; navy/orange cards (Raksha, Aakaar, Jivan, which have no grey parts) turn them white with `filter:brightness(0) invert(1)`. Each `src` crops the 1080² artboard to the drawing with `#svgView(viewBox(x,y,w,h))` (bbox + 12px; re-measure if a drawing is re-exported), and a 0.5px same-colour `drop-shadow` thickens the hairlines. Each card stacks the static drawing with a **highlight layer** (`.pd-a`, from `assets/products/anim/`, built by `design-system/build_product_anim.py`; re-run it after the client re-exports a drawing): only the black, Furnastra-made parts in orange (navy on the orange Aakaar card), with the grey shapes used as an eraser mask. On card hover/focus a CSS mask band (`@keyframes pdSweep`, 1.6s loop) sweeps across it, starting instantly; off under `prefers-reduced-motion`. Both layers sit in the `data-tilt-img` span so they tilt together | ✅ fits one screen |
| 04b | `#talk` | Mid-page CTA panel: "Have a Hospital Furniture Requirement? Let's Talk." + Send Inquiry (orange) / WhatsApp Us (outline) | ✅ (WhatsApp number missing) |
| 05 | `#manufacturing` | **Full-bleed video section**: `assets/company-video.mp4` plays muted on loop (poster `mfg-floor.jpg`; `muted`/`loop` are set in `componentDidMount` because the framework drops those attributes; no autoplay when `animate` is off). No overlay, so the video shows in full. The copy sits in a compact frosted-glass card, bottom-left (`rgba(28,34,88,.55)` + `backdrop-filter:blur(24px) saturate(180%)`, 1px white 16% border (max-width 520px, radius 20px, F-mark watermark; heading reduced to `clamp(26px,2.4vw,36px)` at the user's request so the video stays visible): ISO/CE pills → eyebrow → "Integrated Healthcare Manufacturing Excellence." (white + light-orange accent) → lead + body → orange "Know More" (→ `#oem`). Stats strip removed at the user's request. Height = `100vh - 88px` | ✅ fits one screen |
| 05b | `#applications` | "The Right Component for the Right Care Setting." 4 photo cards (ICU, General Wards, Ambulance & Rescue, Maternity); the hovered card expands and shows its description | ✅ fits one screen |
| 05c | `#why` | Why Furnastra, **redesigned as a visual bento** (`.why-tile`): "Where Healthcare Meets Innovative Expertise." + Learn More (→ `#brand-story`). Tall navy tile: 100% ring that fills when the section enters view (`ringOn`), count-up, Design→Tooling→Moulding→QC chips. Wide white: 35+ yrs + 1990/2016/2024 timeline (line reveal). Orange: colour swatches + Colour/Finish/Spec chips. White: ISO 13485/9001/45001 + CE seals. Lavender: QA stepper Material→Moulding→Testing→PDI, ticks with the shared 4.2s timer (`step % 5`). Indigo: plant → dashed route with a moving truck (`data-drive`) → pin, Single-site / Multi-facility chips | ✅ fits one screen |
| 05d | `#news` | Latest at Furnastra (Blog & News): In the News photo card · LinkedIn post card (scrollable) · Mitsu Chem share-price chart (BSE/NSE) · Q1 results (indigo) · Annual report (orange, mock cover). **All content is dummy** | ✅ fits one screen |
| 05e | `#faq` | Frequently Asked Questions: heading + intro, navy "Still have a question?" card (Contact Us + sales@mitsuchem.com) on the left; 7-item accordion on the right (one open at a time, smooth grid-rows expand, +/− tile turns orange) | ✅ fits one screen |
| 05f | `#colours` | Colour Customisation: "Furniture that matches your space, not just any space." Left: copy, 3 benefit rows, Discuss Your Requirement (orange) / View Product Range (outline). Right: stage card (top-right signature corner) with the bed render and a finish selector, 5 swatches that auto-cycle and crossfade | ✅ fits one screen |
| 05g | `#final-cta` | Final CTA: navy panel over the `cta-hospital.jpg` photo (hospital corridor) (top-left signature corner, F-mark watermark, dashed ring). "Built for OEMs. Engineered for Healthcare." + sub-line, Contact Us (orange) / Download Catalogue (white outline), 3 glass proof pills | ✅ fits one screen |
| — | ~~`#oem`, `#legacy`, Quality, Global presence, `#resources`, `#rfq`~~ | Old dark-theme sections **removed** at the user's request (in git history if needed). Links to `#oem`, `#legacy`, `#resources` and `#rfq` currently go nowhere | 🗑 removed |
| — | back-to-top | Floating round button (bottom-right, `.to-top`): white, indigo arrow, orange SVG ring that fills with page-scroll progress. Shows after 60% of the first screen; updated directly in `handleScroll()` (no re-render) | ✅ |
| — | footer | **Dark navy footer** (user's choice; footers are the one dark block besides the Final CTA): `#1C2258`, faint grid `rgba(215,222,255,.05)`, pale ring, 2px solid orange top border (matches the header). White logo, `#D7DEFF` secondary text, orange mono labels, white links (hover `#F7B79C`), glass ISO/CE chips. Columns: brand · Products (7 + type) · Company (links to existing sections) · Corporate office (address, email, orange Request a quote → `#final-cta`). Bottom bar: © + www.furnastra.com, right-padded to clear the floating back-to-top button. **Motion:** column labels write in (`.wr`, 0/120/240ms); brand column, product and company links, contact details and bottom bar rise in one by one (`data-stagger data-rise="sm"`, 18px lift) | ✅ |

---

## How the user likes to work (feedback so far)

- They send **reference screenshots** and expect close visual matches, adapted to the light theme above (never to the old dark sections).
- **Each section should fit in one screen**; they flag anything that needs a half-scroll.
- They prefer **visual, premium layouts** over text-heavy ones.
- **Typography must match the hero** in every section: Raleway semibold indigo headings.
- They want **no section numbering** and **no `[CONFIRM]`/client flags** visible on the page.
- **White text on orange.**
- **Full-bleed photos, not transparent PNGs** in image frames.
- They want **consistent, generous spacing** between sections.
- Short instructions ("hide this", "remove this") mean exactly that; do the minimal change.

---

## Open items (need client input)

- **Latest at Furnastra (`#news`) is all dummy content.** That includes the headline, the LinkedIn post, and the **share price ₹222.10 / chart (fabricated)**, Q1 and the annual report. Connect it to real feeds (blog CMS, LinkedIn embed, BSE/NSE price API) or replace the dummy items before launch.

- **FAQ lead times:** the question asks about typical lead times, but the client's answer only says "we supply across India". Get a lead-time answer or reword the question.

- **Colour swatches (`#colours`):** Sky Blue (`p12.png`) and Teal Green (`p10.png`) are real renders. Indigo, Coral and Plum are CSS `hue-rotate` filters on `p12.png`, used as illustrations. Ask the client for their actual standard colour palette and renders.

- **Catalogue PDF:** "Download Catalogue" in `#final-cta` points to `#resources` until the client supplies the PDF (there's a TODO comment).

- **WhatsApp number:** the `#talk` WhatsApp button points to `https://wa.me/` (there's a TODO comment).
- **About page URL:** "Discover Our Story" and the "About" menu link go to `#legacy` for now. Product and resource links are `#products` / `#resources` placeholders.
- **BSE listing year:** the deck text says 2016, a slide image says 2017. The timeline uses 2016.
- **Countries:** the client copy itself conflicts: hero subtext says "12 countries", key stats strip says "11" (both client copy, Oct 2026); other sections (e.g. Final CTA pill "Supplying OEMs in 11 countries") still say 11.
- **"Four plants":** the deck shows 2 manufacturing locations + 3 warehouses.
- **30+ SKUs:** derived from 32 variants counted in the catalogue.
- **Certification scope** (ISO 13485 / 9001 / 45001 / CE) for Furnastra parts.
- **"India's leading hospital furniture components manufacturer":** a claim to confirm. "Fueled" (US spelling) vs "Fuelled" (UK).
- **Family → setting mapping** and the setting descriptions in `#applications` were written by Claude; the client should confirm them.
- **Stock photos** to be replaced with real Furnastra or plant photography.
- **Not done yet:** responsive/mobile breakpoints (there are no media queries), the RFQ form backend, SEO meta (`<title>`, description, `lang`), focus styles and reduced-motion support.

---

## Repo

`https://github.com/Crezvatic-Private-Limited/furnastra` (private), branch `main`.
