# 🚀 FASTAPI-ML-APP

A simple machine learning API built using **FastAPI** to serve a trained logistic regression model. Users can upload an Excel file with input data, and the API will return predictions in an Excel file.

---

## 📁 Project Structure

FASTAPI-ML-APP/
├── app/
 └── main.py # FastAPI application (routes & logic)
 └── schema.py # Pydantic models (if needed for validation)
├── model/
 └──logreg_model.pkl # Trained logistic regression model
 └── model_train.py # Script to train & save the model
├── api.log # Optional log file
├── requirements.txt # Python dependencies
