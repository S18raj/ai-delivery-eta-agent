from app.agent.tools import predict_eta
from app.agent.cache import get_from_cache, save_to_cache

def run_agent(query: str):

    # 1. Check cache
    cached = get_from_cache(query)
    if cached:
        return f"(cached)\n{cached}"

    # 2. Generate fresh response
    prediction = predict_eta(query)

    response = f"""
Predicted ETA: {prediction['eta']}

Explanation:
{prediction['reason']}
"""

    # 3. Save to cache
    save_to_cache(query, response)

    return response