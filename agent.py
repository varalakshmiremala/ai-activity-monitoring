import joblib
import pandas as pd
from datetime import datetime

class ActivityAgent:
    def __init__(self):
        self.model = joblib.load("model.pkl")

    def predict(self, data):
        return self.model.predict([data])[0]

    def save_log(self, data, result):
        row = data + [result, str(datetime.now())]

        df = pd.DataFrame([row], columns=[
            "f1", "f2", "f3", "activity", "time"
        ])

        try:
            old = pd.read_csv("logs.csv")
            df = pd.concat([old, df], ignore_index=True)
        except:
            pass

        df.to_csv("logs.csv", index=False)