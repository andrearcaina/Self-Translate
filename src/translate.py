import openai
import cohere
from api import OPENAI_KEY, COHERE_KEY
from iso639 import languages

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

# Example usage
while True:
    query = input("User query: ")
    language = input("User language: ")
    response = chatbot(query, language)
    print(f"Bot response: {response}")
