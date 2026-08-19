import json
import pickle
import re
import string
from pathlib import Path

import numpy as np
from flask import Flask, jsonify, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "config.json", "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

MAX_LENGTH = int(CONFIG.get("max_length", 600))
THRESHOLD = float(CONFIG.get("threshold", 0.5))

with open(BASE_DIR / "imdb_tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

model = load_model(BASE_DIR / "imdb_gru_model.keras", compile=False)


def clean_text(text: str) -> str:
    """Keep preprocessing aligned with the training notebook."""
    text = re.sub(r"<.*?>", " ", text)
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def predict_sentiment(review: str) -> dict:
    cleaned = clean_text(review)
    sequence = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post",
    )

    probability = float(model.predict(padded, verbose=0)[0][0])

    if probability >= THRESHOLD:
        sentiment = "Positive"
        confidence = probability
    else:
        sentiment = "Negative"
        confidence = 1.0 - probability

    return {
        "sentiment": sentiment,
        "confidence": round(confidence * 100, 2),
        "positive_probability": round(probability * 100, 2),
        "negative_probability": round((1.0 - probability) * 100, 2),
        "word_count": len(review.split()),
        "cleaned_word_count": len(cleaned.split()),
    }


app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify({"status": "ok", "model": "GRU", "max_length": MAX_LENGTH})


@app.post("/predict")
def predict():
    data = request.get_json(silent=True) or {}
    review = str(data.get("review", "")).strip()

    if not review:
        return jsonify({"error": "Please enter a movie review."}), 400

    if len(review) > 12000:
        return jsonify({"error": "Please keep the review under 12,000 characters."}), 400

    try:
        result = predict_sentiment(review)
        return jsonify(result)
    except Exception as exc:
        app.logger.exception("Prediction failed")
        return jsonify({"error": f"Prediction failed: {exc}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
