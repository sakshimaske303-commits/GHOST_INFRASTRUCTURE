import streamlit as st
import streamlit.components.v1 as components
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, PALETTE

apply_custom_style()


def render_card(content_html, height=200):
    components.html(f"""
        <div style="background: #B4D5D6; border-radius: 10px; padding: 24px;
                    font-family: 'Inter', sans-serif; box-sizing: border-box; height: {height-48}px;">
            {content_html}
        </div>
    """, height=height)


st.markdown("<h1 style='text-align: center;'>🗺️ INTERACTIVE MAPS</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF; font-size: 1.5rem;'>"
    "Explore the Historical and Accessibility Data Live</h3>",
    unsafe_allow_html=True,
)
st.markdown("---")

st.markdown("""
<p style='color:#FFFFFF; font-weight:600; font-size:1.1rem; line-height:1.7;'>
An interactive QGIS-built map of Bochum's historical industrial sites and present-day 
accessibility network, hosted via GitHub Pages.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Historical Geography + Accessibility Overlay</h3>", unsafe_allow_html=True)

MAP_SERVER_BASE = "https://sakshimaske303-commits.github.io/GHOST_INFRASTRUCTURE/outputs/maps"
map_url = f"{MAP_SERVER_BASE}/ghost_infrastructure_overlay_map/index.html"

components.iframe(src=map_url, height=650, scrolling=True)

render_card("""
    <p style="color:#111111; font-weight:800; text-transform:uppercase; font-size:0.8rem; margin:0 0 10px 0;">MAP LEGEND</p>
    <p style="color:#111111; font-weight:700; font-size:0.95rem; margin:0;">
        🔵 Blue Triangle — Coal Mine (1829-1974) &nbsp;|&nbsp;
        🟡 Yellow Diamond — Worker Colony (1870-1915) &nbsp;|&nbsp;
        🟢 Green Dot — High 15-Min Accessibility &nbsp;|&nbsp;
        🔴 Red Dot — Low 15-Min Accessibility
    </p>
""", height=170)

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — Maps built in QGIS, exported via QGIS2Web</p>",
    unsafe_allow_html=True,
)