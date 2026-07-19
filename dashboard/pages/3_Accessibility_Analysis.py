import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, PALETTE

apply_custom_style()


def render_card(content_html):
    st.markdown(f"""
        <div style="background: #B4D5D6; border-radius: 10px; padding: 20px; margin-bottom: 16px;">
            {content_html}
        </div>
    """, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;'>🚶 ACCESSIBILITY ANALYSIS</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF; font-size: 1.5rem;'>"
    "The 15-Minute City, Measured by Real Street Networks</h3>",
    unsafe_allow_html=True,
)
st.markdown("---")

st.markdown("""
<p style='color:#FFFFFF; font-weight:600; font-size:1.1rem; line-height:1.7;'>
Bochum's complete pedestrian street network was acquired via OSMnx from OpenStreetMap, 
along with essential-service points of interest. A 15-minute walking threshold was 
operationalized as 1,125 meters of true network distance (at 75 meters/minute walking speed) — 
computed via Dijkstra's shortest-path algorithm, not a simple straight-line radius.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;">NETWORK NODES</p>
        <p style="color:#111111; font-weight:800; font-size:1.5rem; margin:0;">69,393</p>
    """)
with col2:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;">STREET EDGES</p>
        <p style="color:#111111; font-weight:800; font-size:1.5rem; margin:0;">169,668</p>
    """)
with col3:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;">SERVICES CHECKED</p>
        <p style="color:#111111; font-weight:800; font-size:1.5rem; margin:0;">786</p>
    """)
with col4:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;">15-MIN COVERAGE</p>
        <p style="color:#111111; font-weight:800; font-size:1.5rem; margin:0;">85.8%</p>
    """)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>What Counts as an Essential Service</h3>", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
with s1:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.95rem; margin:0 0 8px 0;">🏥 Health</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:0;">Hospitals, clinics, pharmacies</p>
    """)
with s2:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.95rem; margin:0 0 8px 0;">🎓 Education</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:0;">Schools, kindergartens</p>
    """)
with s3:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.95rem; margin:0 0 8px 0;">🛒 Daily Needs</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:0;">Supermarkets, convenience stores, parks</p>
    """)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Why Network Distance, Not a Straight-Line Radius</h3>", unsafe_allow_html=True)

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1rem; line-height:1.7; margin:0;">
        A straight-line "as the crow flies" radius overstates real accessibility — it ignores 
        rivers, rail lines, dead-end streets, and blocks a pedestrian would actually have to walk 
        around. Dijkstra's algorithm computes the true shortest walking path along the actual street 
        network from every essential-service location, giving a genuinely walkable 15-minute 
        catchment rather than an idealized circle.
    </p>
""")

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — Source: OpenStreetMap via OSMnx</p>",
    unsafe_allow_html=True,
)