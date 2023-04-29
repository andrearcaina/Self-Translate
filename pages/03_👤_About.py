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
col1a,col1b, col1c = col1.columns([2,5,2])
col1a.title("self.")
col1b.markdown(f'<h2 style="background-color:#002b36;color:#6dac32;font-size:46px;border-radius:100%;">{"translate"}</h2>', unsafe_allow_html=True)
col1c.title("is...")

col1.write("a revolutionary translation application that can be utilized by users worldwide! This cutting-edge app has the ability to translate text from a vast collection of over 100 languages, while also providing support for sign language. With the incorporation of self.translate, learning, traveling, and socializing has never been easier.")
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

if(col4.button("Home")):
    switch_page("Home")