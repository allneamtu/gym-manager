from fastapi import FastAPI
from database import Base, engine
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola desde Gym Manager"}