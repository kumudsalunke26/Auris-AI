

import gradio as gr
from modules.detect_language import detect_language
from modules.translate_text import translate_text
from modules.sentiment_analysis import analyze_sentiment
from modules.speech_to_text import speech_to_text
from modules.text_to_speech import text_to_speech

def process_text(text, target_lang):
    lang = detect_language(text)
    translated = translate_text(text, target_lang)
    sentiment = analyze_sentiment(text)
    return lang, translated, sentiment

def process_audio(audio):
    return speech_to_text(audio)




with gr.Blocks(theme=gr.themes.Soft(), css="""
    .gradio-container {
        background: linear-gradient(135deg, #0f172a, #1e1b4b, #000000);
        color: white;
    }
    .title {
        font-size: 26px;
        font-weight: bold;
        text-align: center;
        color: #a5b4fc;
        margin-bottom: 26px;
    }
""") as demo:

    gr.Markdown("<div class='title'>🌍 AURIS: Advanced Unified Recognition and Intelligent System for Multilingual Language Processing</div>")

    with gr.Tab("🧠 Text Processing"):
        gr.Markdown("### Analyze language, sentiment & translation instantly")

        with gr.Row():
            text_input = gr.Textbox(
                label="Enter Text",
                placeholder="Type your sentence here...",
                lines=4
            )

        lang_dropdown = gr.Dropdown(
            ["en","hi","mr","fr","es","de","it","ta","te","bn","gu","pa","ur","ar","zh","ja","ko"],
            label="Target Language",
            value="en"
        )

        btn = gr.Button("🚀 Process with AURIS", variant="primary")

        with gr.Row():
            detected = gr.Textbox(label="Detected Language")
            translated = gr.Textbox(label="Translated Text")
            sentiment = gr.Textbox(label="Sentiment Analysis")

        btn.click(process_text, [text_input, lang_dropdown],
                  [detected, translated, sentiment])


    with gr.Tab("🎤 Speech to Text"):
        gr.Markdown("### Convert your voice into text")

        audio_input = gr.Audio(type="filepath", label="Upload / Record Audio")
        speech_output = gr.Textbox(label="Recognized Text")

        btn2 = gr.Button("🎤 Convert Speech")

        btn2.click(process_audio, audio_input, speech_output)


    with gr.Tab("🔊 Text to Speech"):
        gr.Markdown("### Convert text into natural voice")

        tts_input = gr.Textbox(label="Enter Text", lines=4)
        # tts_output = gr.Audio(label="Generated Speech")

        tts_output = gr.Audio(
    type="filepath",
    label="Generated Speech"
)

        btn3 = gr.Button("🔊 Generate Voice")

        btn3.click(text_to_speech, tts_input, tts_output)

demo.launch()