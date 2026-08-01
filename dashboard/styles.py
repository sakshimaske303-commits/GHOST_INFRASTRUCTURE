import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bitter:wght@500;600;700;800;900&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* Rich midnight-blue gradient — not flat, has depth */
        .stApp {
            background: linear-gradient(135deg, #0F3C65 0%, #0A2E4F 55%, #0F3C65 100%);
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #092542 0%, #0A2E4F 100%);
            border-right: 1px solid rgba(255, 242, 186, 0.15);
        }

        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span {
            color: #FFFFFF !important;
            font-weight: 600;
        }

        h1 {
            font-family: 'Bitter', serif !important;
            color: #FFF2BA !important;
            font-weight: 900 !important;
            font-size: 3.4rem !important;
            text-shadow: 0 0 30px rgba(255, 242, 186, 0.22);
        }

        h2 {
            font-family: 'Bitter', serif;
            color: #FFF2BA !important;
            font-weight: 700 !important;
            border-left: 4px solid #FFF2BA;
            padding-left: 14px;
            font-size: 1.8rem !important;
        }

        h3 {
            font-family: 'Bitter', serif;
            color: #E4D28C !important;
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
            color: #FFF2BA;
            font-weight: 800;
        }

        .stButton>button {
            background-color: #FFF2BA;
            color: #0F3C65;
            border-radius: 6px;
            border: none;
            font-weight: 700;
        }

        hr {
            border: none;
            height: 1px;
            background-color: #FFF2BA;
            margin: 1.6rem 0;
        }

        .caption-text {
            color: #C7D3DE;
            font-size: 0.9rem;
            font-weight: 600;
        }

        /* Force midnight-blue text inside buttermilk blueprint cards */
        .blueprint-card {
            background: #FFF2BA;
            border-radius: 10px;
            padding: 20px;
        }
        .blueprint-card * {
            color: #0F3C65 !important;
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
            color: #0F3C65 !important;
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
            background-color: #FFF2BA;
            border-radius: 10px;
            padding: 20px;
        }
        div[data-testid="stMetric"] * {
            color: #0F3C65 !important;
            font-weight: 800 !important;
        }

        /* ---- Keep header visible (needed for the sidebar
        open/close button) but hide only the Deploy button ---- */
[data-testid="stHeader"] {
    background-color: #0F3C65 !important;
    height: 3rem !important;
}
[data-testid="stAppDeployButton"] {
    display: none !important;
}
[data-testid="stDecoration"] {
    display: none !important;
}
#MainMenu {
    visibility: hidden !important;
}
.block-container {
    padding-top: 1rem !important;
}

        /* ---- Sidebar collapse/expand button — safety net
        covering every naming variant Streamlit has used
        across versions, since it's invisible-by-default on
        a dark theme and hard to see on mobile otherwise ---- */
        [data-testid="collapsedControl"],
        [data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapseButton"],
        [data-testid="baseButton-header"],
        [data-testid="stHeader"] button,
        [data-testid*="ollapse" i],
        button[kind="header"] {
            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;
            z-index: 999999 !important;
        }
        [data-testid="collapsedControl"],
        [data-testid="stSidebarCollapsedControl"] {
            position: fixed !important;
            top: 12px !important;
            left: 12px !important;
            background: #092542 !important;
            border: 1.5px solid #FFF2BA !important;
            border-radius: 8px !important;
            padding: 4px !important;
        }
        [data-testid="collapsedControl"] svg,
        [data-testid="stSidebarCollapsedControl"] svg,
        [data-testid="stSidebarCollapseButton"] svg,
        [data-testid="baseButton-header"] svg,
        [data-testid="stHeader"] button svg,
        button[kind="header"] svg {
            fill: #FFF2BA !important;
            stroke: #FFF2BA !important;
            opacity: 1 !important;
        }
        </style>
    """, unsafe_allow_html=True)


PALETTE = {
    "bg_main": "#0F3C65",
    "bg_card": "#FFF2BA",
    "bg_sidebar": "#092542",
    "text_primary": "#FFFFFF",
    "text_muted": "#C7D3DE",
    "accent_rust": "#FFF2BA",
    "accent_steel": "#FFF2BA",
}