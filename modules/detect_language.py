# import joblib, os

# MODEL_PATH = os.path.join("models", "lang_detect_model.pkl")
# VEC_PATH = os.path.join("models", "lang_vectorizer.pkl")

# lang_model = joblib.load(MODEL_PATH)
# lang_vectorizer = joblib.load(VEC_PATH)

# def detect_language(text: str) -> str:
#     vec = lang_vectorizer.transform([text])
#     return lang_model.predict(vec)[0]

import langid

def detect_language(text):
    if len(text.strip()) < 3:
        return "Text too short"

    lang, confidence = langid.classify(text)

    return f"{lang}"