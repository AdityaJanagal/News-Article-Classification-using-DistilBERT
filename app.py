import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# Load trained model and tokenizer
model_path = "./news_classifier"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

model.eval()


# Class names
label_names = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Sci/Tech"
}


# Prediction function
def predict_news(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

    probabilities = torch.softmax(
        outputs.logits,
        dim=-1
    )

    predicted_class = torch.argmax(
        probabilities,
        dim=-1
    ).item()

    confidence = probabilities[0][predicted_class].item()

    return label_names[predicted_class], confidence


# Streamlit UI
st.title("📰 News Article Classification")
st.write("Classify a news article using a fine-tuned DistilBERT Transformer model.")


# Text input
text = st.text_area(
    "Enter a news article:",
    height=200,
    placeholder="Enter your news article here..."
)


# Predict button
if st.button("Predict"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        category, confidence = predict_news(text)

        st.success(f"Category: {category}")

        st.info(
            f"Confidence: {confidence * 100:.2f}%"
        )
