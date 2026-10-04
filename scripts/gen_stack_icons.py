#!/usr/bin/env python3
"""Genera partials/stack-icons.html con los iconos del stack (SVG inline).
Fuente de los logos: simple-icons (https://simple-icons.org), embebidos para no
depender de la red en tiempo de ejecucion. Comentarios en espanol."""

import os, re, urllib.request

REPO = "/home/guillermo/pagina_personal"
OUT = os.path.join(REPO, "partials", "stack-icons.html")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

ICON_BASE = "https://cdn.jsdelivr.net/npm/simple-icons@13/icons/%s.svg"

GROUPS = [
    ("Lenguajes", [
        ("Python", "python", "#3776AB"), ("R", "r", "#276DC3"), ("SQL", "postgresql", "#4169E1"),
        ("C++", "cplusplus", "#00599C"), ("Bash", "gnubash", "#4EAA25"), ("HTML", "html5", "#E34F26"),
        ("CSS", "css3", "#1572B6"), ("JavaScript", "javascript", "#E8B400"), ("LaTeX", "latex", "#008080"),
    ]),
    ("ML / Data", [
        ("MLflow", "mlflow", "#0194E2"), ("PyTorch", "pytorch", "#EE4C2C"), ("TensorFlow", "tensorflow", "#FF6F00"),
        ("scikit-learn", "scikitlearn", "#F7931E"), ("Pandas", "pandas", "#150458"), ("NumPy", "numpy", "#4D77CF"),
    ]),
    ("Herramientas", [
        ("Docker", "docker", "#2496ED"), ("FastAPI", "fastapi", "#009688"), ("Quarto", "quarto", "#39729E"),
        ("Git", "git", "#F05032"), ("GitHub", "github", "#7A7A7A"), ("Linux", "linux", "#FCC624"),
    ]),
]

_cache = {}


def icon(slug):
    if slug not in _cache:
        try:
            req = urllib.request.Request(ICON_BASE % slug, headers={"User-Agent": "gen"})
            with urllib.request.urlopen(req, timeout=10) as r:
                _cache[slug] = r.read().decode("utf-8", "ignore")
        except Exception:
            _cache[slug] = None
    return _cache[slug]


def inline(slug, color):
    svg = icon(slug)
    if not svg:
        return '<span class="tool__mono" style="background:%s">%s</span>' % (color, slug[:2].upper())
    svg = re.sub(r"<title>.*?</title>", "", svg, flags=re.S)
    # fix width/height/fill al SVG de simple-icons
    svg = svg.replace("<svg ", '<svg width="20" height="20" fill="%s" aria-hidden="true" ' % color, 1)
    return svg


groups_html = []
for group, items in GROUPS:
    chips = "".join(
        '<span class="tool"><span class="tool__ico">%s</span>%s</span>' % (inline(slug, col), name)
        for name, slug, col in items)
    groups_html.append('<div class="toolgroup"><h3>%s</h3><div class="tools">%s</div></div>' % (group, chips))

header = ("<!-- Iconos del stack: logos de simple-icons (simple-icons.org), embebidos como SVG inline.\n"
          "     Regenerar con scripts/gen_stack_icons.py si se cambian las herramientas. -->\n")

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(header + "\n".join(groups_html) + "\n")

print("escrito:", OUT, os.path.getsize(OUT), "bytes")
print("iconos embebidos:", sum(1 for s in _cache if _cache[s]), "de", sum(len(g[1]) for g in GROUPS))
