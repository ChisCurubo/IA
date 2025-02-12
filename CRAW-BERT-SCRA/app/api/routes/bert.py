from fastapi import APIRouter

router = APIRouter()

@router.get("/analyze", summary="Analizar texto con BERT")
async def analyze_text(text: str):
    return {"message": f"Texto analizado con BERT: {text}"}