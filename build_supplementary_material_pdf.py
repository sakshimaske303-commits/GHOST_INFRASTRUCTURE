"""Builds the Supplementary Material document (S1-S6) for journal submission: cover page +
one figure per page, at the 300dpi source images. Captions are copied verbatim from
MANUSCRIPT.md's "Supplementary Material" section so the submission PDF and the in-text
listing match exactly. Modeled on build_maps_plots_pdf.py's cover+index+figure-page pattern.
"""

import os
from PIL import Image
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth


def simpleSplit(text, font_name, font_size, max_width):
    """Word-wraps text to fit within max_width, returning a list of lines."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if stringWidth(candidate, font_name, font_size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

OUT_PATH = "SUPPLEMENTARY_MATERIAL.pdf"

BACKGROUND = HexColor("#0F3C65")
ACCENT = HexColor("#FFF2BA")

ITEMS = [
    {
        "file": "outputs/plots/study_area_essen.png",
        "label": "Figure S1",
        "title": "Study Area — Essen, North Rhine-Westphalia, Germany",
        "caption": "Map of Essen's administrative boundary in North Rhine-Westphalia, "
                    "Germany, directly comparable to Figure 1 (Bochum).",
    },
    {
        "file": "outputs/plots/essen_historical_geography.png",
        "label": "Figure S2",
        "title": "Essen's Historical Coal-Mining Geography, 1779-1986",
        "caption": "Essen's historical coal mining geography: 4 coal mines and 4 worker "
                    "colonies, digitized from KuLaDig and German Wikipedia, directly "
                    "comparable to Figure 2 (Bochum).",
    },
    {
        "file": "outputs/plots/threshold_sensitivity_comparison.png",
        "label": "Figure S3",
        "title": "Walking-Threshold Sensitivity: Ghost Infrastructure Effect, Bochum",
        "caption": "Effect size comparison of distance to nearest historical site by "
                    "accessibility group (left) and mean distance to nearest historical "
                    "site at 10, 15, and 20 minute thresholds (right).",
    },
    {
        "file": "outputs/plots/essen_ghost_infrastructure_overlay.png",
        "label": "Figure S4",
        "title": "Historical Geography vs. Present-Day 15-Minute Accessibility — Essen",
        "caption": "Historical industrial sites overlaid on present day 15 minute walking "
                    "accessibility in Essen, directly comparable to Figure 3 (Bochum).",
    },
    {
        "file": "outputs/plots/essen_distance_comparison_boxplot.png",
        "label": "Figure S5",
        "title": "Distance to Nearest Historical Site: High vs. Low Accessibility — Essen",
        "caption": "Distance to historical sites for high and low accessibility nodes in "
                    "Essen, comparable to Figure 4 (Bochum).",
    },
    {
        "file": "outputs/plots/essen_lisa_cluster_map.png",
        "label": "Figure S6",
        "title": "Local Moran's I Cluster Map — Essen",
        "caption": "Local Moran's I cluster map for Essen, directly comparable to Figure 5 "
                    "(Bochum).",
    },
]


def cover_page(c, width, height):
    c.setFillColor(BACKGROUND)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(width / 2, height - 2.0 * inch, "SUPPLEMENTARY MATERIAL")

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#FFFFFF"))
    c.drawCentredString(
        width / 2, height - 2.5 * inch,
        "Ghost Infrastructure: Historical Industrial Geography and the"
    )
    c.drawCentredString(
        width / 2, height - 2.78 * inch,
        "Persistence of Path Dependent Accessibility in Bochum, Germany"
    )

    c.setFont("Helvetica-Oblique", 11)
    c.setFillColor(HexColor("#C7D3DE"))
    c.drawCentredString(
        width / 2, height - 3.25 * inch,
        "Figures S1-S6 — Essen replication and threshold-sensitivity supplementary figures"
    )

    # Index
    y = height - 4.2 * inch
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
        width / 2, 1.1 * inch,
        "These figures accompany the manuscript's main-text figures 1-6 and are referenced"
    )
    c.drawCentredString(
        width / 2, 0.9 * inch,
        "inline at the corresponding points in the manuscript text."
    )

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

    caption_font_size = 9
    c.setFont("Helvetica", caption_font_size)
    caption_lines = simpleSplit(item["caption"], "Helvetica", caption_font_size, page_w - 2 * margin)
    line_h = caption_font_size * 1.3
    footer_h = 0.25 * inch + line_h * len(caption_lines)

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
    c.setFont("Helvetica", caption_font_size)
    caption_top = footer_h - 0.15 * inch
    for i, line in enumerate(caption_lines):
        c.drawString(margin, caption_top - i * line_h, line)
    c.setFont("Helvetica", 7)
    c.drawRightString(page_w - margin, 0.2 * inch, "SUPPLEMENTARY MATERIAL")

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
