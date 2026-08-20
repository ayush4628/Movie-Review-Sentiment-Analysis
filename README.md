<p align="center">
  <h1 align="center">🎬 Movie Review Sentiment Analysis 🍿</h1>
  <p align="center">
    A deep learning-powered web application that analyzes movie reviews and classifies them as <strong>Positive</strong> or <strong>Negative</strong>.
  </p>
</p>

<p align="center">
  <a href="https://movie-review-sentiment-analysis-wbsm.onrender.com/">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Open%20App-2ea44f?style=for-the-badge" alt="Live Demo">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow">
  <img src="https://img.shields.io/badge/GRU-RNN-8A2BE2?style=flat-square" alt="GRU">
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=flat-square&logo=render&logoColor=111111" alt="Render">
  <img src="https://img.shields.io/badge/Accuracy-90.34%25-blue?style=flat-square" alt="Accuracy">
  <img src="https://img.shields.io/github/license/ayush4628/Movie-Review-Sentiment-Analysis?style=flat-square" alt="License">
</p>

---

## 📌 Overview

**Movie Review Sentiment Analysis** is an end-to-end Natural Language Processing and Deep Learning project that predicts the sentiment of a movie review.

The application takes a user's review as input and uses a trained **GRU (Gated Recurrent Unit)** neural network to classify it into:

* 😊 **Positive**
* 😞 **Negative**

The project covers the complete workflow from **data preprocessing and model training to evaluation, Flask API development, and cloud deployment**.

---

## 🔍 How It Works

```text
Movie Review
     ↓
Text Preprocessing
     ↓
Tokenization
     ↓
Sequence Padding
     ↓
GRU Deep Learning Model
     ↓
Sentiment Probability
     ↓
Positive / Negative
```

The trained model is integrated into a Flask web application and deployed on **Render**.

---

## 🌐 Live Demo

### 🚀 Try the Application

