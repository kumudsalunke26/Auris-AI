---

title: Auris AI
emoji: 📚
colorFrom: pink
colorTo: pink
sdk: gradio
sdk_version: 6.16.0
python_version: 3.13
app_file: app.py
pinned: false
---

# AURIS AI 🤖

## Advanced Unified Recognition & Intelligence System

AURIS AI is a **multilingual Natural Language Understanding (NLU) and speech-processing platform** that integrates multiple language and speech capabilities into a unified application.

The system combines **language detection, machine translation, sentiment analysis, speech-to-text, and text-to-speech** to provide an integrated multilingual AI experience across **10+ languages**.

---

## ✨ Features

| Feature                        | Description                                         |
| ------------------------------ | --------------------------------------------------- |
| 🌐 **Language Detection**      | Automatically identifies the language of text input |
| 🔄 **Machine Translation**     | Translates text between supported languages         |
| 😊 **Sentiment Analysis**      | Analyzes the sentiment of textual input             |
| 🎤 **Speech-to-Text**          | Converts spoken language into text                  |
| 🔊 **Text-to-Speech**          | Converts text into natural-sounding speech          |
| 🌍 **Multilingual Processing** | Supports 10+ languages                              |
| 🖥️ **Interactive Interface**  | Unified Gradio-based user interface                 |

---

## 🧠 System Architecture

```text
                         ┌──────────────────┐
                         │     User Input   │
                         │   Text / Speech  │
                         └────────┬─────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
               Text Input                 Speech Input
                    │                           │
                    │                    Speech-to-Text
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Language         │
                         │ Detection        │
                         │   LangDetect     │
                         └────────┬─────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
              Translation               Sentiment Analysis
           Deep Translator                  TextBlob
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Processed Text   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Edge-TTS      │
                         │ Text-to-Speech   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   Audio Output   │
                         └──────────────────┘
```

---

## 🛠️ Technologies Used

| Category             | Technology              |
| -------------------- | ----------------------- |
| Programming Language | **Python**              |
| Interface            | **Gradio 6.16.0**       |
| Language Detection   | **LangDetect**          |
| Sentiment Analysis   | **TextBlob**            |
| Machine Translation  | **Deep Translator**     |
| Speech-to-Text       | **SpeechRecognition**   |
| Text-to-Speech       | **Edge-TTS**            |
| AI Platform          | **Hugging Face**        |
| Deployment           | **Hugging Face Spaces** |
| Version Control      | **Git / GitHub**        |

---

## 🔄 Processing Pipeline

AURIS AI follows a modular multilingual processing pipeline:

```text
Input
  │
  ├─────────────── Text ────────────────┐
  │                                     │
  └────────────── Speech ──► STT ───────┤
                                        ▼
                              Language Detection
                                        │
                    ┌───────────────────┼──────────────────┐
                    │                   │                  │
                    ▼                   ▼                  ▼
              Translation        Sentiment          Text Processing
                    │             Analysis
                    └───────────────────┼──────────────────┘
                                        │
                                        ▼
                                  Text-to-Speech
                                        │
                                        ▼
                                   Audio Output
```

---

## 🌍 Multilingual Support

AURIS AI supports **10+ languages** across its language-processing workflow.

The multilingual pipeline enables users to:

* Detect the language of text.
* Translate text into supported languages.
* Analyze textual sentiment.
* Convert speech into text.
* Generate speech from processed text.

The project focuses on making language-processing capabilities accessible through a single interface rather than requiring users to interact with separate tools for each task.

---

## 🔬 Research Focus

AURIS AI explores **multilingual Natural Language Understanding (NLU)** by integrating multiple NLP tasks into a single system.

The project investigates how different language-processing components can work together across diverse languages and language families.

### Research areas

* Multilingual NLP
* Natural Language Understanding
* Cross-lingual text processing
* Machine translation
* Sentiment analysis
* Speech recognition
* Speech synthesis
* Human-computer interaction

---

## 🧩 Core Components

### 1. Language Detection

**LangDetect** is used to identify the language of textual input.

```text
Text Input
    ↓
LangDetect
    ↓
Detected Language
```

### 2. Machine Translation

**Deep Translator** enables translation between supported languages.

```text
Source Text
    ↓
Source Language
    ↓
Translation
    ↓
Target Language
```

### 3. Sentiment Analysis

**TextBlob** is used to analyze the sentiment of textual input.

```text
Text
 ↓
TextBlob
 ↓
Sentiment Analysis
```

### 4. Speech-to-Text

**SpeechRecognition** converts spoken input into text.

```text
Voice Input
    ↓
SpeechRecognition
    ↓
Text
    ↓
NLP Pipeline
```

### 5. Text-to-Speech

**Edge-TTS** converts processed text into speech output.

```text
Processed Text
      ↓
   Edge-TTS
      ↓
 Audio Output
```

---

## 🖥️ Application Interface

AURIS AI provides an interactive **Gradio interface** that brings the different language and speech-processing capabilities together.

The interface is designed to allow users to interact with the system without needing to manually execute individual NLP or speech-processing modules.

### Interface capabilities

* Text-based input
* Speech-based input
* Language identification
* Translation
* Sentiment analysis
* Speech generation

---

## 🧪 Testing & Validation

The system was validated through systematic testing of its individual components and integrated workflow.

Testing covered:

* Language detection
* Translation
* Sentiment analysis
* Speech recognition
* Text-to-speech generation
* Multilingual inputs
* End-to-end processing

The validation process was used to verify that the individual modules function correctly and work together within the unified pipeline.

---

## ☁️ Deployment

AURIS AI is deployed on **Hugging Face Spaces** using Gradio.

### Live Demo

**Hugging Face Space:**

https://huggingface.co/spaces/kumudsalunke/Auris-AI

### Deployment Architecture

```text
             GitHub Repository
                    │
                    ▼
              Source Code
                    │
                    ▼
          Hugging Face Spaces
                    │
                    ▼
              Gradio App
                    │
                    ▼
                  Users
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AURIS
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

The Gradio application will provide a local URL in the terminal.

---

## 🎯 Project Objectives

* Build a unified multilingual NLP platform.
* Integrate multiple Natural Language Understanding tasks.
* Combine text and speech processing in one application.
* Explore cross-lingual language processing.
* Provide an accessible interface for multilingual users.
* Deploy a reproducible AI application using GitHub and Hugging Face.

---

## 🔮 Future Enhancements

* 🌍 Support additional low-resource languages.
* 🤖 Introduce transformer-based sentiment analysis.
* 🗣️ Add real-time multilingual voice conversations.
* 💬 Add conversational AI capabilities.
* 📊 Add multilingual NLP performance analytics.
* 🎙️ Improve real-time speech processing.
* 🧠 Add advanced emotion detection.
* 🔍 Introduce automated evaluation benchmarks.

---

## 📌 Project Highlights

| Metric             | Details                 |
| ------------------ | ----------------------- |
| Languages          | **10+**                 |
| Language Detection | **LangDetect**          |
| Translation        | **Deep Translator**     |
| Sentiment Analysis | **TextBlob**            |
| Speech-to-Text     | **SpeechRecognition**   |
| Text-to-Speech     | **Edge-TTS**            |
| Interface          | **Gradio 6.16.0**       |
| Python             | **3.13**                |
| Deployment         | **Hugging Face Spaces** |

---

## 👩‍💻 Author

**Kumud Salunke**


## ⭐ Acknowledgements

This project combines open-source NLP and speech-processing libraries to demonstrate an integrated multilingual AI workflow.


---
