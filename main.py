from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel,List

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

class Cars(BaseModel):
    id: str
    brand: str
    model: str
    characteristics: dict = []

cars_db:List = []
@app.post("/cars",status_code=201)
async def add_cars(cars:List[Cars]):
    cars_db.extends(cars)
    return cars_db



@app.get("/cars")
async def get_all_cars():
    return cars_db

@app.get("/cars/{id}")
async def get_cars_by_id(find_id:int):
    for()

