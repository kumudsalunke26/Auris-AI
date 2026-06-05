

# import pyttsx3

# def text_to_speech(text, filename="output.wav"):
#     engine = pyttsx3.init()
#     engine.save_to_file(text, filename)
#     engine.runAndWait()
#     return filename



from gtts import gTTS
import os

def text_to_speech(text):
    os.makedirs("temp", exist_ok=True)

    file_path = "temp/output.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(file_path)

    return file_path