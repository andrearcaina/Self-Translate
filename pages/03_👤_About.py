import streamlit as st
from src.utils import favicon
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Self.Translate",
    page_icon=favicon(),
    layout="wide",
    initial_sidebar_state="expanded",
)

col1, col2, col3, col4= st.columns([3,1,2,1])

col1.subheader("< about />")

col1.markdown(f'<h2> self.<span style="background-color:#002b36;color:#6dac32;font-size:46px;border-radius:100%;">{"translate"}</span> is... </h2>', unsafe_allow_html=True)

col1.write('<p style="text-align:justify;"> a revolutionary translation application that can be utilized by users worldwide! This cutting-edge app has the ability to translate text from a vast collection of over 100 languages, while also providing support for sign language. With the incorporation of self.translate, learning, traveling, and socializing has never been easier. </p>', unsafe_allow_html=True)
col1.write("\nIncoming mobile version in the future!")


with st.sidebar:
    st.subheader("\n\n< collaborators />")
    st.write("🔥 [Andre Arcaina](https://www.linkedin.com/in/andre-arcaina/)")
    st.write("☁️ [Dominic Chen](https://www.linkedin.com/in/dominicchen1/)")
    st.write("💧 [Justin Tran](https://www.linkedin.com/in/justin-tran-028734254/)")
    st.write("🌍 [Tao Wang](https://www.linkedin.com/in/tao-wang-3b415724b/)")

col3.write("")
col3.write("")
col3.image(favicon())

if col4.button("Home"):
    switch_page("Home")