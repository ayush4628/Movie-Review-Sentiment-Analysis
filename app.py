import json
import pickle
import re
import string
import time
from pathlib import Path

import numpy as np
import tensorflow as tf


# =========================================
# TENSORFLOW RESOURCE OPTIMIZATION
# =========================================

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

BASE_DIR = Path(__file__).resolve().parent


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

print("Loading GRU-Lite tokenizer...")

with open(
    BASE_DIR / "imdb_tokenizer_lite.pkl",
    "rb"
) as f:

    tokenizer = pickle.load(f)


print("GRU-Lite tokenizer loaded successfully.")


# =========================================
# LOAD MODEL
# =========================================

print("Loading GRU-Lite model...")

model = load_model(
    BASE_DIR / "imdb_gru_lite_model.keras",
    compile=False
)

print("GRU-Lite model loaded successfully.")


# =========================================
# MODEL WARM-UP
# =========================================

print("Warming up GRU-Lite model...")

dummy_input = np.zeros(
    (1, MAX_LENGTH),
    dtype=np.int32
)

model(
    dummy_input,
    training=False
)

print("GRU-Lite model warm-up completed.")


# =========================================
# FLASK APPLICATION
# =========================================

app = Flask(__name__)


# =========================================
# CLEAN TEXT
# =========================================

def clean_text(text: str) -> str:

    # Remove HTML tags
    text = re.sub(
        r"<.*?>",
        " ",
        text
    )

    # Convert to lowercase
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

    total_start = time.time()

    # -------------------------------------
    # CLEAN TEXT
    # -------------------------------------

    cleaned = clean_text(
        review
    )


    # -------------------------------------
    # TOKENIZATION
    # -------------------------------------

    sequence = tokenizer.texts_to_sequences(
        [cleaned]
    )


    # -------------------------------------
    # PADDING
    # -------------------------------------

    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post",
        truncating="post"
    )


    preprocessing_time = (
        time.time() - total_start
    )

    print(
        f"Preprocessing time: "
        f"{preprocessing_time:.4f}s"
    )


    # -------------------------------------
    # MODEL INFERENCE
    # -------------------------------------

    prediction_start = time.time()

    prediction = model(
        padded,
        training=False
    )

    probability = float(
        prediction.numpy()[0][0]
    )


    inference_time = (
        time.time() - prediction_start
    )

    print(
        f"Model inference time: "
        f"{inference_time:.4f}s"
    )


    # -------------------------------------
    # SENTIMENT
    # -------------------------------------

    if probability >= THRESHOLD:

        sentiment = "Positive"

        confidence = probability

    else:

        sentiment = "Negative"

        confidence = 1.0 - probability


    # -------------------------------------
    # TOTAL TIME
    # -------------------------------------

    total_time = (
        time.time() - total_start
    )

    print(
        f"Total prediction time: "
        f"{total_time:.4f}s"
    )

    print(
        f"Prediction probability: "
        f"{probability:.6f}"
    )

    print(
        f"Sentiment: "
        f"{sentiment}"
    )


    # -------------------------------------
    # RESPONSE
    # -------------------------------------

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
# HEALTH CHECK
# =========================================

@app.get("/health")
def health():

    return jsonify({

        "status":
            "ok",

        "model":
            "GRU-Lite",

        "max_length":
            MAX_LENGTH,

        "threshold":
            THRESHOLD

    })


# =========================================
# PREDICT API
# =========================================

@app.post("/predict")
def predict():

    try:

        # ---------------------------------
        # GET JSON DATA
        # ---------------------------------

        data = request.get_json(
            silent=True
        ) or {}


        # ---------------------------------
        # GET REVIEW
        # ---------------------------------

        review = str(
            data.get(
                "review",
                ""
            )
        ).strip()


        # ---------------------------------
        # EMPTY REVIEW
        # ---------------------------------

        if not review:

            return jsonify({

                "error":
                    "Please enter a movie review."

            }), 400


        # ---------------------------------
        # MAXIMUM LENGTH
        # ---------------------------------

        if len(review) > 12000:

            return jsonify({

                "error":
                    "Please keep the review under 12,000 characters."

            }), 400


        print(
            "----------------------------------------"
        )

        print(
            f"Prediction request received."
        )

        print(
            f"Review characters: {len(review)}"
        )

        print(
            f"Review words: {len(review.split())}"
        )


        # ---------------------------------
        # PREDICT
        # ---------------------------------

        result = predict_sentiment(
            review
        )


        # ---------------------------------
        # RETURN RESULT
        # ---------------------------------

        print(
            "Prediction completed successfully."
        )

        print(
            "----------------------------------------"
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
# LOCAL DEVELOPMENT
# =========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )