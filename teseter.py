import streamlit as st
import openai
import cohere
from api import OPENAI_KEY, COHERE_KEY

openai.api_key = OPENAI_KEY

cohere_client = cohere.Client(COHERE_KEY)

def translate(text, target):
    response = cohere_client.detect_language(texts=[text])
    lang = response.results[0]
    if lang != target:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Translate the following text from {lang} to {target}: '{text}'",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        text = response.choices[0].text.strip()
    return text

def chatbot(query, language):
    query = translate(query, "en")
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Q: {query}\nA:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    english = response.choices[0].text.strip()

    response = translate(english, language)

    return response

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

language_out = st.radio("Language", ('English','French','Chinese','Italian'))
st.write(language_out)

lang_map = {'English': 'en', 'French': 'fr', 'Chinese': 'ch', 'Italian': 'it'}

label = 'Enter text'

user_input = ""
user_input = st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="enter text", disabled=False, label_visibility="visible")

if(not user_input == ""):
    query = user_input
    language = lang_map.get(language_out)
    response = chatbot(query, language)
    st.write(f"Bot response: {response}")
