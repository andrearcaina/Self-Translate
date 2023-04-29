import streamlit as st
import src.utils as utl

st.set_page_config(
    page_title="Self.Translate",
    page_icon="🦌",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
html = """
<div class="container">
    <div class="static">self.</div>
        <ul class="dynamic">
            <li><span>translate</span></li>
            <li><span>traduire</span></li>
            <li><span>tradurre</span></li>
            <li><span>txhais lus</span></li>
        </ul>
</div>
"""

utl.read_markdown(html)

utl.read_css("frontend/streamlit.css")