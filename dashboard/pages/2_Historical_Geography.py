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


st.markdown("<h1 style='text-align: center;'>⛏️ HISTORICAL GEOGRAPHY</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF; font-size: 1.5rem;'>"
    "13 Coal Mines, 4 Worker Colonies — Digitized From Archives</h3>",
    unsafe_allow_html=True,
)
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;">EARLIEST MINE</p>
        <p style="color:#111111; font-weight:800; font-size:1.4rem; margin:0;">1829</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:4px 0 0 0;">Vereinigte Engelsburg</p>
    """)
with col2:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;">LAST MINE CLOSED</p>
        <p style="color:#111111; font-weight:800; font-size:1.4rem; margin:0;">1974</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:4px 0 0 0;">Holland Colliery</p>
    """)
with col3:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;">DATA SOURCE</p>
        <p style="color:#111111; font-weight:800; font-size:1.4rem; margin:0;">Mindat.org</p>
        <p style="color:#333333; font-weight:600; font-size:0.85rem; margin:4px 0 0 0;">Compiled record by record</p>
    """)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE; text-align:center;'>The Industrial Skeleton of Bochum</h3>", unsafe_allow_html=True)

image_path = os.path.join(PROJECT_ROOT, "outputs", "plots", "historical_geography.png")
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning("Historical geography map not found.")

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1rem; line-height:1.7; margin:0;">
        Mines (blue triangles) and worker-housing colonies (yellow squares) were compiled 
        independently and kept as two structurally distinct layers by design: a mine is an 
        extraction site, a colony is residential housing. A proposed steelworker colony 
        (Stahlhausen) was explicitly excluded during review since it belonged to a different 
        industry (steel, not coal).
    </p>
""")

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE; text-align:center;'>The Full Ghost Infrastructure Overlay</h3>", unsafe_allow_html=True)

image_path2 = os.path.join(PROJECT_ROOT, "outputs", "plots", "ghost_infrastructure_overlay.png")
if os.path.exists(image_path2):
    st.image(image_path2, use_container_width=True)
else:
    st.warning("Overlay map not found.")

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1rem; line-height:1.7; margin:0;">
        The same 17 historical sites overlaid on 69,393 present-day street-network nodes, colored 
        by 15-minute accessibility status. Green dots dominate the interior; red dots — genuine 
        accessibility gaps — concentrate toward the periphery, further from the historical 
        industrial core.
    </p>
""")

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — Sources: Mindat.org, German heritage archives</p>",
    unsafe_allow_html=True,
)