import streamlit as st
import geopandas as gpd
import plotly.graph_objects as go
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_ROOT)
from styles import apply_custom_style, PALETTE

apply_custom_style()

st.markdown("<h1 style='text-align: center;'>📈 EXPLORE TRENDS</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: #FFFFFF; font-size: 1.5rem;'>"
    "Live Distance-Threshold Explorer</h3>",
    unsafe_allow_html=True,
)
st.markdown("---")

st.markdown("""
<p style='color:#FFFFFF; font-weight:600; font-size:1.1rem; line-height:1.7;'>
The core finding used a fixed comparison between "low" and "high" accessibility nodes. Use the 
slider below to define your own distance threshold for "close to a historical site" and see 
how accessibility coverage changes on either side of that line, recalculated live from the 
underlying 69,393-node dataset.
</p>
""", unsafe_allow_html=True)

st.markdown("---")


@st.cache_data
def load_data():
    return gpd.read_file(os.path.join(PROJECT_ROOT, "data", "accessibility", "bochum_accessibility_with_distance.gpkg"))


nodes = load_data()

threshold = st.slider(
    "Distance threshold defining 'close to a historical site' (meters)",
    min_value=200, max_value=3000, value=1500, step=100
)

close_nodes = nodes[nodes["dist_to_historical_m"] <= threshold]
far_nodes = nodes[nodes["dist_to_historical_m"] > threshold]

close_pct = (close_nodes["within_15min"].sum() / len(close_nodes) * 100) if len(close_nodes) > 0 else 0
far_pct = (far_nodes["within_15min"].sum() / len(far_nodes) * 100) if len(far_nodes) > 0 else 0

fig = go.Figure()
fig.add_trace(go.Bar(
    x=[f"Within {threshold}m of Historical Site", f"Beyond {threshold}m"],
    y=[close_pct, far_pct],
    marker_color=[PALETTE["accent_rust"], PALETTE["accent_steel"]],
    text=[f"{close_pct:.1f}%", f"{far_pct:.1f}%"],
    textposition="outside",
    textfont=dict(color="#FFFFFF", size=18),
))

fig.update_layout(
    template="plotly_white",
    yaxis_title="% of Nodes Within 15-Minute Accessibility",
    yaxis=dict(range=[0, 105], tickfont=dict(color="#FFFFFF", size=13),
               title_font=dict(color="#FFFFFF", size=14)),
    xaxis=dict(tickfont=dict(color="#FFFFFF", size=14)),
    height=450,
    font=dict(family="Inter", color="#FFFFFF"),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(t=30, b=40, l=40, r=40),
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(f"""
<p style='color:#FFFFFF; font-weight:600; font-size:1rem;'>
At a {threshold}m threshold: {len(close_nodes):,} nodes are classified "close," 
{len(far_nodes):,} nodes are classified "far." The gap between the two bars visualizes the 
ghost infrastructure effect at this specific threshold.
</p>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<p class='caption-text' style='text-align:center;'>GHOST INFRASTRUCTURE — Recalculated live from 69,393 network nodes</p>",
    unsafe_allow_html=True,
)