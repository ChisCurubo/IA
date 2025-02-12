from fastapi import APIRouter

router = APIRouter()

@router.get("/scrape", summary="Realizar scraping de una página web")
async def scrape_website(url: str):
    return {"message": f"Scraping realizado en: {url}"}