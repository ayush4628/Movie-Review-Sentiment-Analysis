# 🎬 Movie Review Sentiment Analysis

<p align="center">
  <strong>MovieMind — Deep Learning based Movie Review Sentiment Analysis</strong>
</p>

<p align="center">
  A Flask web application that uses a trained GRU neural network to classify movie reviews as <strong>Positive</strong> or <strong>Negative</strong>.
</p>

<p align="center">
  <a href="https://movie-review-sentiment-analysis-wbsm.onrender.com/">🚀 Live Demo</a>
  &nbsp; • &nbsp;
  <a href="https://github.com/ayush4628/Movie-Review-Sentiment-Analysis">📂 GitHub Repository</a>
</p>

---

## 📌 Project Overview

**MovieMind** is an end-to-end Natural Language Processing and Deep Learning project built to understand the sentiment expressed in movie reviews.

The project starts with the **IMDb 50K movie review dataset**, performs text preprocessing and tokenization, trains and evaluates deep learning models, and finally deploys the trained **GRU (Gated Recurrent Unit)** model as an interactive Flask web application.

The deployed application allows users to enter a movie review and instantly receive:

- 🎭 Predicted sentiment
- 📊 Prediction confidence
- 📈 Positive probability
- 📉 Negative probability
- 🔢 Word count
- 🧹 Cleaned word count

The application is designed with a cinematic dark interface, example reviews, a live character counter, loading state, confidence visualization, and responsive support for different screen sizes.

---

## 🌐 Live Demo

### 🚀 Try the Application

**Live App:**  
https://movie-review-sentiment-analysis-wbsm.onrender.com/

Enter your own movie review and click **Analyze Sentiment** to see the model's prediction.

### Example

```text
Review:
"This movie was absolutely fantastic. The acting was brilliant,
the story was engaging, and I enjoyed every minute of it."

Prediction:
Positive

Confidence:
High
```

> **Note:** The application is hosted on Render. If the service has been idle, the first request may take a little longer because the deployment needs to wake up.

---

## 🧠 Machine Learning / Deep Learning Approach

This project focuses on **Natural Language Processing (NLP)** with a recurrent neural network.

### Dataset

The model is trained using the **IMDb Movie Reviews dataset** containing:

- **50,000 movie reviews**
- Binary sentiment classification
- `Positive` and `Negative` labels

### Text Processing Pipeline

The prediction pipeline follows the same preprocessing approach used during model training:

```text
Raw Review
    ↓
Remove HTML
    ↓
Convert to Lowercase
    ↓
Remove URLs
    ↓
Remove Punctuation
    ↓
Clean Whitespace
    ↓
Tokenizer
    ↓
Convert Words → Integer Sequences
    ↓
Padding / Truncation
    ↓
GRU Model
    ↓
Sigmoid Probability
    ↓
Positive / Negative
```

The deployed configuration uses:

| Parameter | Value |
|---|---:|
| Dataset | IMDb 50K Reviews |
| Vocabulary Size | 20,000 |
| Maximum Sequence Length | 600 |
| Sentiment Threshold | 0.5 |
| Model | GRU |
| Output | Binary Sentiment |

---

## 📊 Model Performance

The final deployed GRU model achieved the following performance on the test set:

| Metric | Score |
|---|---:|
| **Accuracy** | **90.34%** |
| **Precision** | **91.64%** |
| **Recall** | **88.78%** |
| **F1 Score** | **90.19%** |

These metrics show that the model provides a strong balance between identifying positive and negative reviews.

### Why GRU?

GRU was selected because it is designed for sequential data and can capture relationships between words across a review while using fewer gates than an LSTM.

This makes GRU a good balance between:

- Sequence understanding
- Model complexity
- Training efficiency
- Inference performance

---

## 🏗️ Application Architecture

```text
                     USER
                       │
                       ▼
              ┌─────────────────┐
              │   Flask Web UI  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Review Input   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Text Preprocess │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ IMDb Tokenizer  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Padding /       │
              │ Truncation      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   GRU Model     │
              │   TensorFlow    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Sentiment +     │
              │ Confidence      │
              └────────┬────────┘
                       │
                       ▼
                    USER
```

---

## ✨ Features

- 🎬 Interactive movie-review interface
- 🧠 Deep Learning based sentiment classification
- 🔄 GRU sequence model
- 📝 Real-time review input
- 📊 Confidence/probability visualization
- 🎭 Positive and Negative sentiment prediction
- 🔢 Live character/word information
- ⚡ Lightweight inference pipeline
- 📱 Responsive frontend
- 🩺 Health-check endpoint for deployment
- 🔌 JSON prediction API
- ☁️ Deployed on Render
- 🧪 Separate script for checking the trained model

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Deep Learning / NLP

- TensorFlow
- Keras
- GRU
- Natural Language Processing
- Text Tokenization
- Sequence Padding

### Backend

- Flask

### Frontend

- HTML
- CSS
- JavaScript

### Data & Experimentation

- NumPy
- Pandas
- Jupyter Notebook
- IMDb Dataset

