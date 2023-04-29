import streamlit as st
import sqlite3 as sql
from googletrans import LANGUAGES
from src.translate import translate_lang
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

    label = 'Enter text'

    user_input = ""
    user_input = st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="enter text", disabled=False, label_visibility="visible")

    if not user_input == "":
        query = user_input
        language = languages.get(target_lang)
        response = translate_lang(query, language)
        st.text_input(label=f"Output in {target_lang}", value=f"{response}", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="", disabled=True, label_visibility="visible")
        return query, response
    return None, None

page = st.sidebar.selectbox(label='Options', options=('Regular', 'Sign'))


col1, col2 = st.columns([4,2.2])

with col1:
    if page == 'Regular':
        query, response = regular_translate()
        database, cursor = connect_database()
        if st.sidebar.button("Clear Translation Log"):
            clear_table()

    elif page == "Sign":
        st.write("Sign Language")

with col2:
    # this needs to change so that the translation log refreshes when the entire web app refreshes
    # for now it only outputs the translated output when the user inputs something
    # this is because we are clearning the table everytime
    if page == 'Regular':
        st.write("Translation Log:")
        st.write("Input | Output")
        clear_table()
        cursor.execute("INSERT INTO translations VALUES (?, ?)", (query, response))
        database.commit()
        cursor.execute("SELECT * FROM translations")
        for row in cursor.fetchall():
            st.write(f"{row[0]} -> {row[1]}")
        database.close()

