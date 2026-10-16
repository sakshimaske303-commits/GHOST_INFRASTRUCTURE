import streamlit as st
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../dashboard
ROOT_DIR = os.path.dirname(BASE_DIR)                                     # repo root
sys.path.append(BASE_DIR)
from styles import apply_custom_style, page_header, lead, card, kicker, card_title, card_body, PALETTE

st.set_page_config(page_title="Anthropogenic Geomorphology — GHOST INFRASTRUCTURE", page_icon="⛏️", layout="wide")
apply_custom_style()

page_header(
    "⛏️", "WHAT MINING LEAVES BEHIND",
    "Background: How Mining Reshaped the Ruhr Landscape (context, not a tested result)",
)

st.markdown("---")

# ============================================================
# DIAGRAM
# ============================================================
col_a, col_b, col_c = st.columns([0.2, 5.9, 0.2])
with col_b:
    # imgg1.png is no longer displayed: it is an illustration, not a data-derived map, and its
    # map-like panels (with scale bars) could be mistaken for project results.
    # See DEFENSIBILITY_PLAN.md (item S5) for the keep/delete decision.
    pass

st.markdown("---")

# ============================================================
# SECTION 1 — MINING AS A GEOMORPHIC AGENT
# ============================================================
st.markdown("<h3>Mining Doesn't Just Extract Rock — It Reshapes the Surface</h3>", unsafe_allow_html=True)

lead("""
Bochum's 19th-century coal seams were worked from underground shafts, hollowing out extensive
subsurface voids as extraction advanced. Rock is not perfectly rigid: once support is removed
from beneath it, overlying strata gradually sag and settle to fill part of that void — a process
German mining geomorphology calls <strong>Bergsenkung</strong> (mining subsidence). Because
extraction rarely proceeds uniformly, this settling is differential, producing a shallow,
saucer-shaped depression at the surface rather than a sudden collapse — visible in the diagram
above as concentric subsidence contours spreading outward from the old shaft.
""")

st.markdown("---")

# ============================================================
# SECTION 2 — SPOIL HEAPS AS NEW LANDFORMS
# ============================================================
st.markdown("<h3>The Waste Rock Becomes a New Landform</h3>", unsafe_allow_html=True)

lead("""
Everything brought up from underground that isn't coal — waste rock, spoil — has to go
somewhere, and 19th-century practice was simply to pile it at the surface, building
<strong>Halde</strong> (spoil heaps): entirely artificial hills, sometimes tens of metres tall,
now numerous enough across the Ruhr Valley that many have been reclaimed as parks and viewpoints.
This is <strong>anthropogenic geomorphology</strong> in its most literal form — human industrial
activity manufacturing genuinely new topographic relief, not merely modifying existing terrain.
Unlike the mines themselves, these landforms don't disappear when extraction ends; they persist
in the landscape for as long as any natural hill would.
""")

st.markdown("---")

# ============================================================
# SECTION 3 — TIE TO THE PROJECT'S REVERSED FINDING
# ============================================================
st.markdown("<h3>A Possible Mechanism (Untested Hypothesis)</h3>", unsafe_allow_html=True)

card(
    kicker("Connecting the Theory to the Finding")
    + card_body(
        "Subsidence basins and spoil heaps were never just geological curiosities — mining "
        "companies built rail lines and roads specifically to reach shafts and move coal, and "
        "workers' colonies (Zechensiedlungen) were built beside them. That transport network and "
        "settlement pattern is the leading hypothesized <strong>legacy geomorphology</strong> behind "
        "present-day Bochum's road grid, though direct digitization of the historical rail and road "
        "network — needed to test transportation connectivity independently of proximity to mines "
        "and colonies — is still future work. This mechanism has <strong>not</strong> been tested in "
        "this project: it is one possible explanation for the statistical association reported on "
        "The Finding page, and that association may also reflect general urban form rather than "
        "anything specific to mining.",
        large=True,
    ),
    dark=True,
)

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — The Landform Behind the Legacy</p>",
    unsafe_allow_html=True,
)
