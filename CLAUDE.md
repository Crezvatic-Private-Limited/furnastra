# Furnastra Homepage — read this first

You are continuing the redesign of **`Furnastra Homepage v2.dc.html`**.

Before you design or edit anything, read:

1. **`design-system/STYLE_GUIDE.md`**: colour tokens, typography, buttons, layout,
   motifs, motion attributes, framework gotchas and how to verify visually.
2. **`design-system/PROJECT_LOG.md`**: the section order, which sections are done
   or still old, the user's preferences, and open client items.

## Non-negotiables (summary)

- Use the **light theme** of the top sections (header → Applications). The dark sections
  below are legacy, so don't copy their style.
- Headings: Raleway **600**, `clamp(30px,3.6vw,52px)`, `#44499E`, with an orange (`#E8966C`)
  accent on the last word. Eyebrows: JetBrains Mono 11.5px, orange, **no numbering**.
- Buttons: `border-radius:12px`, weight 500. Primary is orange with white text;
  secondary is outlined in `#44499E`.
- Container `max-width:1440px`, side padding `clamp(20px,4vw,72px)`, fixed header **88px**.
- **Every section must fit one screen** (check at 1440×900 and 1504×731).
- Prefer visual, premium layouts, and use full-bleed photos (never transparent PNGs) in photo frames.
- Don't add `[CONFIRM]` flags or section numbers to the page.
- Only `.dc.html` files render. CSS "errors" on `{{ }}` in the IDE are false positives.
- Verify each change with a headless Chrome screenshot before you report it as done.

When you finish a section, update the status table in `design-system/PROJECT_LOG.md`.
