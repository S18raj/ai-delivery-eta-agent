import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    "traffic": [1, 5, 8, 3, 7],
    "weather": [1, 7, 9, 2, 8],
    "distance": [5, 15, 25, 10, 20],
    "delay_hours": [1, 3, 6, 2, 5]
}

df = pd.DataFrame(data)

X = df[["traffic", "weather", "distance"]]
y = df["delay_hours"]

model = LinearRegression()
model.fit(X, y)

with open("eta_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained")