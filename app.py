import json
import pickle
import re
import string
from pathlib import Path

import numpy as np

# =========================================
# TensorFlow configuration
# =========================================

import tensorflow as tf

# Keep TensorFlow from creating too many threads
tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)


from flask import Flask, jsonify, render_template, request

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# =========================================
# BASE DIRECTORY
# =========================================

BASE_DIR = Path(__file__).resolve().parent


# =========================================
# LOAD CONFIG
# =========================================

with open(
    BASE_DIR / "config.json",
    "r",
    encoding="utf-8"
) as f:

    CONFIG = json.load(f)


MAX_LENGTH = int(
    CONFIG.get("max_length", 600)
)

THRESHOLD = float(
    CONFIG.get("threshold", 0.5)
)


# =========================================
# LOAD TOKENIZER
# =========================================

print("Loading tokenizer...")

with open(
    BASE_DIR / "imdb_tokenizer.pkl",
    "rb"
) as f:

    tokenizer = pickle.load(f)


print("Tokenizer loaded successfully.")


# =========================================
# LOAD MODEL
# =========================================

print("Loading GRU model...")

model = load_model(
    BASE_DIR / "imdb_gru_model.keras",
    compile=False
)

print("GRU model loaded successfully.")


# =========================================
# FLASK APP
# =========================================

app = Flask(__name__)


# =========================================
# TEXT CLEANING
# =========================================

def clean_text(text: str) -> str:

    """
    Keep preprocessing aligned
    with the training notebook.
    """

    # Remove HTML tags
    text = re.sub(
        r"<.*?>",
        " ",
        text
    )

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )

    # Remove punctuation
    text = text.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# =========================================
# SENTIMENT PREDICTION
# =========================================

def predict_sentiment(review: str) -> dict:

    cleaned = clean_text(review)


    # Convert text to sequence
    sequence = tokenizer.texts_to_sequences(
        [cleaned]
    )


    # Padding
    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )


    # Model prediction
    prediction = model.predict(
        padded,
        verbose=0
    )


    probability = float(
        prediction[0][0]
    )


    # Determine sentiment
    if probability >= THRESHOLD:

        sentiment = "Positive"

        confidence = probability

    else:

        sentiment = "Negative"

        confidence = 1.0 - probability


    return {

        "sentiment":
            sentiment,

        "confidence":
            round(
                confidence * 100,
                2
            ),

        "positive_probability":
            round(
                probability * 100,
                2
            ),

        "negative_probability":
            round(
                (1.0 - probability) * 100,
                2
            ),

        "word_count":
            len(review.split()),

        "cleaned_word_count":
            len(cleaned.split())
    }


# =========================================
# HOME
# =========================================

@app.get("/")
def home():

    return render_template(
        "index.html"
    )


# =========================================
# HEALTH CHECK
# =========================================

@app.get("/health")
def health():

    return jsonify({

        "status": "ok",

        "model": "GRU",

        "max_length":
            MAX_LENGTH
    })


# =========================================
# PREDICT API
# =========================================

@app.post("/predict")
def predict():

    try:

        # Get JSON safely
        data = request.get_json(
            silent=True
        )


        if not data:

            return jsonify({

                "error":
                    "No JSON data received."

            }), 400


        # Get review
        review = str(
            data.get(
                "review",
                ""
            )
        ).strip()


        # Empty review
        if not review:

            return jsonify({

                "error":
                    "Please enter a movie review."

            }), 400


        # Maximum length
        if len(review) > 12000:

            return jsonify({

                "error":
                    "Please keep the review under 12,000 characters."

            }), 400


        print(
            f"Prediction requested. "
            f"Characters: {len(review)}"
        )


        # Run prediction
        result = predict_sentiment(
            review
        )


        print(
            f"Prediction result: "
            f"{result['sentiment']} "
            f"({result['confidence']}%)"
        )


        # Return JSON
        return jsonify(
            result
        ), 200


    except Exception as exc:

        # IMPORTANT:
        # This prints the complete traceback
        # in Render logs.

        app.logger.exception(
            "Prediction failed"
        )


        return jsonify({

            "error":
                f"Prediction failed: {str(exc)}"

        }), 500


# =========================================
# LOCAL DEVELOPMENT
# =========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )