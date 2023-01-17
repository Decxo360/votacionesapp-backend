from sqlalchemy import Insert, Select
from model.Usuario import User
from schemas.request import loginRequest, usuarioRequest
from schemas.response import usuario, login
from config.bd import engine, connection
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix='/usuario')


@router.post("/crear")
async def crearUsuario(user: usuarioRequest.UsuarioRequest) -> usuario.UsuarioResponse:
    stmt = Insert(User).values({"apellidos": user.apellidos, "correo": user.correo, "descripcion": user.descripcion,
                                "nombre": user.nombre, "password": user.password, "username": user.username})
    result = connection.execute(stmt)
    connection.commit()
    retorno = connection.execute(Select(User).where(
        User.idusuario == result.lastrowid)).first()
    if retorno.idusuario == None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Ha ocurrido algun error desde la base de datos'
        )
    response = usuarioRequest.UsuarioResponse(
        result.idusuario, result.nombre, result.username, result.correo, result.apellidos, result.descripcion)

    return response


@router.get("/todos")
async def obtenerTodosUsuarios():
    result = Select(User)
    print(result)
    return {
        "resultado": Session(engine).scalars(result).all()
    }


@router.get("/login")
def LogIn(login: loginRequest.LoginRequest) -> login.LoginResponse:
    stmt = Select(User).where(User.correo == login.correo,
                              User.password == login.password)
    result = connection.execute(stmt).first()
    if result == None:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail='No existe usuario con tales parametros'
        )
    usuario = login.LoginResponse(
        result.idusuario, result.nombre, result.username, result.correo, result.apellidos)
    return usuario


@router.get("/{idusuario}")
def obtenerUnUsuario(idusuario: int) -> usuario.UsuarioResponse:
    stmt = Select(User).where(User.idusuario == idusuario).limit(10)
    result = connection.execute(stmt).first()
    if result == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='El usuario indicado no existe'
        )
    usuario = usuario.Usuario(result.idusuario, result.nombre,
                              result.username, result.correo, result.descripcion)
    return usuario
