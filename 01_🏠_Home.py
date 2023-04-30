import streamlit as st
import src.utils as utl
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Self.Translate",
    page_icon=utl.favicon(),
    layout="wide",
    initial_sidebar_state="expanded"
)
html = """
<div class="container">
    <div class="static">self.</div>
        <ul class="dynamic">
            <li><span>translate</span></li>
            <li><span>traduire</span></li>
            <li><span>tradurre</span></li>
            <li><span>traducir</span></li>
        </ul>
</div>

<p>Translate text in any language, or translate sign language through the webcam </p>
<p> orrr get a beginner/intermediate/advanced lesson plan for a specified language :D </p>

"""

utl.read_markdown(html)

utl.read_css("frontend/streamlit.css")

col1, col2 = st.columns([0.4,2.2])

with col1:
    if st.button("translation"):
        switch_page("translate")

with col2:
    if st.button("about us"):
        switch_page("about")