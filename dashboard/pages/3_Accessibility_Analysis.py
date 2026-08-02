import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, lead, footer_caption, card, stat_card, card_body

apply_custom_style()

page_header("🚶", "ACCESSIBILITY ANALYSIS", "The 15-Minute City, Measured by Real Street Networks")
st.markdown("---")

lead(
    "Bochum's complete pedestrian street network was acquired via OSMnx from OpenStreetMap, "
    "along with essential-service points of interest. A 15-minute walking threshold was "
    "operationalized as 1,125 meters of true network distance (at 75 meters/minute walking speed) — "
    "computed via Dijkstra's shortest-path algorithm, not a simple straight-line radius."
)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    stat_card("Network Nodes", "69,393")
with col2:
    stat_card("Street Edges", "169,668")
with col3:
    stat_card("Services Checked", "786")
with col4:
    stat_card("15-Min Coverage", "85.8%")

st.markdown("---")

st.markdown("<h3>What Counts as an Essential Service</h3>", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
with s1:
    card(card_body("🏥 <strong>Health</strong><br>Hospitals, clinics, pharmacies"))
with s2:
    card(card_body("🎓 <strong>Education</strong><br>Schools, kindergartens"))
with s3:
    card(card_body("🛒 <strong>Daily Needs</strong><br>Supermarkets, convenience stores, parks"))

st.markdown("---")

st.markdown("<h3>Why Network Distance, Not a Straight-Line Radius</h3>", unsafe_allow_html=True)

card(card_body(
    "A straight-line \"as the crow flies\" radius overstates real accessibility — it ignores "
    "rivers, rail lines, dead-end streets, and blocks a pedestrian would actually have to walk "
    "around. Dijkstra's algorithm computes the true shortest walking path along the actual street "
    "network from every essential-service location, giving a genuinely walkable 15-minute "
    "catchment rather than an idealized circle.",
    large=True,
))

st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE — Source: OpenStreetMap via OSMnx")
