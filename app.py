import streamlit as st
import random
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load Mistral 7B Model
model = AutoModelForCausalLM.from_pretrained('mistralai/Mistral-7B-v0.1')
tokenizer = AutoTokenizer.from_pretrained('mistralai/Mistral-7B-v0.1')

# Streamlit App Title
st.title("AI Doctor Role-Play Trainer")
st.write("Practice responding to dynamic doctor questions using Mistral 7B.")

# Predefined Questions for Role-Play
questions = [
    "Why should I prescribe your brand?",
    "How is your product different from competitors?",
    "Can you explain the safety profile?",
    "What is the evidence supporting your product’s efficacy?"
]

# Function to get AI-generated response
def get_mistral_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Random Question Generator
if st.button("Start Role-Play"):
    question = random.choice(questions)
    st.write(f"Doctor: {question}")
    user_response = st.text_input("Your Response:")
    if user_response:
        ai_reply = get_mistral_response(f"Doctor: {question} MR: {user_response}")
        st.write(f"Doctor's Response: {ai_reply}")
