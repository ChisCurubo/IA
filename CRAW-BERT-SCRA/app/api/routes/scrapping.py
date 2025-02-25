from typing import List
from fastapi import APIRouter, Request, HTTPException  # Se agregó HTTPException
from fastapi.responses import JSONResponse
from app.services import crawler
from app.services import scrapping, descargar_audio

router = APIRouter()

@router.post("/a")
async def web_scrapping(request: Request):
    data = await request.json()
    print(data)
    # response = crawler("https://www.letras.com/kendrick-lamar")
    return {"message": "funcionando!"}
    # return JSONResponse(content=list(response))

@router.get("/scrapingYutu")
async def web_scrapping1(request: Request):
    try:
        response = scrapping()  # Asegúrate de que scrapping() no requiere argumentos
        # descarga = descargar_audio("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        if not response:
            raise HTTPException(status_code=404, detail="No se encontraron datos")

        print(response)
        
        
        return JSONResponse(content={response})  # No es necesario hacer `list(response)` si ya es una lista

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
