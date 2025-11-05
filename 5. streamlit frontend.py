# src/frontend/dashboard.py
import streamlit as st
import requests

st.title("🧠 Emotion-Driven Music Generator")

if st.button("Generate Music"):
    response = requests.get("http://localhost:8000/generate").json()
    st.write(f"Detected Emotion: {response['emotion']}")
    st.audio(response["music"], format="audio/midi")