"""Build the hover-highlight layers for the client's product line drawings.

assets/products/FARNASTRA_*.svg  (black = part Furnastra makes, .cls-1 grey = rest)
  -> assets/products/anim/FARNASTRA_*.svg
     only the black parts, recoloured orange (navy for the orange Aakaar card);
     grey parts hidden. index.html lays this over the drawing (.pd-a) and sweeps
     a CSS mask band across it on card hover, so the motion starts instantly.

Re-run after the client re-exports a drawing:  python3 design-system/build_product_anim.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'products'
OUT = ROOT / 'anim'
COLOUR = {'AKAAR': '#2A3373'}  # orange card: an orange highlight would vanish

GREY = re.compile(r'<(?:path|polygon|polyline|rect|circle|ellipse|line)\b[^>]*class="cls-1"[^>]*/>')

OUT.mkdir(exist_ok=True)
for src in sorted(ROOT.glob('FARNASTRA_*.svg')):
    name = src.stem.split('_')[1]
    svg = src.read_text()
    # Black outlines continue under the grey parts; use the grey shapes as an eraser
    # so only the black that is actually visible in the drawing gets highlighted.
    eraser = ''.join(g.replace('class="cls-1"', 'fill="#000" stroke="#000" stroke-width="2"') for g in GREY.findall(svg))
    head = (' fill="%s"><style>.cls-1{display:none}</style><mask id="hm" maskUnits="userSpaceOnUse" x="0" y="0" width="1080" height="1080">'
            '<rect width="1080" height="1080" fill="#fff"/>%s</mask><g mask="url(#hm)">' % (COLOUR.get(name, '#F59067'), eraser))
    svg = re.sub(r'(<svg\b[^>]*?)>', lambda m: m.group(1) + head, svg, count=1).replace('</svg>', '</g></svg>')
    (OUT / src.name).write_text(svg)
    print(src.name)
