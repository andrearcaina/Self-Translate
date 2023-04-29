import streamlit as st
from streamlit_extras.switch_page_button import switch_page

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

col1, col2, col3, col4= st.columns([3,1,2,1])

col1.subheader("< about />")

col1.markdown(f'<h2> self.<span style="background-color:#002b36;color:#6dac32;font-size:46px;border-radius:100%;">{"translate"}</span> is... </h2>', unsafe_allow_html=True)

col1.write('<p style="text-align:justify;"> a revolutionary translation application that can be utilized by users worldwide! This cutting-edge app has the ability to translate text from a vast collection of over 100 languages, while also providing support for sign language. With the incorporation of self.translate, learning, traveling, and socializing has never been easier. </p>', unsafe_allow_html=True)
col1.write("\nMobile version incoming!")

col1.subheader("\n\n< collaborators />")
col1.write("[Andre](https://www.linkedin.com/in/andre-arcaina/)")
col1.write("[Dominic](https://www.linkedin.com/in/dominicchen1/)")
col1.write("[Tao](https://www.linkedin.com/in/tao-wang-3b415724b/)")


col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.image("./logo.png")

if col4.button("Home"):
    switch_page("Home")