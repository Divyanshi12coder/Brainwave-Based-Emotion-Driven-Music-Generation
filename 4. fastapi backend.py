# src/app.py
from fastapi import FastAPI
from src.acquisition.eeg_stream import simulate_eeg_stream
from src.emotion_model.emotion_classifier import classify_emotion
from src.music_gen.music_generator import generate_music

app = FastAPI()

@app.get("/generate")
def generate():
    eeg_data = next(simulate_eeg_stream())
    emotion = classify_emotion(eeg_data)
    music_path = generate_music(emotion)
    return {"emotion": emotion, "music": music_path}