import streamlit as st
import streamlit.components.v1 as components
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, lead, footer_caption, card, kicker, card_body

apply_custom_style()

page_header("🗺️", "INTERACTIVE MAPS & PLOTS", "Explore the Historical and Accessibility Data Live")
st.markdown("---")

lead(
    "Interactive Python (folium) maps of Bochum's and Essen's historical industrial sites "
    "and present-day accessibility networks, plus the three headline replication charts as "
    "hoverable, toggleable plots instead of flat images."
)

st.markdown("---")

st.markdown("<h3>Bochum — Interactive Map (Python / folium)</h3>", unsafe_allow_html=True)

lead(
    "Built directly in Python (folium) rather than QGIS. Historical sites are clickable markers "
    "with full detail; the 9,858 low-accessibility nodes are rendered as a heatmap layer rather "
    "than individual points, since that many live markers would overwhelm a browser."
)

bochum_map_path = os.path.join(PROJECT_ROOT, "outputs", "maps", "bochum_interactive_map.html")
if os.path.exists(bochum_map_path):
    with open(bochum_map_path, "r", encoding="utf-8") as f:
        bochum_map_html = f.read()
    components.html(bochum_map_html, height=650, scrolling=True)
else:
    st.warning("Bochum interactive map not found.")

card(
    kicker("Map Legend")
    + card_body(
        "🟠 Orange Marker — Coal Mine (click for name, dates) &nbsp;|&nbsp; "
        "🔵 Light-Blue Marker — Worker Colony (click for name, associated mine, dates) &nbsp;|&nbsp; "
        "🔴 Heatmap — Low 15-Min Accessibility (n=9,858 of 69,393 nodes) &nbsp;|&nbsp; "
        "Use the layer control (top-right) to toggle layers on/off",
        large=True,
    )
)

st.markdown("---")

st.markdown("<h3>Essen — Interactive Map (Python / folium)</h3>", unsafe_allow_html=True)

lead(
    "Built directly in Python (folium) rather than QGIS. Historical sites are clickable markers "
    "with full detail; the 8,267 low-accessibility nodes are rendered as a heatmap layer rather "
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

st.markdown("<h3>Interactive Plots — Replication &amp; Sensitivity</h3>", unsafe_allow_html=True)

lead(
    "The three headline statistical charts, hoverable and toggleable instead of locked into a "
    "flat image."
)

PLOTS = {
    "Bochum vs. Essen Multi-City Comparison": "outputs/plots/interactive/bochum_essen_comparison.html",
    "Walking-Time-Threshold Sensitivity": "outputs/plots/interactive/threshold_sensitivity.html",
    "Distance-to-Historical-Site Comparison": "outputs/plots/interactive/distance_comparison_boxplot.html",
}

plot_choice = st.selectbox("Select a chart", list(PLOTS.keys()))
plot_path = os.path.join(PROJECT_ROOT, PLOTS[plot_choice])
if os.path.exists(plot_path):
    with open(plot_path, "r", encoding="utf-8") as f:
        plot_html = f.read()
    components.html(plot_html, height=600, scrolling=True)
else:
    st.warning("Chart file not found.")

st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE — Bochum and Essen maps built directly in Python (folium); plots built with Plotly")
