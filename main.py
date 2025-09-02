from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "Bienvenue sur mon API FastAPI!"}
