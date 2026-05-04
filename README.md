# AI Delivery ETA Agent

An AI-powered delivery ETA prediction and explanation system built using machine learning, FastAPI, caching, and LLM-generated delivery delay explanations.

## Overview

This project predicts delivery delays based on operational conditions such as:

- Traffic congestion
- Weather conditions
- Vehicle issues
- Festival season load

It combines ML prediction with natural-language explanation generation.

---

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Groq LLM API
- Local caching
- HTML frontend

---

## Architecture

User Query  
↓  
FastAPI API  
↓  
Query Parsing  
↓  
ML Prediction  
↓  
Cache Check  
↓  
LLM Explanation Generation  
↓  
Response

---

## Features

- ETA delay prediction
- Natural language delay explanations
- Caching for repeated requests
- Condition-based feature engineering
- REST API endpoints

---

## Example Query

**Input**

heavy traffic in city

**Output**

Predicted ETA: 3.5 hour delay

Explanation:
Due to traffic congestion, delivery is delayed by approximately 3.5 hours.

---

## Run Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run backend

```bash
python -m uvicorn app.main:app --reload
```

---

## Future Improvements

- Real logistics dataset integration
- Advanced ML models
- Database logging
- Dashboard analytics
