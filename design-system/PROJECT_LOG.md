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
| 01 | `#hero` | Hero: sparkle eyebrow, H1 on 2 lines, orange + outline buttons, bed render `p6.png` with 4 callouts (elbowed orange leader lines, hover spotlight), pale ring + grid. **Key stats strip** inside the hero: 35+ yrs / 30+ SKUs (orange) / 11 countries / 3 ISO (indigo), with an F-mark watermark in each card | ✅ |
| 02 | `#brand-story` | "The next era of healthcare is here." Left: heading + 4-step vertical timeline (1990 / 2016 / 2022 / 2024, auto-advances, smooth expand) + "DISCOVER OUR STORY". Right: lead + paragraph, then one photo (shop floor) with a top-left rounded corner, a milestone glass pill, the year/title and a rotating ISO badge | ✅ fits one screen |
| 03 | `#story` | "Inside a Furnastra-built bed", a sticky scroll section | ⏸ **hidden** (`display:none`); restyled before hiding |
| 04 | `#products` | Component Catalogue: one-line heading + "View All Products"; 2-row bento (Raksha tall feature + 3×2: Sahara, Setu, Aakaar (orange), Rahat, Rudra, Jivan (navy)); a divider with a sparkle above it | ✅ fits one screen |
| 04b | `#talk` | Mid-page CTA panel: "Have a Hospital Furniture Requirement? Let's Talk." + Send Inquiry (orange) / WhatsApp Us (outline) | ✅ (WhatsApp number missing) |
| 05 | `#manufacturing` | "Integrated Healthcare Manufacturing Excellence." Bento: Testing & Quality (white), Certifications (indigo), In-house R&D (orange, wide), Infrastructure (photo, tall, right) with counters 4 / 22 / 57 / 36,000+ | ✅ fits one screen |
| 05b | `#applications` | "The Right Component for the Right Care Setting." 4 photo cards (ICU, General Wards, Ambulance & Rescue, Maternity); the hovered card expands and shows its description | ✅ fits one screen |
| 05c | `#why` | Why Furnastra: "Where Healthcare Meets Innovative Expertise." + Learn More. 3 benefit cards (right-aligned) · centre seal (rotating dashed ring, pale ring, navy core "100% in-house manufacturing · since 1990") · 3 benefit cards. Cards: hover lift, orange icon tile fills | ✅ fits one screen |
| 05d | `#news` | Latest at Furnastra (Blog & News): In the News photo card · LinkedIn post card (scrollable) · Mitsu Chem share-price chart (BSE/NSE) · Q1 results (indigo) · Annual report (orange, mock cover). **All content is dummy** | ✅ fits one screen |
| 06 | `#oem` | OEM / custom development (7-step process) | ⏳ **old theme**, to redesign |
| 07 | `#legacy` | Furnastra + Mitsu Chem (overlaps with Brand Story; consider merging or cutting) | ⏳ old |
| 08 | — | Quality at every stage + certs marquee | ⏳ old |
| 09 | — | Global presence (11 countries, 4 regions) | ⏳ old |
| 10 | `#resources` | Resources (4 cards) | ⏳ old |
| 11 | `#rfq` | Request a quote form (not functional, no backend) | ⏳ old |
| — | footer | Dark footer | ⏳ old |

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

- **WhatsApp number:** the `#talk` WhatsApp button points to `https://wa.me/` (there's a TODO comment).
- **About page URL:** "Discover Our Story" and the "About" menu link go to `#legacy` for now. Product and resource links are `#products` / `#resources` placeholders.
- **BSE listing year:** the deck text says 2016, a slide image says 2017. The timeline uses 2016.
- **Countries:** 11 on the site, but one client copy said "12".
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
