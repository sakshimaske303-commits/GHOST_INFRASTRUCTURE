import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from styles import apply_custom_style, PALETTE

st.set_page_config(
    page_title="GHOST INFRASTRUCTURE",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_custom_style()


def render_card(content_html):
    st.markdown(f"""
        <div style="background: #B4D5D6; border-radius: 10px; padding: 20px; margin-bottom: 16px;">
            {content_html}
        </div>
    """, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;'>🏭 GHOST INFRASTRUCTURE</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF; font-size: 1.6rem;'>"
    "How 19th-Century Coal Geography Still Shapes Who Gets a '15-Minute Life' Today</h3>",
    unsafe_allow_html=True,
)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    render_card("<p style='color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;'>STUDY CITY</p><p style='color:#111111; font-weight:800; font-size:1.5rem; margin:0;'>Bochum</p><p style='color:#333333; font-weight:600; font-size:0.85rem; margin:4px 0 0 0;'>Ruhr Valley, Germany</p>")
with col2:
    render_card("<p style='color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;'>HISTORICAL SITES</p><p style='color:#111111; font-weight:800; font-size:1.5rem; margin:0;'>17</p><p style='color:#333333; font-weight:600; font-size:0.85rem; margin:4px 0 0 0;'>13 mines + 4 colonies</p>")
with col3:
    render_card("<p style='color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;'>NETWORK NODES</p><p style='color:#111111; font-weight:800; font-size:1.5rem; margin:0;'>69,393</p><p style='color:#333333; font-weight:600; font-size:0.85rem; margin:4px 0 0 0;'>OSMnx street network</p>")
with col4:
    render_card("<p style='color:#111111; font-weight:800; font-size:0.8rem; text-transform:uppercase; margin:0 0 8px 0;'>15-MIN COVERAGE</p><p style='color:#111111; font-weight:800; font-size:1.5rem; margin:0;'>85.8%</p><p style='color:#333333; font-weight:600; font-size:0.85rem; margin:4px 0 0 0;'>of the city</p>")

st.markdown("---")

col_left, col_right = st.columns([1.1, 1])

with col_left:
    st.markdown("""
    <h3 style='color:#7FB8BE;'>What Is Ghost Infrastructure?</h3>
    <p style='color:#FFFFFF; font-weight:600; font-size:1.1rem; line-height:1.7;'>
    Bochum's modern shape was never designed for people — it was built around
    <strong style='color:#7FB8BE;'>coal mines and steel works</strong>, with railways, roads,
    and worker-housing colonies laid out to serve 19th-century industry, not human accessibility.
    </p>
    <p style='color:#FFFFFF; font-weight:600; font-size:1.1rem; line-height:1.7;'>
    Coal mining ended in Bochum in 1973. This project asks: more than half a century later,
    does that historical industrial geography still silently determine which neighborhoods
    get a genuine <strong style='color:#7FB8BE;'>"15-minute city"</strong> — walkable access
    to essential services — and which don't?
    </p>
    """, unsafe_allow_html=True)

with col_right:
    render_card("""
        <p style="color:#111111; font-weight:800; text-transform:uppercase; font-size:0.8rem; margin:0 0 10px 0;">THE TWIST</p>
        <p style="color:#111111; font-weight:700; font-size:1rem; line-height:1.7; margin:0;">
            The hypothesis was that historical industrial sites would predict present-day
            <span style="background-color:#FFEB3B; padding:0 4px;">neglect</span>. The data said the opposite:
            proximity to historical coal-mine and colony locations statistically predicts
            <span style="background-color:#FFEB3B; padding:0 4px;">better</span> 15-minute accessibility today.
        </p>
    """)

st.markdown("---")
st.markdown("<h3 style='color:#7FB8BE;'>Three Findings</h3>", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
with f1:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.85rem; text-transform:uppercase; margin:0 0 8px 0;">Finding 1</p>
        <p style="color:#111111; font-weight:800; font-size:1.05rem; margin:0 0 8px 0;">Reversed Effect</p>
        <p style="color:#333333; font-weight:600; font-size:0.9rem; margin:0;">Low-accessibility zones are, on average, further from historical industrial sites — not closer.</p>
    """)
with f2:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.85rem; text-transform:uppercase; margin:0 0 8px 0;">Finding 2</p>
        <p style="color:#111111; font-weight:800; font-size:1.05rem; margin:0 0 8px 0;">Genuinely Independent</p>
        <p style="color:#333333; font-weight:600; font-size:0.9rem; margin:0;">The effect holds even after controlling for distance to the city center.</p>
    """)
with f3:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.85rem; text-transform:uppercase; margin:0 0 8px 0;">Finding 3</p>
        <p style="color:#111111; font-weight:800; font-size:1.05rem; margin:0 0 8px 0;">Path Dependency of Centrality</p>
        <p style="color:#333333; font-weight:600; font-size:0.9rem; margin:0;">Industrial-era cores were built dense, and that density persists today.</p>
    """)

st.markdown("---")
st.markdown("<h3 style='color:#7FB8BE;'>Explore the Research</h3>", unsafe_allow_html=True)

nav_items = [
    ("🏛️", "Study Design", "Bochum, methodology, why this city"),
    ("⛏️", "Historical Geography", "13 mines, 4 worker colonies"),
    ("🚶", "Accessibility Analysis", "The 15-minute network model"),
    ("📊", "The Finding", "Statistical test + confound verification"),
    ("🗺️", "Interactive Maps", "Live geospatial exploration"),
    ("📖", "Methodology & Data", "Sources, debugging journey, limitations"),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(nav_items):
    with cols[i % 3]:
        render_card(f"<p style='font-size: 1.6rem; margin: 0 0 6px 0;'>{icon}</p><p style='color:#111111; font-weight:800; font-size:1rem; margin:0 0 4px 0;'>{title}</p><p style='color:#333333; font-weight:600; font-size:0.85rem; margin:0;'>{desc}</p>")

st.markdown("---")

render_card("""
    <div style="text-align:center;">
        <p style="color:#333333; font-weight:700; text-transform:uppercase; letter-spacing:2px; font-size:0.85rem; margin:0 0 8px 0;">Developed by</p>
        <p style="color:#111111; font-weight:900; font-size:2.2rem; margin:0 0 8px 0;">SAKSHI D. MASKE</p>
        <p style="color:#333333; font-weight:700; font-size:1rem; margin:0;">Independent Geospatial Researcher</p>
    </div>
""")