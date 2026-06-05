# import speech_recognition as sr

# def speech_to_text(audio_file):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(audio_file) as source:
#         audio = recognizer.record(source)
#     try:
#         return recognizer.recognize_google(audio)
#     except:
#         return "Speech recognition failed"

import speech_recognition as sr

def speech_to_text(audio_file):
    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "API unavailable"