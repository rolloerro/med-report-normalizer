def normalize_medical_text(text: str) -> dict:
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    return {
        "complaints": [l for l in lines if "жалоб" in l.lower()],
        "anamnesis": " ".join(lines[:2]) if lines else "",
        "diagnoses": [l for l in lines if "диагноз" in l.lower()],
        "labs": [l for l in lines if "анализ" in l.lower()],
        "procedures": [l for l in lines if "проведен" in l.lower()],
        "recommendations": [l for l in lines if "рекоменд" in l.lower()],
        "raw_fragments": {
            f"line_{i}": line for i, line in enumerate(lines)
        }
    }
