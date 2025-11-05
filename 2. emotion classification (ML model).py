# src/emotion_model/emotion_classifier.py
import joblib
import numpy as np

model = joblib.load("models/emotion_model.pkl")

def classify_emotion(eeg_data):
    features = np.mean(eeg_data, axis=1).reshape(1, -1)
    emotion = model.predict(features)[0]
    return emotion