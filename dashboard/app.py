import streamlit as st
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
from styles import (
    apply_custom_style, page_header, lead,
    card, kicker, card_title, card_body, stat_card, nav_card,
    PALETTE,
)

st.set_page_config(
    page_title="GHOST INFRASTRUCTURE",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_custom_style()

GITHUB_URL = "https://github.com/sakshimaske303-commits/GHOST_INFRASTRUCTURE"

page_header(
    "🏭", "GHOST INFRASTRUCTURE",
    "How 19th-Century Coal Geography Still Shapes Who Gets a \"15-Minute Life\" Today",
)

st.markdown(
    f"""
    <style>
        .doi-badge-link {{ text-decoration:none; }}
        .doi-badge-card {{ transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease; cursor: pointer; }}
        .doi-badge-link:hover .doi-badge-card {{ transform: translateY(-3px) scale(1.02); box-shadow: 0 10px 32px rgba(255, 242, 186, 0.6); filter: brightness(1.08); }}
    </style>
    <div style="display:flex; justify-content:center; margin: 10px 0 18px 0;">
        <a href="https://doi.org/10.5281/zenodo.21761320" target="_blank" class="doi-badge-link" style="text-decoration:none;">
            <div class="doi-badge-card" style="
                display:flex; align-items:center; gap:18px;
                background: linear-gradient(145deg, {PALETTE['bg_sidebar']}, {PALETTE['bg_main']});
                border: 2px solid {PALETTE['accent']};
                border-radius: 14px;
                padding: 16px 32px;
                box-shadow: 0 4px 20px rgba(255, 242, 186, 0.35);
            ">
                <span style="font-size:2.1rem; line-height:1;">📦</span>
                <div style="text-align:left;">
                    <div style="color:#E4D28C; font-family:'Bitter',serif; font-weight:800; font-size:1.05rem; letter-spacing:0.4px; display:flex; align-items:center; gap:8px;">
                        <span>ARCHIVED &amp; CITABLE ON ZENODO</span>
                        <span style="opacity:0.8; font-size:0.95rem;">↗</span>
                    </div>
                    <div style="color:{PALETTE['text_primary']}; font-family:'Bitter',serif; font-weight:900; font-size:1.35rem; margin-top:2px;">
                        DOI: 10.5281/zenodo.21761320
                    </div>
                </div>
            </div>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    stat_card("Study City", "Bochum", "Ruhr Valley, Germany")
with col2:
    stat_card("Historical Sites", "17", "13 mines + 4 colonies")
with col3:
    stat_card("Network Nodes", "69,393", "OSMnx street network")
with col4:
    stat_card("15-Min Coverage", "85.8%", "of the city")

st.markdown("---")

col_left, col_right = st.columns([1.1, 1])

with col_left:
    st.markdown("<h3>What Is Ghost Infrastructure?</h3>", unsafe_allow_html=True)
    lead(
        "Bochum's modern shape was never designed for people — it was built around "
        "<strong>coal mines and steel works</strong>, with railways, roads, and worker-housing "
        "colonies (Zechensiedlungen) laid out to serve 19th-century industry, not human accessibility."
    )
    lead(
        "Coal mining ended in Bochum in 1974. This project asks: more than half a century later, "
        "does that historical industrial geography still leave a measurable imprint on which "
        "neighborhoods get a genuine <strong>\"15-minute city\"</strong> — walkable access to "
        "essential services — and which don't?"
    )

with col_right:
    card(
        kicker("The Twist")
        + card_body(
            "The hypothesis was that historical industrial sites would predict present-day "
            "<span class='gi-highlight'>neglect</span>. The data said the opposite: proximity to "
            "historical coal-mine and colony locations statistically predicts "
            "<span class='gi-highlight'>better</span> 15-minute accessibility today — verified "
            "against city-center proximity and corroborated by an independent spatial-clustering "
            "(Local Moran's I) analysis.",
            large=True,
        ),
        dark=True,
    )

st.markdown("---")

st.markdown("<h3>Three Findings</h3>", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
with f1:
    card(
        kicker("Finding 1") + card_title("Reversed Effect")
        + card_body(
            "Low-accessibility zones are, on average, further from historical industrial sites — "
            "not closer, as the original hypothesis assumed (Cohen's d=0.589)."
        )
    )
with f2:
    card(
        kicker("Finding 2") + card_title("Genuinely Independent")
        + card_body(
            "Verified via logistic regression: the effect holds even after controlling for "
            "distance to the city center — it isn't just a center-proximity proxy."
        )
    )
with f3:
    card(
        kicker("Finding 3") + card_title("Spatially Clustered")
        + card_body(
            "A Local Moran's I analysis confirms low accessibility forms genuine, statistically "
            "significant cold-spot clusters — not random scatter — farther from historical sites."
        )
    )

st.markdown("---")

st.markdown("<h3>Explore the Research</h3>", unsafe_allow_html=True)

nav_items = [
    ("🏛️", "Study Design", "Bochum, methodology, why this city"),
    ("⛏️", "Historical Geography", "13 mines, 4 worker colonies"),
    ("🚶", "Accessibility Analysis", "The 15-minute network model"),
    ("📊", "The Finding", "Statistical test + confound + spatial clustering"),
    ("📈", "Explore Trends", "Live distance-threshold explorer"),
    ("🗺️", "Interactive Maps", "Live geospatial exploration"),
    ("📖", "Methodology & Data", "Sources, debugging journey, limitations"),
]

cols = st.columns(3)
for i, (icon, title, desc) in enumerate(nav_items):
    with cols[i % 3]:
        nav_card(icon, title, desc)

st.markdown("---")

st.markdown("<h3>📄 Full Project Documentation</h3>", unsafe_allow_html=True)
lead("Download the complete research paper, project journal, and development log.")

doc1, doc2, doc3 = st.columns(3)

with doc1:
    try:
        with open(os.path.join(ROOT_DIR, "GI_Research_Paper.pdf"), "rb") as f:
            st.download_button(
                label="📘 Research Paper (PDF)",
                data=f,
                file_name="GI_Research_Paper.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    except FileNotFoundError:
        st.warning("Research_Paper.pdf not found.")

with doc2:
    try:
        with open(os.path.join(ROOT_DIR, "GI_Project_Report.pdf"), "rb") as f:
            st.download_button(
                label="📗 Project Report (PDF)",
                data=f,
                file_name="GI_Project_Report.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    except FileNotFoundError:
        st.warning("Project_Journal.pdf not found.")

with doc3:
    try:
        with open(os.path.join(ROOT_DIR, "GI_Development_Log.pdf"), "rb") as f:
            st.download_button(
                label="📙 Development Log (PDF)",
                data=f,
                file_name="GI_Development_Log.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    except FileNotFoundError:
        st.warning("Development_Log.pdf not found.")

st.markdown("---")

# ============================================================
# FOOTER — NAME + GITHUB LINK
# ============================================================
card(f"""
    <div style="text-align:center;">
        {kicker("Developed by")}
        <p style="font-family:'Bitter',serif; font-weight:900; font-size:2rem; margin:0 0 6px 0;">SAKSHI D. MASKE</p>
        <p style="font-weight:700; font-size:0.95rem; margin:0 0 16px 0;">Independent Geospatial Researcher</p>
        <a href="{GITHUB_URL}" target="_blank" class="gi-pill-btn">🔗 View on GitHub</a>
    </div>
""")
