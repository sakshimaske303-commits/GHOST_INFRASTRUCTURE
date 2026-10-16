import json
import os
import sys

import streamlit as st

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, footer_caption, card, kicker, stat_card, card_body

apply_custom_style()

page_header("📊", "THE FINDING", "An Apparent Legacy Effect, Tested Against Random Locations")


def load(name):
    with open(os.path.join(PROJECT_ROOT, "outputs", "robustness", name), encoding="utf-8") as f:
        return json.load(f)


rob, pop = load("robustness_results.json"), load("population_results.json")
A, C = rob["bochum"]["A_null_model"], rob["bochum"]["C_service_definition"]
P = pop["bochum"]


def pct(x):
    return f"{100 * x:.1f}%"


st.markdown("---")
st.markdown("<h3>Step 1 — The naive comparison</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    stat_card("Nodes WITHOUT 15-min access", f"{C['points_only']['mean_dist_low_m']:,.0f} m",
              "average distance to nearest historical site")
with col2:
    stat_card("Nodes WITH 15-min access", f"{C['points_only']['mean_dist_high_m']:,.0f} m",
              "average distance to nearest historical site")
card(card_body(
    f"Street nodes that lack walking access to services lie farther from the old mines and colonies "
    f"(Cohen's d = {A['observed_cohens_d']:.3f}). Taken at face value, this looks like an industrial "
    "legacy: the old mining districts seem better served. Version 1 of this project stopped here.",
    large=True,
))

st.markdown("---")
st.markdown("<h3>Step 2 — Would random locations do the same?</h3>", unsafe_allow_html=True)
card(card_body(
    "The decisive test: draw 1,000 random sets of 17 locations from the same street network and repeat the "
    f"comparison. <strong>{pct(A['share_null_d_positive'])}</strong> of random sets show the same 'reversed' pattern, "
    f"and <strong>{pct(A['share_null_d_ge_observed'])}</strong> reach an effect at least as large as the real sites. "
    "Low-access streets sit at the low-density edge of the city, so almost any set of points inside the "
    "built-up area looks 'close to good access'.",
    large=True,
))
img = os.path.join(PROJECT_ROOT, "outputs", "robustness", "null_model.png")
if os.path.exists(img):
    st.image(img, use_container_width=True,
             caption="Cohen's d for 1,000 random site sets (bars) versus the real historical sites (line)")

st.markdown("---")
st.markdown("<h3>Step 3 — Count people, not street nodes</h3>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    stat_card("Residents without access", f"{P['points_only']['pct_residents_without_access']:.1f}%",
              "point-mapped services only")
with c2:
    stat_card("Residents without access", f"{P['all_services']['pct_residents_without_access']:.1f}%",
              "all mapped services (incl. hospitals, parks, schools)")
card(card_body(
    "Using the Zensus 2022 100 m population grid, the real sites are compared with random populated "
    "locations. Random sets reach the real effect "
    f"{pct(P['points_only']['share_null_d_ge_observed'])} (point services) and "
    f"{pct(P['all_services']['share_null_d_ge_observed'])} (all services) of the time. Neither comes close to "
    "the 95% line that was fixed in advance.",
    large=True,
))
img = os.path.join(PROJECT_ROOT, "outputs", "robustness", "null_model_population.png")
if os.path.exists(img):
    st.image(img, use_container_width=True, caption="Population-weighted null model, both cities")

st.markdown("---")
st.markdown("<h3>What this means</h3>", unsafe_allow_html=True)
card(
    kicker("Answer to the research question")
    + card_body(
        "The coal-mining sites are <strong>not</strong> associated with walking access beyond what general "
        "urban form explains. The apparent legacy signal is real as a description but not specific to mining. "
        "What does distinguish the gaps is settlement age: residents of areas built up after 1975 are much "
        "more often without access. See <strong>Robustness: Both Cities &amp; Settlement Age</strong>.",
        large=True,
    ),
    dark=True,
)

st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE v2.0 — numbers read from outputs/robustness/*.json")
