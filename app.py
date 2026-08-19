import json
import pickle
import re
import string
from pathlib import Path

import tensorflow as tf

# Limit TensorFlow resources
tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)

from flask import (
    Flask,
    jsonify,
    render_template,
    request
)

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# =========================================
# BASE DIRECTORY
# =========================================

BASE_DIR = Path(
    __file__
).resolve().parent


# =========================================
# LOAD CONFIG
# =========================================

with open(
    BASE_DIR / "config_lite.json",
    "r",
    encoding="utf-8"
) as f:

    CONFIG = json.load(f)


MAX_LENGTH = int(
    CONFIG.get(
        "max_length",
        300
    )
)

THRESHOLD = float(
    CONFIG.get(
        "threshold",
        0.5
    )
)


# =========================================
# LOAD TOKENIZER
# =========================================

print(
    "Loading GRU-Lite tokenizer..."
)

with open(
    BASE_DIR / "imdb_tokenizer_lite.pkl",
    "rb"
) as f:

    tokenizer = pickle.load(f)


print(
    "Tokenizer loaded successfully."
)


# =========================================
# LOAD MODEL
# =========================================

print(
    "Loading GRU-Lite model..."
)

model = load_model(
    BASE_DIR / "imdb_gru_lite_model.keras",
    compile=False
)

print(
    "GRU-Lite model loaded successfully."
)


# =========================================
# FLASK
# =========================================

app = Flask(
    __name__
)


# =========================================
# CLEAN TEXT
# =========================================

def clean_text(text):

    text = re.sub(
        r"<.*?>",
        " ",
        text
    )

    text = text.lower()

    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )

    text = text.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# =========================================
# PREDICTION
# =========================================

def predict_sentiment(review):

    cleaned = clean_text(
        review
    )


    sequence = (
        tokenizer
        .texts_to_sequences(
            [cleaned]
        )
    )


    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )


    probability = float(
        model.predict(
            padded,
            verbose=0
        )[0][0]
    )


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

        "word_count":
            len(
                review.split()
            )
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
# HEALTH
# =========================================

@app.get("/health")
def health():

    return jsonify({

        "status":
            "ok",

        "model":
            "GRU-Lite",

        "max_length":
            MAX_LENGTH

    })


# =========================================
# PREDICT
# =========================================

@app.post("/predict")
def predict():

    try:

        data = request.get_json(
            silent=True
        ) or {}


        review = str(
            data.get(
                "review",
                ""
            )
        ).strip()


        if not review:

            return jsonify({

                "error":
                    "Please enter a movie review."

            }), 400


        if len(review) > 12000:

            return jsonify({

                "error":
                    "Please keep the review under 12,000 characters."

            }), 400


        result = predict_sentiment(
            review
        )


        return jsonify(
            result
        ), 200


    except Exception as exc:

        app.logger.exception(
            "Prediction failed"
        )


        return jsonify({

            "error":
                f"Prediction failed: {str(exc)}"

        }), 500


# =========================================
# LOCAL
# =========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )