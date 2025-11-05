# src/emotion_model/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("data/eeg_emotion_dataset.csv")
X = df[["mean", "std", "band_power"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SVC(kernel="rbf", probability=True)
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "models/emotion_model.pkl")