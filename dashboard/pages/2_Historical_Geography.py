import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, footer_caption, card, stat_card, card_body

apply_custom_style()

page_header("⛏️", "HISTORICAL GEOGRAPHY", "13 Coal Mines, 4 Worker Colonies — Digitized From Archives")
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    stat_card("Earliest Mine", "1829", "Vereinigte Engelsburg")
with col2:
    stat_card("Last Mine Closed", "1974", "Holland Colliery")
with col3:
    stat_card("Data Source", "Mindat.org", "Compiled record by record")

st.markdown("---")

st.markdown("<h3>The Industrial Skeleton of Bochum</h3>", unsafe_allow_html=True)

image_path = os.path.join(PROJECT_ROOT, "outputs", "plots", "historical_geography.png")
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning("Historical geography map not found.")

card(card_body(
    "Mines (orange triangles) and worker-housing colonies — Zechensiedlungen (cyan squares) — "
    "were compiled independently and kept as two structurally distinct layers by design: a mine "
    "is an extraction site, a colony is residential housing. A proposed steelworker colony "
    "(Stahlhausen) was explicitly excluded during review since it belonged to a different "
    "industry (steel, not coal)."
))

st.markdown("---")

st.markdown("<h3>The Full Ghost Infrastructure Overlay</h3>", unsafe_allow_html=True)

image_path2 = os.path.join(PROJECT_ROOT, "outputs", "plots", "ghost_infrastructure_overlay.png")
if os.path.exists(image_path2):
    st.image(image_path2, use_container_width=True)
else:
    st.warning("Overlay map not found.")

card(card_body(
    "The same 17 historical sites overlaid on 69,393 present-day street-network nodes, colored "
    "by 15-minute accessibility status. Green dots dominate the interior; red dots — genuine "
    "accessibility gaps — concentrate toward the periphery, further from the historical "
    "industrial core."
))

st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE — Sources: Mindat.org, German heritage archives")
