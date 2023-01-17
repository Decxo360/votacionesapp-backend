from sqlalchemy import Insert,Select
from model.Usuario import User,user_table
from schemas.usuario import Usuario
from config.bd import engine,connection
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter

router = APIRouter(prefix='/usuario')

@router.post("/crear")
async def crearUsuario(user: Usuario):
    user_bd = User(user.apellidos,user.correo,user.descripcion,user.nombre,user.password,user.username)
    print(user)
    stmt =Insert(User).values({"apellidos":user.apellidos,"correo":user.correo,"descripcion":user.descripcion,"nombre":user.nombre,"password":user.password,"username":user.username})
    result = connection.execute(stmt)
    connection.commit()
    retorno = connection.execute(Select(User).where(User.idusuario == result.lastrowid)).first()
    return {
        "usuario": {
            "nombre":retorno.nombre,
            "apellidos":retorno.apellidos,
            "idusuario":retorno.idusuario,
            "username":retorno.username
        },
        "msg":"usuario creado exitosamente"
    }


@router.get("/todos")
async def crearUsuario():
    result = Select(User)
    print(result)

    try:
        return 'algo tambien'
    except:
        return 'algo'
    
    return {
        "resultado" : Session(engine).scalars(result).all()
    }