### Deployment

- Render
- Gunicorn / WSGI deployment

### Development Tools

- Git
- GitHub
- Python Virtual Environment

---

## 📁 Project Structure

```text
Movie-Review-Sentiment-Analysis/
│
├── static/
│   ├── style.css
│   └── app.js
│
├── templates/
│   └── index.html
│
├── .gitignore
├── .python-version
├── LICENSE
├── Movie_Sentiment_Analysis.ipynb
├── README.md
├── app.py
├── check_model.py
├── config_lite.json
├── imdb_gru_lite_model.keras
├── imdb_tokenizer_lite.pkl
└── requirements.txt
```

### Important Files

| File | Purpose |
|---|---|
| `app.py` | Flask application and prediction API |
| `Movie_Sentiment_Analysis.ipynb` | Model training, experimentation, and evaluation |
| `imdb_gru_lite_model.keras` | Trained GRU model |
| `imdb_tokenizer_lite.pkl` | Tokenizer used during training |
| `config_lite.json` | Model preprocessing/configuration |
| `check_model.py` | Script for testing model predictions |
| `templates/index.html` | Main web page |
| `static/style.css` | Application styling |
| `static/app.js` | Frontend interactions |
| `requirements.txt` | Python dependencies |

---

## 🔬 Model Development

The model development process was performed in the Jupyter Notebook.

### Main steps

1. Load the IMDb dataset.
2. Explore and inspect the review data.
3. Clean the text.
4. Convert text into sequences.
5. Build a vocabulary using a tokenizer.
6. Pad sequences to a fixed length.
7. Build recurrent neural network architectures.
8. Train the models.
9. Evaluate using classification metrics.
10. Select the final GRU model.
11. Save the trained model and tokenizer.
12. Integrate the model with Flask.
13. Build the interactive frontend.
14. Deploy the application on Render.

---

## 🔌 API

The Flask application also exposes a prediction endpoint.

### `POST /predict`

#### Request

```json
{
  "review": "This movie was fantastic and I loved every minute of it."
}
```

#### Example Response

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

### `GET /health`

Returns a small health/status response that can be used to verify that the Flask application is running correctly.

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/ayush4628/Movie-Review-Sentiment-Analysis.git
cd Movie-Review-Sentiment-Analysis
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open the application

```text
http://127.0.0.1:5000
```

---

## 🧪 Test the Model

You can use `check_model.py` to test the trained model independently.

```bash
python check_model.py
```

You can also enter custom reviews through the web interface after starting the Flask application.

---

## 🎯 Example Reviews

### Positive

```text
"The movie was brilliant. The performances were outstanding
and the story kept me engaged from beginning to end."
```

Expected sentiment:

```text
Positive
```

### Negative

```text
"This was a terrible movie with a weak story, poor acting,
and a very disappointing ending."
```

Expected sentiment:

```text
Negative
```

### Mixed / Ambiguous

```text
"The visuals were amazing and the actors did a great job,
but the story was slow and the ending felt disappointing."
```

For mixed or ambiguous reviews, the model may produce a prediction with lower confidence because the review contains both positive and negative language.

---

## ⚙️ Deployment

The application is deployed using **Render**.

The production application contains:

- Flask backend
- Trained Keras GRU model
- Saved tokenizer
- Model configuration
- HTML/CSS/JavaScript frontend
- Production WSGI configuration

### Deployment considerations

Because TensorFlow and the trained Keras model are loaded at runtime, the deployment requires sufficient memory and may take some time to initialize.

The application should run Flask through a production WSGI server rather than Flask's development server in production.

---

## 📌 Key Learning Outcomes

This project helped me practice an end-to-end Deep Learning workflow:

- Natural Language Processing
- Text preprocessing
- Tokenization
- Sequence padding
- Recurrent Neural Networks
- GRU architecture
- Binary classification
- Model evaluation
- Precision, Recall and F1 Score
- Model serialization
- Flask model deployment
- REST API development
- Frontend and backend integration
- Git and GitHub
- Cloud deployment

---

## 🔮 Future Improvements

Some possible improvements for the next version:

- [ ] Add LSTM and BiLSTM comparison to the deployed application
- [ ] Add neutral sentiment classification
- [ ] Add attention mechanism
- [ ] Add model explainability
- [ ] Improve handling of sarcasm and mixed reviews
- [ ] Add prediction history
- [ ] Add downloadable prediction reports
- [ ] Add automated testing
- [ ] Add Docker support
- [ ] Add CI/CD with GitHub Actions
- [ ] Optimize TensorFlow inference and cold-start performance

---

## 📜 License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

---

## 👨‍💻 Author

**Ayush Maurya**

Data Science / Machine Learning Enthusiast

Interested in:

- Data Science
- Machine Learning
- Deep Learning
- Natural Language Processing
- Generative AI
- Python Development

### Connect with me

- GitHub: https://github.com/ayush4628
- LinkedIn: Add your LinkedIn profile here

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

Thanks for checking out **MovieMind — Movie Review Sentiment Analysis**! 🎬🧠
