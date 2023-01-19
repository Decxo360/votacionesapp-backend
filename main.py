from fastapi import FastAPI
from sqlalchemy.orm import Session
from routes import usuario,seguidor,votacion,voto
from config.bd import engine

app = FastAPI()

session = Session(engine)

app.include_router(usuario.router)
app.include_router(seguidor.router)
app.include_router(votacion.router)
app.include_router(voto.router)