**[Open Movie Review Sentiment Analyzer →](https://movie-review-sentiment-analysis-wbsm.onrender.com/)**

Enter any movie review and click **Analyze Sentiment** to see the model's prediction.

### 💡 Example

```text
Review:
"The movie was absolutely fantastic. The acting was brilliant,
the story was engaging, and I enjoyed every minute of it."

Prediction:
Positive

Confidence:
High
```

> **Deployment note:** Since the application is hosted on Render, the first request after the service has been inactive may take a little longer while the server starts.

---


## 🧠 Dataset

The model was trained using the **IMDb Movie Reviews dataset** for binary sentiment classification.

| Property            |                         Details |
| ------------------- | ------------------------------: |
| 📚 Dataset          |              IMDb Movie Reviews |
| 📊 Total Reviews    |                          50,000 |
| 🏷️ Classes         |                               2 |
| 😊 Positive Reviews |                          25,000 |
| 😞 Negative Reviews |                          25,000 |
| 🎯 Task             | Binary Sentiment Classification |

The objective is to learn the relationship between the words used in a review and the overall sentiment expressed by the reviewer.

---

## 📊 Model Performance

The final deployed model uses a **GRU (Gated Recurrent Unit)** architecture.

| Metric       |      Score |
| ------------ | ---------: |
| 🎯 Accuracy  | **90.34%** |
| 🎯 Precision | **91.64%** |
| 🎯 Recall    | **88.78%** |
| 🎯 F1 Score  | **90.19%** |

The model provides a strong balance between identifying positive and negative movie reviews.

### Model Configuration

| Parameter               |    Value |
| ----------------------- | -------: |
| Dataset                 | IMDb 50K |
| Vocabulary Size         |   20,000 |
| Maximum Sequence Length |      600 |
| Model                   |      GRU |
| Output Layer            |  Sigmoid |
| Classification          |   Binary |
| Decision Threshold      |      0.5 |

---

## 🧠 Why GRU?

A **GRU (Gated Recurrent Unit)** is a type of Recurrent Neural Network designed for sequential data.

Movie reviews are sequences of words, so understanding the order and relationship between words is important.

GRU is useful because it can:

* Understand sequential text
* Capture relationships between words
* Handle long-term dependencies
* Use fewer gates than LSTM
* Provide efficient training and inference

The GRU model was selected as the final model for deployment because it provided strong sentiment classification performance while remaining suitable for a web application.

---

## 🛠️ Tech Stack

| Category           | Technology                        |
| ------------------ | --------------------------------- |
| 🐍 Programming     | Python                            |
| 🧠 Deep Learning   | TensorFlow / Keras                |
| 🔄 Neural Network  | GRU                               |
| 📝 NLP             | Text Preprocessing / Tokenization |
| 🌐 Backend         | Flask                             |
| 🎨 Frontend        | HTML / CSS / JavaScript           |
| 📊 Data Processing | NumPy / Pandas                    |
| 📓 Development     | Jupyter Notebook                  |
| 🚀 Deployment      | Render                            |
| 🐙 Version Control | Git / GitHub                      |

---

## 📂 Project Structure

```text
Movie-Review-Sentiment-Analysis/
│
├── static/
│   └── ...                         # CSS, JavaScript and static assets
│
├── templates/
│   └── ...                         # HTML templates
│
├── .gitignore
├── .python-version
├── LICENSE
│
├── Movie_Sentiment_Analysis.ipynb
│       # Model training, experimentation
│       # and evaluation
│
├── README.md
│
├── app.py
│       # Flask application
│
├── check_model.py
│       # Model prediction testing
│
├── config_lite.json
│       # Model configuration
│
├── imdb_gru_lite_model.keras
│       # Trained GRU model
│
├── imdb_tokenizer_lite.pkl
│       # Saved IMDb tokenizer
│
└── requirements.txt
        # Python dependencies
```

---

## 📝 Text Preprocessing

Before a review is passed to the GRU model, it goes through text preprocessing.

```text
Raw Review
    ↓
Remove HTML / URLs
    ↓
Convert to Lowercase
    ↓
Remove Punctuation
    ↓
Tokenization
    ↓
Convert Text → Integer Sequences
    ↓
Padding / Truncation
    ↓
GRU Model
```

This ensures that the input during prediction follows the same general preprocessing approach used during model training.

---

## 🎬 Application Features

The web application provides an interactive interface for movie sentiment analysis.

### ✨ Features

* 🎬 Movie-themed user interface
* 📝 Custom movie review input
* 😊 Positive sentiment prediction
* 😞 Negative sentiment prediction
* 📊 Confidence score
* 📈 Positive and negative probability
* 🔢 Word count
* 🧹 Cleaned word count
* 💡 Example reviews for quick testing
* 🔄 Loading state during prediction
* 📱 Responsive interface
* 🔌 REST prediction API
* ⚡ Real-time model inference

---

## 🔌 REST API

The Flask application provides a prediction endpoint that can be used programmatically.

### `POST /predict`

Send a movie review to the endpoint.

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

A health-check endpoint is available to verify that the Flask application is running correctly.

---
## 💻 Run Locally

Follow these steps to run the project on your local machine.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ayush4628/Movie-Review-Sentiment-Analysis.git
```

```bash
cd Movie-Review-Sentiment-Analysis
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

### 3️⃣ Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### 5️⃣ Start the Flask application

```bash
python app.py
```

### 6️⃣ Open the application

Visit:

```text
http://127.0.0.1:5000/
```

---

## 🎯 Example Predictions

### 😊 Positive Review

```text
"The movie was absolutely brilliant. The acting was amazing,
the story was engaging, and the ending was perfect."
```

**Expected:**

```text
Sentiment: Positive
```

---

### 😞 Negative Review

```text
"This movie was terrible. The story was boring,
the acting was weak, and the ending was disappointing."
```

**Expected:**

```text
Sentiment: Negative
```

---

### 🤔 Mixed Review

```text
"I expected this movie to be great, but it turned out to be
both enjoyable and disappointing. The performances were strong
and there were several genuinely funny moments, but the weak
story and unnecessary scenes made the movie feel much longer.
There were parts I loved and parts I couldn't stand, so I
honestly have mixed feelings about it."
```

A mixed review may produce a lower confidence score because it contains both positive and negative sentiment.

---

## 📚 Key Learning Outcomes

This project helped me understand how to take an NLP deep learning model from experimentation to a deployable web application.

### 🧠 Deep Learning

* Understanding Recurrent Neural Networks
* Implementing GRU architecture
* Working with sequential text data
* Training a binary classification model
* Evaluating deep learning models
* Saving and loading trained models

### 📝 Natural Language Processing

* Text cleaning
* Tokenization
* Vocabulary creation
* Sequence conversion
* Padding and truncation
* Text classification

### 📊 Model Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* Prediction probability
* Confidence analysis

### 🌐 Deployment

* Building a Flask application
* Creating REST APIs
* Connecting frontend with backend
* Loading a trained model during inference
* Deploying a machine learning application on Render

---

## 🚀 Future Improvements

The current project can be extended with:

* [ ] 🔵 Add LSTM and BiLSTM model comparison
* [ ] 🟣 Add attention mechanism
* [ ] 🟢 Add neutral sentiment classification
* [ ] 🧠 Add explainable AI for predictions
* [ ] 🎭 Improve sarcasm detection
* [ ] 🤔 Improve mixed-review handling
* [ ] 📜 Add prediction history
* [ ] 📊 Add sentiment analytics dashboard
* [ ] 📥 Add downloadable prediction reports
* [ ] 🧪 Add automated unit tests
* [ ] 🔄 Add GitHub Actions CI/CD
* [ ] 🐳 Add Docker support
* [ ] ⚡ Optimize TensorFlow inference
* [ ] 🚀 Improve Render cold-start performance

---

## 📊 Project Status

| Component              | Status      |
| ---------------------- | ----------- |
| 📚 IMDb Dataset        | ✅ Completed |
| 🧹 Text Preprocessing  | ✅ Completed |
| 🔤 Tokenization        | ✅ Completed |
| 🧠 GRU Model           | ✅ Completed |
| 🎯 Model Evaluation    | ✅ Completed |
| 💾 Model Serialization | ✅ Completed |
| 🌐 Flask Application   | ✅ Completed |
| 🔌 REST API            | ✅ Completed |
| 🎨 Frontend            | ✅ Completed |
| ☁️ Render Deployment   | ✅ Completed |
| 🐙 GitHub Repository   | ✅ Completed |

---

## 👨‍💻 Author

### Ayush Maurya

**Data Science / Machine Learning Enthusiast**

Interested in building practical applications using:

* 🐍 Python
* 📊 Data Science
* 🤖 Machine Learning
* 🧠 Deep Learning
* 📝 Natural Language Processing
* ✨ Generative AI
* 🌐 Machine Learning Deployment

### 🔗 Connect With Me

<p>
  <a href="https://github.com/ayush4628">
    <img src="https://img.shields.io/badge/GitHub-ayush4628-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/ayush4628/">
    <img src="https://img.shields.io/badge/LinkedIn-Ayush%20Maurya-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</p>

---

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for more information.

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a **⭐ Star** on GitHub.

<p align="center">
  <strong>🎬 + 🧠 + 📝 = 🚀</strong>
  <br>
  <sub>Built with Python, TensorFlow, GRU, Flask & curiosity.</sub>
</p>

<p align="center">
  Made with ❤️ for learning, experimentation and real-world Machine Learning.
</p>
