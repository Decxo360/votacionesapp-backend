from fastapi import FastAPI
from model.Usuario import User
from sqlalchemy import Select
from sqlalchemy.orm import Session
from routes import usuario
from config.bd import db,engine

app = FastAPI()

session = Session(engine)

app.include_router(usuario.router)
