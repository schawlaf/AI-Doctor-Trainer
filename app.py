import os
import requests
import streamlit as st
from huggingface_hub import login

# Secure Hugging Face Authentication
huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
if not huggingface_token:
    st.error("Hugging Face token not found. Please add it to Streamlit secrets.")
else:
    login(token=huggingface_token)

# Simple Test to Verify Hugging Face Connection
response = requests.get('https://huggingface.co/api/whoami', headers={"Authorization": f"Bearer {huggingface_token}"})
if response.status_code == 200:
    st.success("✅ Hugging Face connection successful!")
else:
    st.error(f"❌ Hugging Face connection failed: {response.status_code}")
