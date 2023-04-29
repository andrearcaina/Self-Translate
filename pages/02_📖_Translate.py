import streamlit as st
import sqlite3 as sql
import numpy as np
from googletrans import LANGUAGES
from src.translate import translate_lang
from src.camera import camera_recognition
from src.utils import favicon

st.set_page_config(
    page_title="Self.Translate",
    page_icon=favicon(),
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def clear_table():
    database, cursor = connect_database()
    cursor = database.cursor()
    cursor.execute("DELETE FROM translations")
    database.commit()
    database.close()

def connect_database():
    database = sql.connect("translation_log.db")
    cursor = database.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS translations
                (input, output)''')
    database.commit()

    return database, cursor

def regular_translate():
    languages = {v: k for k, v in LANGUAGES.items()}

    lang_names = sorted(list(languages.keys()))

    target_lang = st.selectbox("Select target language", options=lang_names)

    user_input = st.text_area(label=f"Input text: ", value="", max_chars=4000, disabled=False, placeholder="enter text", label_visibility="visible")

    if not user_input == "":
        query = user_input
        language = languages.get(target_lang)
        response, lang_name = translate_lang(query, language)
        st.text_area(label=f"Detected Language: {lang_name}", value=f"{query}", disabled=True, label_visibility="visible")
        st.text_area(label=f"Language Output: {target_lang}", value=f"{response}", disabled=True, label_visibility="visible")
        return query, response
    return None, None

page = st.sidebar.selectbox(label='Options', options=('Regular', 'Sign'))


col1, col2 = st.columns([4,2.2])

with col1:
    if page == 'Regular':
        query, response = regular_translate()
        if st.sidebar.button("Clear Translation Log"):
            clear_table()

    elif page == "Sign":
        st.write("Sign Language")
        camera_recognition()

with col2:
    # this needs to change so that the translation log refreshes when the entire web app refreshes
    # for now it only outputs the translated output when the user inputs something
    # this is because we are clearning the table everytime
    if page == 'Regular':
        database, cursor = connect_database()
        st.write("Translation Log:")
        st.write("Input | Output")
        clear_table()
        cursor.execute("INSERT INTO translations VALUES (?, ?)", (query, response))
        database.commit()
        cursor.execute("SELECT * FROM translations")
        for row in cursor.fetchall():
            st.write(f"{row[0]} -> {row[1]}")
        database.close()

