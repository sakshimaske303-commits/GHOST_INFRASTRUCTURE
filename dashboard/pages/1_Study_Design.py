import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, lead, footer_caption, card, kicker, card_title, card_body

apply_custom_style()

page_header("🏛️", "STUDY DESIGN", "Why Bochum, Why 15-Minute Accessibility, Why This Question")
st.markdown("---")

lead(
    "The concept of \"path dependency\" — that historical spatial decisions continue to shape "
    "present-day urban outcomes long after their original rationale has disappeared — is a "
    "well-established idea in economic geography. Yet it is rarely tested with direct, "
    "quantitative spatial evidence. This project makes it measurable, directly overlaying "
    "digitized historical industrial geography against a quantitative, network-based measure "
    "of present-day urban accessibility: the \"15-minute city\" framework."
)

st.markdown("---")

st.markdown("<h3>Why Bochum</h3>", unsafe_allow_html=True)

card(card_body(
    "Bochum was a small agricultural town until iron, coal, and steel industries developed "
    "mid-19th century, becoming a defining Ruhr Valley industrial city through the 1950s. "
    "The last coal mine in Bochum (Zeche Holland) closed in 1974. Bochum is also directly relevant "
    "to this research program's institutional context — home to Ruhr University Bochum.",
    large=True,
))

st.markdown("---")

st.markdown("<h3>The Research Question</h3>", unsafe_allow_html=True)

card(card_body(
    "Does the historical geography of Ruhr Valley coal and steel industry infrastructure — "
    "mine locations and worker-housing colonies — continue to structurally predict which "
    "present-day neighborhoods fall inside or outside a \"15-minute\" accessibility standard, "
    "decades after industrial decline? (Industrial-era transportation networks were part of the "
    "original conceptual scope; see Future Work on the Methodology & Data page.)",
    large=True,
))

st.markdown("---")

st.markdown("<h3>Study Area</h3>", unsafe_allow_html=True)

study_area_path = os.path.join(PROJECT_ROOT, "outputs", "plots", "study_area_bochum.png")
if os.path.exists(study_area_path):
    st.image(study_area_path, use_container_width=True)

st.markdown("---")

st.markdown("<h3>Three-Step Methodology</h3>", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)
with m1:
    card(
        kicker("Step 1") + card_title("Historical Digitization")
        + card_body(
            "13 coal mines and 4 worker colonies compiled and georeferenced from Mindat.org and "
            "German heritage archives."
        )
    )
with m2:
    card(
        kicker("Step 2") + card_title("Network Accessibility")
        + card_body(
            "69,393-node pedestrian street network built via OSMnx, tested against 786 essential "
            "services using true network-distance isochrones."
        )
    )
with m3:
    card(
        kicker("Step 3") + card_title("Statistical Testing")
        + card_body(
            "Welch's t-test, logistic regression confound verification, and an independent Local "
            "Moran's I spatial-clustering analysis."
        )
    )

st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE — Bochum, Ruhr Valley, Germany")
