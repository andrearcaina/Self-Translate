import openai
import cohere
from api import OPENAI_KEY, COHERE_KEY

openai.api_key = OPENAI_KEY

cohere_client = cohere.Client(COHERE_KEY)

def translate(text, target, choice="translate"):
    response = cohere_client.detect_language(texts=[text])
    lang = response.results[0]
    if lang != target:
        if choice == "translate":
            prompt = f"Use google translate and output this text: '{text}' from {lang} to {target}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        text = response.choices[0].text.strip()
    return text

while True:
    query = input("User query: ")
    if query == "e":
        break
    language = input("User language: ")
    print(translate(query, language))