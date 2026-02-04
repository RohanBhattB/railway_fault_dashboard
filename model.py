import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

def map_condition(label):
    if label == "normal_like":
        return "Good"
    elif label == "misalignment_like":
        return "OK"
    else:
        return "Danger"

def train_and_predict():
    df = pd.read_csv("vibration_fault_classification_random_forest.csv")
    df.fillna(df.mean(numeric_only=True), inplace=True)

    X = df.drop(columns=["path", "label"])
    y = df["label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced_subsample"
    )
    model.fit(X_scaled, y)

    preds = model.predict(X_scaled)

    df["Predicted_Label"] = preds
    df["Condition"] = [map_condition(p) for p in preds]

    return df
