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
    <div style="display:flex; justify-content:center; flex-wrap:wrap; gap:16px; margin: 10px 0 18px 0;">
        <a href="https://eartharxiv.org/repository/view/14809/" target="_blank" class="doi-badge-link" style="text-decoration:none;">
            <div class="doi-badge-card" style="
                display:flex; align-items:center; gap:18px;
                background: linear-gradient(145deg, {PALETTE['bg_sidebar']}, {PALETTE['bg_main']});
                border: 2px solid {PALETTE['accent']};
                border-radius: 14px;
                padding: 16px 32px;
                box-shadow: 0 4px 20px rgba(255, 242, 186, 0.35);
            ">
                <div style="text-align:left;">
                    <div style="color:#E4D28C; font-family:'Bitter',serif; font-weight:800; font-size:1.05rem; letter-spacing:0.4px; display:flex; align-items:center; gap:8px;">
                        <span>PREPRINT ON EARTHARXIV</span>
                        <span style="opacity:0.8; font-size:0.95rem;">↗</span>
                    </div>
                    <div style="color:{PALETTE['text_primary']}; font-family:'Bitter',serif; font-weight:900; font-size:1.35rem; margin-top:2px;">
                        Read the preprint
                    </div>
                </div>
            </div>
        </a>
        <a href="https://doi.org/10.5281/zenodo.21761320" target="_blank" class="doi-badge-link" style="text-decoration:none;">
            <div class="doi-badge-card" style="
                display:flex; align-items:center; gap:18px;
                background: linear-gradient(145deg, {PALETTE['bg_sidebar']}, {PALETTE['bg_main']});
                border: 2px solid {PALETTE['accent']};
                border-radius: 14px;
                padding: 16px 32px;
                box-shadow: 0 4px 20px rgba(255, 242, 186, 0.35);
            ">
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
    stat_card("15-Min Coverage", "85.8%", "of network nodes")

st.markdown("---")

card(
    kicker("Why This Matters")
    + card_body(
        "It is often assumed that a city's industrial past decides which neighbourhoods are well served "
        "today. This project tested that idea for walking access in two Ruhr cities, Bochum and Essen, and "
        "tested it properly: against random locations, for residents rather than street nodes, and with "
        "satellite-derived settlement age. The apparent 'legacy' effect turned out to be general urban form. "
        "The real access gaps are small and sit in areas built up after 1975, which is where planning "
        "attention belongs.",
        large=True,
    ),
    dark=True,
)

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
            "A first comparison suggested that places near old mines have "
            "<span class='gi-highlight'>better</span> access today. But 1,000 random sets of locations "
            "in the same city do just as well, and the effect disappears when residents are counted. "
            "Version 1 of this project reported the first result; version 2 tests it and reports what "
            "actually holds.",
            large=True,
        ),
        dark=True,
    )

st.markdown("---")

st.markdown("<h3>Three Findings</h3>", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
with f1:
    card(
        kicker("Finding 1") + card_title("No Mining-Specific Legacy")
        + card_body(
            "Real mine and colony sites are not distinguishable from random built-up locations once "
            "access is counted for residents, in either city."
        )
    )
with f2:
    card(
        kicker("Finding 2") + card_title("Gaps Are Small for People")
        + card_body(
            "Counting all mapped services, about 2% of Bochum's and under 1% of Essen's residents "
            "lack 15-minute walking access (Zensus 2022)."
        )
    )
with f3:
    card(
        kicker("Finding 3") + card_title("Newer Areas Lag Behind")
        + card_body(
            "Residents of areas first built up after 1975 (GHSL satellite data) are 2–8 times more "
            "likely to lack access."
        )
    )

st.markdown("---")

st.markdown("<h3>Explore the Research</h3>", unsafe_allow_html=True)

nav_items = [
    ("Study Design", "Bochum, methodology, why this city"),
    ("Theoretical Foundations", "Background: how mining reshaped the Ruhr landscape"),
    ("Historical Geography", "13 mines, 4 worker colonies"),
    ("Accessibility Analysis", "The 15-minute network model"),
    ("The Finding", "Naive comparison, null model, residents"),
    ("Explore Trends", "Live distance-threshold explorer"),
    ("Interactive Maps & Plots", "Live geospatial exploration plus the three headline charts"),
    ("Methodology & Data", "Sources, debugging journey, limitations"),
    ("Robustness: Both Cities & Settlement Age", "Essen, urban form, GHSL settlement age"),
]

cols = st.columns(3)
for i, (title, desc) in enumerate(nav_items):
    with cols[i % 3]:
        nav_card(title, desc)

st.markdown("---")

st.markdown("<h3>Full Project Documentation</h3>", unsafe_allow_html=True)
lead("The complete research paper, project journal, and development log are available to download below.")

_all_docs = [
    {"label": "Executive Summary", "filename": "GI_Executive_Summary.pdf"},
    {"label": "Research Paper", "filename": "GI_Research_Paper.pdf"},
    {"label": "Development Log", "filename": "GI_Development_Log.pdf"},
]
_existing = [d for d in _all_docs if os.path.exists(os.path.join(BASE_DIR, "static", d["filename"]))]
_missing = [d for d in _all_docs if d not in _existing]

if _existing:
    _cols = st.columns(len(_existing))
    for _col, _d in zip(_cols, _existing):
        with _col:
            with open(os.path.join(BASE_DIR, "static", _d["filename"]), "rb") as _f:
                st.download_button(
                    label=f"⬇ {_d['label']}",
                    data=_f.read(),
                    file_name=_d["filename"],
                    mime="application/pdf",
                    use_container_width=True,
                )
for d in _missing:
    st.warning(f"{d['filename']} not found.")

st.markdown("---")

# ============================================================
# FOOTER — NAME + GITHUB LINK
# ============================================================
card(f"""
    <div style="text-align:center;">
        {kicker("Developed by")}
        <p style="font-family:'Bitter',serif; font-weight:900; font-size:2rem; margin:0 0 6px 0;">SAKSHI D. MASKE</p>
        <p style="font-weight:700; font-size:0.95rem; margin:0 0 16px 0;">Independent Geospatial Researcher</p>
        <a href="{GITHUB_URL}" target="_blank" class="gi-pill-btn">View on GitHub</a>
    </div>
""")
