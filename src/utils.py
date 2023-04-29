import streamlit as st

def read_markdown(html):
    st.markdown(html, unsafe_allow_html=True)

def read_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

