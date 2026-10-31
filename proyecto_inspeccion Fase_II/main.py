from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("modelo_random_forest.pkl")

class Pieza(BaseModel):
    Measured: float
    Hour: int
    Minute: int

@app.get("/")
def home():
    return {"mensaje":"Sistema de inspección activo"}

@app.post("/predict")
def predict(data:Pieza):
    entrada = pd.DataFrame([{
        "Measured": data.Measured,
        "Hour": data.Hour,
        "Minute": data.Minute
    }])
    pred = model.predict(entrada)
    resultado = "PASS" if pred[0] == 1 else "FAIL"
    return {
        "clasificacion": resultado
    }
