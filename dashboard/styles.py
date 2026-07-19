import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bitter:wght@500;600;700;800;900&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background-color: #2E3A61;
        }

        section[data-testid="stSidebar"] {
            background-color: #253250;
        }

        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span {
            color: #FFFFFF !important;
            font-weight: 600;
        }

        h1 {
            font-family: 'Bitter', serif !important;
            color: #FFFFFF !important;
            font-weight: 900 !important;
            font-size: 3.4rem !important;
        }

        h2 {
            font-family: 'Bitter', serif;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            border-left: 4px solid #7FB8BE;
            padding-left: 14px;
            font-size: 1.8rem !important;
        }

        h3 {
            font-family: 'Bitter', serif;
            color: #7FB8BE !important;
            font-weight: 700 !important;
        }

        /* Text only on dark background */
        .stMarkdown p,
        .stMarkdown li {
            color: #FFFFFF;
            font-weight: 600;
            font-size: 1.1rem;
            line-height: 1.7;
        }

        strong, b {
            color: #7FB8BE;
            font-weight: 800;
        }

        .stButton>button {
            background-color: #7FB8BE;
            color: #253250;
            border-radius: 6px;
            border: none;
            font-weight: 700;
        }

        hr {
            border: none;
            height: 1px;
            background-color: #7FB8BE;
            margin: 1.6rem 0;
        }

        .caption-text {
            color: #D9D9D9;
            font-size: 0.9rem;
            font-weight: 600;
        }

        /* Force black text inside blueprint cards */
        .blueprint-card {
            background: #B4D5D6;
            border-radius: 10px;
            padding: 20px;
        }
        .blueprint-card * {
            color: #111111 !important;
            font-weight: 700 !important;
        }
        .blueprint-card h1,
        .blueprint-card h2,
        .blueprint-card h3,
        .blueprint-card h4,
        .blueprint-card h5,
        .blueprint-card p,
        .blueprint-card span,
        .blueprint-card strong,
        .blueprint-card b {
            color: #111111 !important;
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
            background-color: #B4D5D6;
            border-radius: 10px;
            padding: 20px;
        }
        div[data-testid="stMetric"] * {
            color: #111111 !important;
            font-weight: 800 !important;
        }
        </style>
    """, unsafe_allow_html=True)


PALETTE = {
    "bg_main": "#2E3A61",
    "bg_card": "#B4D5D6",
    "bg_sidebar": "#253250",
    "text_primary": "#FFFFFF",
    "text_muted": "#D9D9D9",
    "accent_rust": "#7FB8BE",
    "accent_steel": "#7FB8BE",
}