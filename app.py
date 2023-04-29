import streamlit as st
from googletrans import LANGUAGES
from src.translate import translate_lang

st.set_page_config(
    page_title="Translating App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.markdown(
    f'<link rel="stylesheet" href="/styles.css">',
    unsafe_allow_html=True,
)

languages = {v: k for k, v in LANGUAGES.items()}

lang_names = sorted(list(languages.keys()))

target_lang = st.selectbox("Select target language", options=lang_names)

label = 'Enter text'

user_input = ""
user_input = st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="enter text", disabled=False, label_visibility="visible")

if not user_input == "":
    query = user_input
    language = languages.get(target_lang)
    response = translate_lang(query, language)
    st.text_input(label=f"Output in {target_lang}", value=f"{response}", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="", disabled=True, label_visibility="visible")