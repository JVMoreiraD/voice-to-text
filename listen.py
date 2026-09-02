from text_to_speech import text_to_speech
import speech_recognition as sr


class Listen:
    def __init__(self):
        self.r = sr.Recognizer()

    def listen_and_transcribe(self) -> str | None:
        """
        Escuta o audio do microfone e transcreve o texto.
        """
        with sr.Microphone() as source:
            audio = self.r.listen(source, timeout=15)
        try:
            text = self.r.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            text_to_speech("Não consegui entender o que você disse.")
            return None
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")
            return None

    def listen_and_wait(self, action: callable):
        while True:
            r = self.r
            with sr.Microphone() as source:
                # print("Diga algo...")
                audio = r.listen(source)

            try:
                fala = r.recognize_google(audio, language="pt-BR")
                if "bonsai" in fala.lower():
                    action()
            except sr.UnknownValueError:
                print("Não consegui entender o que você disse.")
            except sr.RequestError as e:
                print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")