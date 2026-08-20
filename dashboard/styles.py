import streamlit as st

PALETTE = {
    "bg_main": "#0F3C65",
    "bg_card": "#FFF2BA",
    "bg_sidebar": "#092542",
    "text_primary": "#FFFFFF",
    "text_muted": "#C7D3DE",
    "accent": "#FFF2BA",
    # kept for backward compatibility with any older references
    "accent_rust": "#FFF2BA",
    "accent_steel": "#FFF2BA",
}


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
            border-right: 1px solid rgba(255, 242, 186, 0.2);
        }

        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span {
            color: #FFFFFF !important;
            font-weight: 600;
        }

        section[data-testid="stSidebar"] a {
            border-radius: 8px !important;
            padding: 8px 14px !important;
            transition: all 0.2s ease;
        }
        section[data-testid="stSidebar"] a:hover {
            background: rgba(255, 242, 186, 0.12) !important;
            border-left: 3px solid #FFF2BA;
        }
        section[data-testid="stSidebar"] a[aria-current="page"] {
            background: rgba(228, 210, 140, 0.18) !important;
            border-left: 3px solid #E4D28C;
            font-weight: 700 !important;
        }

        /* ============ Headings — one accent color, one scale ============ */
        h1 {
            font-family: 'Bitter', serif !important;
            color: #FFF2BA !important;
            font-weight: 900 !important;
            font-size: 2.75rem !important;
            text-align: center;
            text-shadow: 0 0 30px rgba(255, 242, 186, 0.22);
            margin-bottom: 0.4rem !important;
        }

        h2 {
            font-family: 'Bitter', serif;
            color: #FFF2BA !important;
            font-weight: 800 !important;
            font-size: 1.7rem !important;
        }

        h3 {
            font-family: 'Bitter', serif;
            color: #E4D28C !important;
            font-weight: 800 !important;
            font-size: 1.35rem !important;
            margin: 1.6rem 0 1rem 0 !important;
        }

        /* Page subtitle directly under the H1 — not a section header */
        .gi-subtitle {
            text-align: center;
            color: #FFFFFF;
            font-family: 'Bitter', serif;
            font-weight: 700;
            font-size: 1.25rem;
            line-height: 1.5;
            max-width: 900px;
            margin: 0 auto 1.4rem auto;
        }

        /* Lead / body paragraphs directly on the dark background */
        .gi-lead {
            color: #FFFFFF;
            font-weight: 700;
            font-size: 1rem;
            line-height: 1.75;
            margin: 0 0 0.5rem 0;
        }

        /* Text only on dark background (generic markdown fallback) */
        .stMarkdown p,
        .stMarkdown li {
            color: #FFFFFF;
            font-weight: 700;
            font-size: 1rem;
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
            background-color: rgba(255, 242, 186, 0.35);
            margin: 1.8rem 0;
        }

        .caption-text {
            color: #C7D3DE;
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 0.5px;
        }

        /* ============ Unified card system ============
        One card, one type scale, used identically on every page.
        Plain divs (not iframes) so height always matches real content —
        no more manually-guessed pixel heights or clipped/empty boxes. */

        .gi-card, .gi-card-dark {
            border-radius: 12px;
            padding: 22px 24px;
            box-sizing: border-box;
            height: 100%;
            margin-bottom: 20px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18);
        }
        .gi-card {
            background: #FFF2BA;
            border: 2.5px solid #0F3C65;
        }
        .gi-card * {
            color: #081D33 !important;
        }
        .gi-card-dark {
            background: rgba(9, 37, 66, 0.55);
            border: 1.5px solid rgba(255, 242, 186, 0.45);
        }
        .gi-card-dark * {
            color: #FFFFFF !important;
        }
        .gi-card-dark strong, .gi-card-dark b {
            color: #FFF2BA !important;
        }
        .gi-card-dark .gi-kicker {
            color: #FFF2BA !important;
        }

        .gi-kicker {
            font-weight: 800;
            font-size: 0.72rem;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: #1F3B54 !important;
            margin: 0 0 10px 0;
        }
        .gi-stat {
            font-family: 'Bitter', serif;
            font-weight: 900;
            font-size: 1.85rem;
            margin: 0 0 4px 0;
        }
        .gi-card-title {
            font-weight: 900;
            font-size: 1.02rem;
            margin: 0 0 8px 0;
        }
        .gi-card-icon {
            font-size: 1.6rem;
            margin: 0 0 8px 0;
        }
        .gi-card-body {
            font-weight: 700;
            font-size: 0.92rem;
            line-height: 1.65;
            margin: 0;
        }
        .gi-card-body-lg {
            font-weight: 800;
            font-size: 1.02rem;
            line-height: 1.8;
            margin: 0;
        }
        .gi-subtext {
            font-weight: 700;
            font-size: 0.82rem;
            margin: 6px 0 0 0;
            opacity: 0.85;
        }
        .gi-highlight {
            background-color: #FFF2BA;
            color: #081D33 !important;
            padding: 0 5px;
            border-radius: 3px;
        }

        /* Dark pill button (e.g. "View on GitHub") sitting inside a
        light .gi-card — needs to win over the card's `.gi-card * { color }`
        rule, which otherwise forces every descendant to navy text,
        making yellow-on-black button text unreadable. Two classes beats
        one, so this wins regardless of source order. */
        .gi-card .gi-pill-btn, .gi-card-dark .gi-pill-btn {
            display: inline-block;
            background-color: #111111 !important;
            color: #FFF2BA !important;
            font-weight: 800;
            font-size: 0.9rem;
            padding: 10px 24px;
            border-radius: 6px;
            text-decoration: none;
        }

        /* Equal-height cards across a row: Streamlit's column wrapper is
        already a flex child, we just need it (and its inner block) to
        stretch to the row's full height. */
        div[data-testid="stHorizontalBlock"] {
            align-items: stretch;
            gap: 1.2rem;
        }
        div[data-testid="column"] {
            display: flex;
            flex-direction: column;
        }
        div[data-testid="column"] > div {
            width: 100%;
        }

        /* Metric cards (native st.metric) kept visually matched to gi-card */
        div[data-testid="stMetric"] {
            background-color: #FFF2BA;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18);
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


# ============================================================
# Shared page-building blocks — every page uses these instead
# of hand-rolling its own HTML/CSS, so the look-and-feel (font
# sizes, colors, spacing) is identical across all pages.
# ============================================================

def page_header(icon, title, subtitle=None):
    """H1 page title + optional centered subtitle line."""
    st.markdown(f"<h1>{icon} {title}</h1>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<p class='gi-subtitle'>{subtitle}</p>", unsafe_allow_html=True)


def lead(text):
    """A body paragraph directly on the dark page background."""
    st.markdown(f"<p class='gi-lead'>{text}</p>", unsafe_allow_html=True)


def footer_caption(text):
    st.markdown(f"<p class='caption-text' style='text-align:center;'>{text}</p>", unsafe_allow_html=True)


def card(inner_html, dark=False):
    """Generic card wrapper. Build inner_html from the snippet
    helpers below (kicker/stat/card_title/card_body/subtext)."""
    css_class = "gi-card-dark" if dark else "gi-card"
    st.markdown(f'<div class="{css_class}">{inner_html}</div>', unsafe_allow_html=True)


def kicker(text):
    return f'<p class="gi-kicker">{text}</p>'


def stat(text):
    return f'<p class="gi-stat">{text}</p>'


def card_title(text):
    return f'<p class="gi-card-title">{text}</p>'


def card_icon(icon):
    return f'<p class="gi-card-icon">{icon}</p>'


def card_body(text, large=False):
    css_class = "gi-card-body-lg" if large else "gi-card-body"
    return f'<p class="{css_class}">{text}</p>'


def subtext(text):
    return f'<p class="gi-subtext">{text}</p>'


def stat_card(label, value, sub=None):
    """A single kicker + big number + optional subtext card."""
    inner = kicker(label) + stat(value)
    if sub:
        inner += subtext(sub)
    card(inner)


def nav_card(title, desc):
    card(card_title(title) + card_body(desc))
