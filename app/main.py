from fastapi import FastAPI
from pydantic import BaseModel
from app.agent.agent import run_agent

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Delivery ETA Agent Running"}

@app.post("/predict")
def predict(request: QueryRequest):

    response = run_agent(request.query)

    return {
        "query": request.query,
        "response": response
    }