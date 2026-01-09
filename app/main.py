from fastapi import FastAPI
from app.schemas import NormalizeRequest, NormalizeResponse
from app.normalizer import normalize_medical_text

app = FastAPI(
    title="MED-REPORT-NORMALIZER",
    description="Normalization service for medical reports",
    version="0.1.0"
)

@app.post("/normalize", response_model=NormalizeResponse)
def normalize(request: NormalizeRequest):
    return normalize_medical_text(request.text)
