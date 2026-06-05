# import pyttsx3

# def text_to_speech(text, filename="output_audio.mp3"):
#     engine = pyttsx3.init()
#     engine.save_to_file(text, filename)
#     engine.runAndWait()
#     return filename

import pyttsx3

def text_to_speech(text, filename="output.wav"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename