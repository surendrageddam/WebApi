from fastapi import FastAPI
from Scraper.scraping import Scraper


app = FastAPI()


@app.get("/")
async def run(url: str):
    return {"status": 200}

@app.get("/get")
async def run(url: str):
    return{"price": Scraper().scrape(url)}
