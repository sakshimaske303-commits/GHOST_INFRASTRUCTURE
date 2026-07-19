import os
import re

FILES = [
    "dashboard/app.py",
    "dashboard/pages/1_Study_Design.py",
    "dashboard/pages/2_Historical_Geography.py",
    "dashboard/pages/3_Accessibility_Analysis.py",
    "dashboard/pages/4_The_Finding.py",
    "dashboard/pages/6_Interactive_Maps.py",
    "dashboard/pages/8_Methodology_Data.py",
]

OLD_PATTERN = re.compile(
    r'def render_card\(content_html, height=\d+\):\s*\n'
    r'\s*components\.html\(f"""\s*\n'
    r'\s*<div style="background: #B4D5D6; border-radius: 10px; padding: 24px;\s*\n'
    r'\s*font-family: \'Inter\', sans-serif; box-sizing: border-box; height: \{height-48\}px;">\s*\n'
    r'\s*\{content_html\}\s*\n'
    r'\s*</div>\s*\n'
    r'\s*""", height=height\)'
)

NEW_CODE = '''def render_card(content_html, height=None):
    st.markdown(f"""
        <div style="background: #B4D5D6; border-radius: 10px; padding: 24px;
                    font-family: 'Inter', sans-serif; box-sizing: border-box; margin-bottom: 16px;">
            {content_html}
        </div>
    """, unsafe_allow_html=True)'''

for filepath in FILES:
    if not os.path.exists(filepath):
        print(f"NOT FOUND: {filepath}")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content, count = OLD_PATTERN.subn(NEW_CODE, content)

    if count > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed: {filepath}")
    else:
        print(f"Pattern not matched (skipped): {filepath}")

print("\nDone.")