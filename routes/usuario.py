from sqlalchemy import Insert
from model.Usuario import User
from config.bd import connection
import json
from fastapi import APIRouter

router = APIRouter(prefix="/usuario")

@router.post("/crear")
def crearUsuario(nombre: str,correo: str,password:str,username:str,apellidos:str,descripcion:str):
    result = connection.execute(
        Insert(User).values(nombre,correo,password,username,apellidos,descripcion).returning(User.nombre)
    )
    return 'a'
