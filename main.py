from api import request_stream
from api import request
from listen import Listen
from text_to_speech import text_to_speech

def speak_stream(question: str):
    buffer = ""

    for chunk in request_stream(question):
        print(chunk, end="", flush=True)

        buffer += chunk

        # fala a cada frase (melhor que palavra por palavra)
        if any(p in buffer for p in [".", "!", "?"]):
            text_to_speech(buffer)
            buffer = ""

    # fala resto
    if buffer.strip():
        text_to_speech(buffer)

def send_to_ai():
    text_to_speech("Pode falar chefe!")
    listen_instance = Listen()
    said = listen_instance.listen_and_transcribe()
    if said:
        speak_stream(said)

def main():
    listen_instance = Listen()
    listen_instance.listen_and_wait(send_to_ai)

main()
 