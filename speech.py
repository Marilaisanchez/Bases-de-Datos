import speech_recognition as sr

def prueba():
    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        print("Habla porfavor")
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        print("Conversion de voz a texto...")
        print(f"Usted dijo: {recog.recognize_google(audio, language = 'En-US')}")

def speech_es():
    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language = 'En-US')