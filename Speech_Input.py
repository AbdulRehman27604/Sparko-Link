import speech_recognition
def speech_detection():
    text = ""
    speech = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:

                speech.adjust_for_ambient_noise(mic, duration=0.2)
                audio = speech.listen(mic)

                text += " " + speech.recognize_google(audio)
                print(text)
        except speech_recognition.UnknownValueError:
            speech = speech_recognition.Recognizer()
            continue
        return text.strip()




