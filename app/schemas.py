from pydantic import BaseModel
from typing import List, Dict


class NormalizeRequest(BaseModel):
    text: str


class NormalizeResponse(BaseModel):
    complaints: List[str] = []
    anamnesis: str = ""
    diagnoses: List[str] = []
    labs: List[str] = []
    procedures: List[str] = []
    recommendations: List[str] = []
    raw_fragments: Dict[str, str] = {}
