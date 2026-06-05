from langdetect import detect_langs, DetectorFactory
import re

DetectorFactory.seed = 0

def detect_language(text):
    text = text.strip()

    # 1️⃣ If too short → default English
    if len(text.split()) < 4:
        return "en"

    # 2️⃣ Clean text (important for BCA-like words)
    text_clean = re.sub(r'[^a-zA-Z\s]', '', text)

    try:
        result = detect_langs(text_clean)[0]

        # 3️⃣ Confidence check
        if result.prob < 0.70:
            return "en"

        return result.lang

    except:
        return "en"