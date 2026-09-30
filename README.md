# 📰 News Article Classification using DistilBERT

An end-to-end NLP project that uses a **fine-tuned DistilBERT Transformer** to classify news articles into four categories: **World, Sports, Business, and Sci/Tech**.

The project includes data preprocessing, Transformer tokenization, model fine-tuning, evaluation, model deployment on Hugging Face, and an interactive Streamlit web application.

---

## 🚀 Live Demo

**Streamlit App:**
https://news-article-classification-using-distilbert-6kaysaaopr7fa9euz.streamlit.app/

**Hugging Face Model:**
https://huggingface.co/Adityajanagal/distilbert-news-classifier

---

## 📌 Project Overview

News articles can cover many different topics, making automatic categorization useful for news platforms, search systems, and content organization.

In this project, **DistilBERT** is fine-tuned on the **AG News dataset** to automatically classify a given news article into one of four categories:

| Label | Category    |
| ----- | ----------- |
| 0     | 🌍 World    |
| 1     | ⚽ Sports    |
| 2     | 💼 Business |
| 3     | 🤖 Sci/Tech |

The model achieved **94.89% accuracy** on the test dataset.

---

## 🧠 Model

The project uses:

**DistilBERT (`distilbert-base-uncased`)**

DistilBERT is a smaller and faster version of BERT that retains much of BERT's language-understanding capability while requiring fewer computational resources.

The pretrained DistilBERT model was fine-tuned for a **4-class sequence classification task**.

### Model Workflow

```text
News Article
     ↓
DistilBERT Tokenizer
     ↓
Input IDs + Attention Mask
     ↓
Fine-tuned DistilBERT
     ↓
Classification Head
     ↓
Class Probabilities
     ↓
Predicted Category
```

---

## 📊 Dataset

The project uses the **AG News dataset**, a standard dataset for news classification.

It contains four categories:

* World
* Sports
* Business
* Sci/Tech

The model was trained using the **full AG News training dataset** and evaluated on the test dataset.

---

## 🔄 Project Pipeline

```text
AG News Dataset
       ↓
Data Loading
       ↓
DistilBERT Tokenization
       ↓
Padding & Truncation
       ↓
Fine-tuning DistilBERT
       ↓
Model Evaluation
       ↓
Save Model
       ↓
Upload Model to Hugging Face
       ↓
Streamlit Web Application
```

---

## ⚙️ Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* Scikit-learn
* Streamlit
* NumPy
* Safetensors

---

## 📈 Model Performance

| Metric            |         Result |
| ----------------- | -------------: |
| Test Accuracy     |     **94.89%** |
| Evaluation Loss   |     **0.1870** |
| Number of Classes |          **4** |
| Base Model        | **DistilBERT** |
| Training Epochs   |          **2** |

---

## 🛠️ Training Configuration

The model was fine-tuned using the following configuration:

```text
Learning Rate: 2e-5
Training Batch Size: 16
Evaluation Batch Size: 16
Epochs: 2
Weight Decay: 0.01
Maximum Sequence Length: 128
```

---

## 💻 Streamlit Application

The project includes an interactive Streamlit application where users can enter a news article and receive:

* Predicted news category
* Model confidence

Example:

```text
Input:
Researchers developed a new artificial intelligence system
for analyzing medical images.

Output:
Category: Sci/Tech
Confidence: 98.XX%
```

---

## 📁 Project Structure

```text
News-Article-Classification-using-DistilBERT/
│
├── transformer.ipynb
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

The trained model is hosted separately on **Hugging Face** because the model weights are too large for GitHub's standard 100 MB file limit.

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/AdityaJanagal/News-Article-Classification-using-DistilBERT.git
```

### 2. Navigate to the project

```bash
cd News-Article-Classification-using-DistilBERT
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🤗 Hugging Face Model

The trained model is hosted on Hugging Face:

**Adityajanagal/distilbert-news-classifier**

The Streamlit application automatically downloads the model from Hugging Face when required.

---

## 🎯 What I Learned

Through this project, I worked with:

* Transformer architecture
* DistilBERT
* Hugging Face Transformers
* Tokenization
* Attention masks
* Sequence classification
* Fine-tuning pretrained models
* PyTorch inference
* Model evaluation
* Hugging Face model hosting
* Streamlit deployment

---

## 🔮 Future Improvements

Possible improvements include:

* Add a larger and more diverse news dataset
* Experiment with other Transformer architectures
* Perform hyperparameter tuning
* Add confusion matrix and detailed evaluation metrics
* Add batch prediction support
* Build a news summarization feature
* Explore RAG-based news question answering

---

## 👨‍💻 Author

**Aditya Janagal**

B.Tech — Artificial Intelligence & Data Science

GitHub:
https://github.com/AdityaJanagal

---

⭐ If you found this project useful, feel free to explore the repository and try the Streamlit application.
