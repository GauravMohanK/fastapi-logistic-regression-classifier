from fastapi import FastAPI, HTTPException, BackgroundTasks
from app.schema import IrisInput
import numpy as np
import joblib
import logging
import pandas as pd

# Load the model
model = joblib.load("model/logreg_model.pkl")

# Set up logging
logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s - %(message)s")

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Iris classification API is running."}


def log_request(data: IrisInput, prediction: str):
    logging.info(f"Input: {data.model_dump()} | Prediction: {prediction}")


@app.post("/predict")
def predict(input_data: IrisInput, background_tasks: BackgroundTasks):
    try:
        # Map input to match training feature names
        raw_data = input_data.model_dump()
        renamed_data = {
            "sepal length": raw_data["sepal_length"],
            "sepal width": raw_data["sepal_width"],
            "petal length": raw_data["petal_length"],
            "petal width": raw_data["petal_width"]
        }
        df = pd.DataFrame([renamed_data])

        # Predict
        pred_class = model.predict(df)[0]
        proba = model.predict_proba(df)[0]
        species = str(pred_class)

        # Log
        background_tasks.add_task(log_request, input_data, species)

        return {
            "prediction": species,
            "probabilities": {
                "setosa": float(proba[0]),
                "versicolor": float(proba[1]),
                "virginica": float(proba[2])
            }
        }

    except Exception:
        logging.exception("Prediction failed")
        raise HTTPException(status_code=500, detail="Internal server error")
