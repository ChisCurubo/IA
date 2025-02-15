from fastapi import APIRouter,HTTPException
from app.services import crawler
from fastapi.responses import JSONResponse
from app.services.scrappingService import scrapping
router = APIRouter()

@router.get("/")
async def web_crawling(url: str):
    try:
        response = crawler(url)
        print(response)
        if response:
            scrapping(response[0])
        if not response:
            raise HTTPException(status_code=404, detail="No se encontraron datos")
        return JSONResponse(content=list(response))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))