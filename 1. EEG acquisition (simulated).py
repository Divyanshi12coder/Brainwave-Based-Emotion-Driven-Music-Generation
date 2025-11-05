# src/acquisition/eeg_stream.py
import numpy as np
import time

def simulate_eeg_stream():
    while True:
        eeg_data = np.random.rand(1, 128)  # Simulate 128-channel EEG
        yield eeg_data
        time.sleep(1)