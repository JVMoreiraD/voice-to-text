import pyttsx3


def text_to_speech(text: str):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    for voice in voices:
        if "portuguese" in voice.name.lower() or "brazil" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.setProperty('rate', 200)
    engine.setProperty('volume', 0.8)

    engine.say(text)
    engine.runAndWait()

