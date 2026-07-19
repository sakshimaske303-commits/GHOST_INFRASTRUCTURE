import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, PALETTE

apply_custom_style()


def render_card(content_html):
    st.markdown(f"""
        <div style="background: #B4D5D6; border-radius: 10px; padding: 24px; margin-bottom: 16px;">
            {content_html}
        </div>
    """, unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;'>📊 THE FINDING</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF; font-size: 1.5rem;'>"
    "A Reversed Effect, Verified Against Its Most Obvious Confound</h3>",
    unsafe_allow_html=True,
)
st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Distance to Historical Sites: High vs. Low Accessibility</h3>", unsafe_allow_html=True)

image_path = os.path.join(PROJECT_ROOT, "outputs", "plots", "distance_comparison_boxplot.png")
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning("Boxplot image not found.")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.85rem; text-transform:uppercase; margin:0 0 12px 0;">Low-Accessibility Nodes</p>
        <p style="color:#111111; font-weight:900; font-size:2rem; margin:0 0 8px 0;">1,984 m</p>
        <p style="color:#333333; font-weight:600; font-size:0.95rem; margin:0;">
            Average distance to nearest historical industrial site (n=9,858)
        </p>
    """)
with col2:
    render_card("""
        <p style="color:#111111; font-weight:800; font-size:0.85rem; text-transform:uppercase; margin:0 0 12px 0;">High-Accessibility Nodes</p>
        <p style="color:#111111; font-weight:900; font-size:2rem; margin:0 0 8px 0;">1,450 m</p>
        <p style="color:#333333; font-weight:600; font-size:0.95rem; margin:0;">
            Average distance to nearest historical industrial site (n=59,535)
        </p>
    """)

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Statistical Confirmation</h3>", unsafe_allow_html=True)

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1.15rem; line-height:1.8; margin:0;">
        A Welch's t-test comparing the two groups produced <strong>t=42.887, p&lt;0.00001</strong> — 
        a highly significant relationship, but in the opposite direction to the original hypothesis. 
        Proximity to historical industrial sites predicts <strong>better</strong> present-day 
        accessibility, not worse.
    </p>
""")

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Checking the Obvious Confound: City Center</h3>", unsafe_allow_html=True)

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1.05rem; line-height:1.8; margin:0 0 16px 0;">
        Before accepting this result, the most obvious alternative explanation was tested directly: 
        historical sites might simply cluster near the city center, which independently predicts 
        better accessibility regardless of any genuine historical effect.
    </p>
    <p style="color:#111111; font-weight:800; font-size:1.05rem; line-height:1.8; margin:0;">
        Correlation between distance-to-historical-site and distance-to-city-center: 
        <strong>r = 0.063</strong> — genuinely independent variables, not proxies for one another.
        A logistic regression confirms the historical-site effect remains significant 
        (coefficient = -0.0005, p &lt; 0.001) even after controlling for city-center distance.
    </p>
""")

st.markdown("---")

st.markdown("<h3 style='color:#7FB8BE;'>Interpretation</h3>", unsafe_allow_html=True)

render_card("""
    <p style="color:#111111; font-weight:700; font-size:1.1rem; line-height:1.85; margin:0;">
        19th-century industrial cores were built dense, by necessity — around the mines and 
        colonies where workers actually lived. That density appears to persist as present-day 
        street connectivity and service coverage, decades after the mines closed. This is a 
        <strong>"path dependency of centrality"</strong> rather than the originally hypothesized 
        "path dependency of neglect." Genuine accessibility gaps concentrate further from, 
        not closer to, the historical industrial core.
    </p>
""")

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — Welch's t-test + logistic regression confound verification</p>",
    unsafe_allow_html=True,
)