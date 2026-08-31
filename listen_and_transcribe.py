import speech_recognition as sr


def listen_and_transcribe() -> str | None:
    """
    Escuta o audio do microfone e transcreve o texto.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")
        return None

