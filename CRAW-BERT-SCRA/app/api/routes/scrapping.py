from typing import List
from fastapi import APIRouter , Request
from app.services import crawler
from fastapi.responses import JSONResponse
router = APIRouter()

@router.post("/")
async def web_scrapping(request: Request):
    data = await request.json()
    print(data)
    # response = crawler("https://www.letras.com/kendrick-lamar")
    return {"message": "funcionando!"}
    # return JSONResponse(content=list(response))