from app.ml.predict import predict_delay
from app.agent.prompts import generate_explanation

def predict_eta(query: str):

    query = query.lower()

    traffic = 2
    weather = 2
    distance = 10
    condition = "normal"

    if "rain" in query:
        weather = 8
        condition = "rain"

    if "traffic" in query:
        traffic = 8
        condition = "traffic"

    if "vehicle" in query:
        traffic = 7
        distance = 18
        condition = "vehicle issue"

    if "festival" in query:
        traffic = 9
        weather = 4
        condition = "festival rush"

    delay = predict_delay(traffic, weather, distance)

    explanation = generate_explanation(condition, delay)

    return {
        "eta": f"{delay} hour delay",
        "reason": explanation
    }