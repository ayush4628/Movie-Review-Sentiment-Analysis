# MovieMind — Flask Movie Review Sentiment Analysis

A polished Flask web app for the uploaded IMDB sentiment model.

## Model used

The project uses the trained **GRU** model and the same tokenizer/configuration used during training:

- IMDB dataset: 50,000 reviews
- Vocabulary size: 20,000
- Maximum sequence length: 600
- Sentiment threshold: 0.5
- GRU test accuracy: **90.34%**
- Precision: **91.64%**
- Recall: **88.78%**
- F1 score: **90.19%**

The frontend is intentionally cinematic and responsive: dark movie-studio styling, review examples, live character count, loading state, confidence meter, probability breakdown, and mobile support.

## Project structure

```text
movie_sentiment_flask/
├── app.py
├── config.json
├── imdb_gru_model.keras
├── imdb_tokenizer.pkl
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

## Run locally

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> TensorFlow installation can take some time because the trained Keras model needs TensorFlow at runtime.

### 3. Start Flask

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## API

### POST `/predict`

Request:

```json
{
  "review": "This movie was fantastic and I loved every minute of it."
}
```

Example response:

```json
{
  "sentiment": "Positive",
  "confidence": 98.98,
  "positive_probability": 98.98,
  "negative_probability": 1.02,
  "word_count": 11,
  "cleaned_word_count": 11
}
```

### GET `/health`

Returns a small health/status response so deployment platforms can verify that Flask is running.

## Deployment notes

For production deployment, use a production WSGI server such as Gunicorn where supported by the hosting platform. Do not enable Flask `debug=True` in production.

Because the model is included in the project, deployment needs enough memory to load TensorFlow and the Keras model.

## Important model compatibility note

The prediction pipeline deliberately follows the training notebook: HTML removal, lowercasing, URL removal, punctuation removal, whitespace cleanup, tokenizer conversion, post-padding/truncation to 600 tokens, and a 0.5 sentiment threshold.

The uploaded configuration specifies `max_length = 600` and `threshold = 0.5`.
