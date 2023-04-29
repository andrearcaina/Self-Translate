import streamlit as st
from googletrans import LANGUAGES
from src.translate import translate_lang

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