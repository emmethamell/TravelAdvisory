from fastapi import FastAPI
from travel_advisories.models.database import *

# run with uvicorn views:app --reload
app = FastAPI()

@app.post("/update-database/travel-advisories/")
async def update_travel_advisories_route():
    update_travel_advisories()
    
@app.get("/travel-advisories/{country}/")
async def get_travel_advisories_route(country: str):
    return get_travel_advisory(country)

