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
footer_caption("GHOST INFRASTRUCTURE — Maps built in QGIS, exported via QGIS2Web")
