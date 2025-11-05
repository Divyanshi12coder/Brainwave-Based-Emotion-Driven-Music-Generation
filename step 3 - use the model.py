# src/emotion_model/emotion_classifier.py
import joblib
import numpy as np

model = joblib.load("models/emotion_model.pkl")

def classify_emotion(eeg_data):
    mean = np.mean(eeg_data)
    std = np.std(eeg_data)
    band_power = np.sum(eeg_data[:32])
    features = np.array([[mean, std, band_power]])
    return model.predict(features)[0]