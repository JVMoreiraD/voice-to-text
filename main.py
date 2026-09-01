from listen_and_transcribe import listen_and_transcribe
from text_to_speech import text_to_speech


def main():
    said = listen_and_transcribe()
    if said:
        text_to_speech(said)


main()
