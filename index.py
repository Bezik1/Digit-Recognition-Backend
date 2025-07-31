from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas.PixelData import PixelData
import crud

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(data: PixelData):
    try:
        probability, digit = crud.predict(data)

        return {
            "status": 200,
            "message": "Prediction evaluated succesfully!",
            "data": {
                "probability": probability,
                "digit": digit,
            },
        }
    except Exception:
        return {
            "status": 500,
            "message": "An error occured, while evaluating model predictions!",
        }
