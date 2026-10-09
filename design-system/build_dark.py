"""Generate index-dark.html from index.html by remapping the light-theme colours.

Every style is inline, and one hex can mean different things (#FFFFFF is a card
background *and* the text on navy cards), so colours are remapped per CSS property.
Re-run after every change to index.html:  python3 design-system/build_dark.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "index.html", ROOT / "index-dark.html"

PAGE, SURFACE, RAISED = "#1E2360", "#2A3175", "#353C85"
LINE = "rgba(255,255,255,0.14)"

BG = {  # background / background-color / background-image
    "#F4F5FA": PAGE, "#F7F8FC": "#232966", "#EEF0FB": "#232966", "#E9EBFA": "#232966",
    "#ECEDF8": "#232966", "#FFFFFF": SURFACE, "#E4E7EF": RAISED,
    "#E3E6F0": "rgba(255,255,255,0.06)", "#FCEFE8": "rgba(245,144,103,0.16)", "#C9CFEF": "rgba(255,255,255,0.22)", "#FEF1EB": "rgba(245,144,103,0.16)",
}
TEXT = {  # color, svg fill/stroke
    "#4D4D9F": "#FFFFFF", "#2A3373": "#FFFFFF", "#1C2258": "#FFFFFF",
    "#5B5F63": "#D7DEFF", "#6B7280": "#D7DEFF", "#9AA0AE": "#A9B1E0", "#959EA9": "#A9B1E0",
    "#C9CFEF": "#8C94CC", "#E4E7EF": LINE,
}
BORDER = {
    "#E4E7EF": LINE, "#E9EBFA": LINE, "#ECEDF8": LINE, "#C9CFEF": "rgba(255,255,255,0.25)",
    "#4D4D9F": "rgba(255,255,255,0.7)",
}
NAVY_SHADOW = re.compile(r"rgba\((?:42,\s*51,\s*115|28,\s*34,\s*88),\s*([\d.]+)\)")


def darker_shadow(m):
    return f"rgba(0,0,0,{min(float(m.group(1)) * 2.5, 0.6):.2f})"


SOLID_WHITE = re.compile(r"rgba\(255,\s*255,\s*255,\s*(0?\.[89]\d*|1)\)")  # frosted white panels


def remap(value, table):
    value = re.sub(r"#[0-9A-Fa-f]{6}\b", lambda m: table.get(m.group(0).upper(), m.group(0)), value)
    if table is BG:
        value = SOLID_WHITE.sub(lambda m: f"rgba(42,49,117,{m.group(1)})", value)
    return value


def decl(m):
    prop, value = m.group(1), m.group(2)
    p = prop.lower()
    if p in ("background", "background-color", "background-image"):
        value = remap(value, BG)
    elif p in ("color", "fill", "stroke"):
        value = remap(value, TEXT)
    elif p.startswith("border") or p == "outline":
        value = remap(value, BORDER)
    elif p == "scrollbar-color":
        value = remap(value, {"#C9CFEF": "rgba(255,255,255,0.25)"})
    if p in ("box-shadow", "filter"):
        value = NAVY_SHADOW.sub(darker_shadow, value)
    return f"{prop}:{value}"


s = SRC.read_text()
# CSS declarations, wherever they live: <style>, style="", style-hover="", JS strings
s = re.sub(r"(?<![\w-])([a-zA-Z-]+)\s*:\s*([^;\"'{}]*#[0-9A-Fa-f]{6}[^;\"'{}]*|[^;\"'{}]*rgba\([^;\"'{}]*)", decl, s)

def js_key(m):
    """Colours held in component state, e.g. `bg: a ? '#F59067' : '#FFFFFF'`, classified by key name."""
    key, value = m.group(1), m.group(2)
    k = key.lower()
    if k.endswith("bg") or k == "ring":
        table = BG
    elif k.endswith("bd"):
        table = BORDER
    elif k.endswith(("fg", "color")) or k in ("num", "sub"):
        table = TEXT
    else:
        return m.group(0)
    return f"{key}: " + re.sub(r"'([^']*)'", lambda c: f"'{remap(c.group(1), table)}'", value)


JS_VAL = r"(?:[^,\n{}()]|\([^)]*\))*"  # a value up to the next comma, keeping rgba(...) whole
s = re.sub(rf"\b(\w+):\s*({JS_VAL}'(?:#[0-9A-Fa-f]{{6}}|rgba\([^)]*\))'{JS_VAL})", js_key, s)
s = re.sub(r'\b(fill|stroke)="(#[0-9A-Fa-f]{6})"', lambda m: f'{m.group(1)}="{TEXT.get(m.group(2).upper(), m.group(2))}"', s)

# product line drawings on the (now dark) light cards: black Furnastra parts -> white, grey context -> mid grey
s = re.sub(r'(<img src="assets/products/FARNASTRA_[^"]*"[^>]*?)filter:drop-shadow\(0 0 0\.5px rgba\(0,0,0,0\.55\)\)',
           r'\1filter:invert(1) brightness(3) drop-shadow(0 0 0.5px rgba(255,255,255,0.5))', s)
# dark-header logo (has its own ™)
s = s.replace('<img src="assets/logo-header.png" alt="Furnastra" style="height:clamp(28px,2.8vw,38px);width:auto">',
              '<img src="assets/logo-header-dark.png" alt="Furnastra" style="height:clamp(28px,2.8vw,38px);width:auto">')
# the toggle goes back to the light page, with a sun icon
s = s.replace('href="index-dark.html" class="theme-toggle" aria-label="Switch to dark mode" title="Switch to dark mode"',
              'href="index.html" class="theme-toggle" aria-label="Switch to light mode" title="Switch to light mode"')
s = s.replace('<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/>',
              '<circle cx="12" cy="12" r="4.2"/><path d="M12 2v2.2M12 19.8V22M4.9 4.9l1.6 1.6M17.5 17.5l1.6 1.6M2 12h2.2M19.8 12H22M4.9 19.1l1.6-1.6M17.5 6.5l1.6-1.6"/>')

assert "index-dark.html" not in s, "toggle not flipped"
OUT.write_text(s)
print(f"wrote {OUT.name}")
