# src/emotion_model/generate_dataset.py
import numpy as np
import pandas as pd

emotions = ["happy", "sad", "calm", "angry", "focused"]
samples_per_class = 100
features = []

for emotion in emotions:
    for _ in range(samples_per_class):
        signal = np.random.rand(128)
        mean = np.mean(signal)
        std = np.std(signal)
        band_power = np.sum(signal[:32])  # Simulated alpha band
        features.append([mean, std, band_power, emotion])

df = pd.DataFrame(features, columns=["mean", "std", "band_power", "label"])
df.to_csv("data/eeg_emotion_dataset.csv", index=False)