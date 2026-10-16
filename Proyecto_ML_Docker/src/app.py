from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="ML Prediction API", description="FastAPI service that loads a trained regression model and returns predictions.")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "model.pkl")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model file not found at {MODEL_PATH}. Train the model first.")

model = joblib.load(MODEL_PATH)

class PredictRequest(BaseModel):
    features: list[float]

class PredictResponse(BaseModel):
    prediction: float

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    if len(req.features) != model.coef_.shape[0]:
        raise HTTPException(status_code=400, detail="Feature vector size does not match model.")
    X = np.array(req.features).reshape(1, -1)
    pred = model.predict(X)[0]
    return PredictResponse(prediction=float(pred))
