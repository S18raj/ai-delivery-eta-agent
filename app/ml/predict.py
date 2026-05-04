import pickle
import pandas as pd

with open("eta_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_delay(traffic, weather, distance):

    data = pd.DataFrame([{
        "traffic": traffic,
        "weather": weather,
        "distance": distance
    }])

    prediction = model.predict(data)

    return round(float(prediction[0]), 2)