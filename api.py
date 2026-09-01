import requests

url = "http://127.0.0.1:1234/v1/chat/completions"

SYSTEM_PROMPT = """
Você é um assistente que responde APENAS em texto simples (plain text).
Não use markdown.
Não use símbolos como #, *, _, -, >, listas ou formatação.
Não use emojis.
Responda apenas com frases normais, como fala natural.
"""

def request(question: str):
    payload = {
        "model": "local-model",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]