"""
Builds a single combined PDF of every static plot/map figure in GHOST_INFRASTRUCTURE,
with a cover page and an index, matching the pattern used for the other projects'
Maps_and_Plots PDFs.

Note: this project's one INTERACTIVE map (the QGIS2Web overlay,
outputs/maps/ghost_infrastructure_overlay_map/) is not included as a static capture here.
Its main data layer (all 69,393 accessibility nodes) is a ~21MB embedded JS file that
could not be transferred into the build environment. Its content is not actually missing
from this PDF, though: Figure 3 below (ghost_infrastructure_overlay.png) is a static
render of the exact same three layers (historical sites + accessibility nodes), produced
by the same underlying data via map1_ghost_infrastructure.py.
"""

import os
from PIL import Image
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

OUT_PATH = "GHOST_INFRASTRUCTURE_Maps_and_Plots.pdf"

BACKGROUND = HexColor("#0F3C65")
ACCENT = HexColor("#FFF2BA")
TEXT_DARK = HexColor("#111111")

ITEMS = [
    {
        "file": "outputs/plots/study_area_bochum.png",
        "label": "Figure 1",
        "title": "Study Area — Bochum, North Rhine-Westphalia, Germany",
        "caption": "Administrative boundary of Bochum, the Ruhr Valley coal and steel city "
                    "selected as this project's study area.",
    },
    {
        "file": "outputs/plots/historical_geography.png",
        "label": "Figure 2",
        "title": "Historical Industrial Geography, 1829–1974",
        "caption": "Thirteen digitized coal mines and four worker-housing colonies "
                    "(Zechensiedlungen), compiled from Mindat.org and German heritage archives.",
    },
    {
        "file": "outputs/plots/ghost_infrastructure_overlay.png",
        "label": "Figure 3",
        "title": "Historical Geography vs. Present-Day 15-Minute Accessibility",
        "caption": "All 69,393 street-network nodes, colored by 15-minute accessibility status, "
                    "overlaid with the historical mine and worker-colony locations.",
    },
    {
        "file": "outputs/plots/distance_comparison_boxplot.png",
        "label": "Figure 4",
        "title": "Distance to Nearest Historical Site: High vs. Low Accessibility",
        "caption": "Welch's t-test, t=42.887, p<0.00001 — low-accessibility nodes are, on "
                    "average, further from historical industrial sites than high-accessibility nodes.",
    },
]


def cover_page(c, width, height):
    c.setFillColor(BACKGROUND)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(width / 2, height - 2.0 * inch, "GHOST INFRASTRUCTURE")

    c.setFont("Helvetica", 15)
    c.setFillColor(HexColor("#FFFFFF"))
    c.drawCentredString(width / 2, height - 2.5 * inch, "Maps and Plots")

    c.setFont("Helvetica-Oblique", 11)
    c.setFillColor(HexColor("#C7D3DE"))
    c.drawCentredString(
        width / 2, height - 2.9 * inch,
        "How 19th-Century Coal Geography Still Shapes Who Gets a “15-Minute Life” Today"
    )

    # Index
    y = height - 4.0 * inch
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(ACCENT)
    c.drawString(1.2 * inch, y, "Index")
    y -= 0.35 * inch

    c.setFont("Helvetica", 11)
    c.setFillColor(HexColor("#FFFFFF"))
    for item in ITEMS:
        c.drawString(1.4 * inch, y, f"{item['label']}   {item['title']}")
        y -= 0.3 * inch

    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor("#9FB3C8"))
    c.drawCentredString(
        width / 2, 1.3 * inch,
        "Note: the project's interactive QGIS2Web overlay map is not captured here as a static"
    )
    c.drawCentredString(
        width / 2, 1.1 * inch,
        "image (its 69,393-node data layer could not be transferred for rendering); Figure 3"
    )
    c.drawCentredString(
        width / 2, 0.9 * inch,
        "shows the same three layers as a static render. View it live via the dashboard."
    )

    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor("#C7D3DE"))
    c.drawCentredString(width / 2, 0.5 * inch, "Sakshi D. Maske — Independent Geospatial Researcher")

    c.showPage()


def figure_page(c, item):
    img = Image.open(item["file"])
    img_w, img_h = img.size
    aspect = img_w / img_h

    if aspect >= 1:
        page_w, page_h = landscape(letter)
    else:
        page_w, page_h = letter

    c.setPageSize((page_w, page_h))
    c.setFillColor(HexColor("#FFFFFF"))
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    margin = 0.5 * inch
    header_h = 0.75 * inch
    footer_h = 0.55 * inch

    avail_w = page_w - 2 * margin
    avail_h = page_h - header_h - footer_h

    scale = min(avail_w / img_w, avail_h / img_h)
    draw_w = img_w * scale
    draw_h = img_h * scale
    x = (page_w - draw_w) / 2
    y = footer_h + (avail_h - draw_h) / 2

    c.setFillColor(BACKGROUND)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, page_h - 0.45 * inch, f"{item['label']}. {item['title']}")

    c.drawImage(item["file"], x, y, width=draw_w, height=draw_h, preserveAspectRatio=True)

    c.setFillColor(HexColor("#333333"))
    c.setFont("Helvetica", 9)
    c.drawString(margin, footer_h - 0.3 * inch, item["caption"])
    c.drawRightString(page_w - margin, footer_h - 0.3 * inch, "GHOST INFRASTRUCTURE")

    c.showPage()


def main():
    c = canvas.Canvas(OUT_PATH, pagesize=letter)
    cover_page(c, *letter)
    for item in ITEMS:
        figure_page(c, item)
    c.save()
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
