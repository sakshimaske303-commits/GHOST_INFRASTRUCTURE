import streamlit as st
import streamlit.components.v1 as components
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, lead, footer_caption, card, kicker, card_body

apply_custom_style()

page_header("🗺️", "INTERACTIVE MAPS", "Explore the Historical and Accessibility Data Live")
st.markdown("---")

lead(
    "An interactive QGIS-built map of Bochum's historical industrial sites and present-day "
    "accessibility network, hosted via GitHub Pages."
)

st.markdown("---")

st.markdown("<h3>Historical Geography + Accessibility Overlay</h3>", unsafe_allow_html=True)

MAP_SERVER_BASE = "https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/maps"
map_url = f"{MAP_SERVER_BASE}/ghost_infrastructure_overlay_map/index.html"

components.iframe(src=map_url, height=650, scrolling=True)

card(
    kicker("Map Legend")
    + card_body(
        "🔵 Blue Triangle — Coal Mine (1829-1974) &nbsp;|&nbsp; "
        "🟡 Yellow Diamond — Worker Colony (1870-1915) &nbsp;|&nbsp; "
        "🟢 Green Dot — High 15-Min Accessibility &nbsp;|&nbsp; "
        "🔴 Red Dot — Low 15-Min Accessibility",
        large=True,
    )
)

st.markdown("---")

st.markdown("<h3>Essen — Interactive Map (Python / folium)</h3>", unsafe_allow_html=True)

lead(
    "Built directly in Python (folium) rather than QGIS, as a working stand-in until a polished "
    "QGIS2Web export — matching the Bochum map above — is built later. Historical sites are clickable "
    "markers with full detail; the 8,267 low-accessibility nodes are rendered as a heatmap layer rather "
    "than individual points, since that many live markers would overwhelm a browser."
)

essen_map_path = os.path.join(PROJECT_ROOT, "outputs", "maps", "essen_interactive_map.html")
if os.path.exists(essen_map_path):
    with open(essen_map_path, "r", encoding="utf-8") as f:
        essen_map_html = f.read()
    components.html(essen_map_html, height=650, scrolling=True)
else:
    st.warning("Essen interactive map not found.")

card(
    kicker("Map Legend")
    + card_body(
        "🟠 Orange Marker — Coal Mine (click for name, dates, source) &nbsp;|&nbsp; "
        "🔵 Light-Blue Marker — Worker Colony (click for name, dates, source) &nbsp;|&nbsp; "
        "🔴 Heatmap — Low 15-Min Accessibility (n=8,267 of 72,027 nodes) &nbsp;|&nbsp; "
        "Use the layer control (top-right) to toggle layers on/off",
        large=True,
    )
)

st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE — Bochum map built in QGIS (QGIS2Web); Essen map built in Python (folium)")
