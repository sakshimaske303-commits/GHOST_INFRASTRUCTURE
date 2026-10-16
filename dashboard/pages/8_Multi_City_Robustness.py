import json
import os
import sys

import streamlit as st

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, page_header, footer_caption, card, kicker, card_body

apply_custom_style()

page_header("🧪", "ROBUSTNESS: BOTH CITIES & SETTLEMENT AGE", "Every Check, Both Cities, One Fixed Decision Rule")


def load(name):
    with open(os.path.join(PROJECT_ROOT, "outputs", "robustness", name), encoding="utf-8") as f:
        return json.load(f)


rob, pop, age = load("robustness_results.json"), load("population_results.json"), load("settlement_age_results.json")


def pct(x):
    return f"{100 * x:.1f}%"


st.markdown("---")
card(card_body(
    "Decision rule, fixed before the population and settlement-age analyses were run: the industrial-legacy "
    "claim is accepted for a city only if the real sites beat at least 95% of random site sets for both service "
    "definitions <strong>and</strong> for residents. Otherwise the result is reported as explained by general "
    "urban form. Essen, a second Ruhr city about 15 km west of Bochum, is tested with the identical design.",
    large=True,
))

st.markdown("<h3>Share of random site sets that reach the real effect</h3>", unsafe_allow_html=True)
rows = []
for city in ("bochum", "essen"):
    r, p = rob[city], pop[city]
    rows.append({
        "City": city.capitalize(),
        "Street nodes, point services": pct(r["A_null_model"]["share_null_d_ge_observed"]),
        "Street nodes, all services": pct(r["C_service_definition"]["all_features"]["share_null_d_ge_observed"]),
        "Residents, point services": pct(p["points_only"]["share_null_d_ge_observed"]),
        "Residents, all services": pct(p["all_services"]["share_null_d_ge_observed"]),
    })
st.table(rows)
st.caption("Below 5% would mean the real sites beat 95% of random sets. Only one cell (Bochum, street nodes, "
           "all services) does, and it does not hold for residents. Result: explained by general urban form.")

st.markdown("---")
st.markdown("<h3>Where the gaps actually are: settlement age (GHSL, satellite-derived)</h3>", unsafe_allow_html=True)
img = os.path.join(PROJECT_ROOT, "outputs", "robustness", "settlement_age.png")
if os.path.exists(img):
    st.image(img, use_container_width=True)
card(card_body(
    "Using the GHSL built-up surface for 1975 and 2020 (derived from Landsat and Sentinel-2), each populated "
    "100 m cell is classed as built up before or after 1975. In both cities and under both service "
    f"definitions, residents of post-1975 areas (Bochum {age['bochum']['pct_residents_in_post1975_cells']:.1f}%, "
    f"Essen {age['essen']['pct_residents_in_post1975_cells']:.1f}% of residents) are two to eight times more "
    "likely to lack 15-minute access.",
    large=True,
))

st.markdown("---")
st.markdown("<h3>Other checks</h3>", unsafe_allow_html=True)
b, e = rob["bochum"]["B_urban_form"], rob["essen"]["B_urban_form"]
card(card_body(
    f"<strong>Urban-form controls:</strong> adding distance to the city boundary and local street density, random "
    f"site sets match the real coefficient {pct(b['share_null_coef_full_le_observed'])} (Bochum) and "
    f"{pct(e['share_null_coef_full_le_observed'])} (Essen) of the time.<br>"
    f"<strong>2 km grid bootstrap:</strong> the raw distance difference is [{b['grid_bootstrap_ci95_m'][0]:,.0f}, "
    f"{b['grid_bootstrap_ci95_m'][1]:,.0f}] m in Bochum and [{e['grid_bootstrap_ci95_m'][0]:,.0f}, "
    f"{e['grid_bootstrap_ci95_m'][1]:,.0f}] m in Essen: real as a description, not specific to mining.<br>"
    f"<strong>Leave one site out:</strong> Essen's effect ranges from d = {e['leave_one_site_out_d_min']:.3f} to "
    f"{e['leave_one_site_out_d_max']:.3f}, so one site drives most of it."
))
img = os.path.join(PROJECT_ROOT, "outputs", "plots", "threshold_sensitivity_comparison.png")
if os.path.exists(img):
    with st.expander("Version 1 check: 10 / 15 / 20-minute thresholds (naive comparison only)"):
        st.image(img, use_container_width=True)
        st.caption("The naive pattern holds at all three thresholds, but the null model above shows it is not "
                   "specific to mining sites.")

st.markdown("---")
card(
    kicker("Bottom line")
    + card_body(
        "Neither Bochum nor Essen supports the industrial-legacy claim once random locations and residents are "
        "taken into account. Walking-access gaps are small and concentrated in post-1975 development at the "
        "city edge.",
        large=True,
    ),
    dark=True,
)
st.markdown("---")
footer_caption("GHOST INFRASTRUCTURE v2.0 — numbers read from outputs/robustness/*.json")
