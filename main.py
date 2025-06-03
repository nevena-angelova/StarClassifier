from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI(title="Star Classifier API")

model = joblib.load("model/star_model.pkl")

CLASS_NAMES = {
    0: "Brown Dwarf",
    1: "Red Dwarf",
    2: "White Dwarf",
    3: "Main Sequence",
    4: "Supergiant",
    5: "Hypergiant"
}

class StarInput(BaseModel):
    temperature: float = Field(..., gt=0)
    luminosity: float = Field(..., gt=0)
    radius: float = Field(..., gt=0)
    absolute_magnitude: float
    spectral_class: str = Field(..., pattern="^[OBAFGKM]$")


@app.post("/predict")
def predict_star_type(star: StarInput):
    try:
        X = pd.DataFrame([{
            "Temperature": star.temperature,
            "L": star.luminosity,
            "R": star.radius,
            "A_M": star.absolute_magnitude,
            "Spectral_Class": star.spectral_class
        }])

        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0][pred]

        return {
            "predicted_type": CLASS_NAMES[pred],
            "confidence": round(float(prob), 3)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))