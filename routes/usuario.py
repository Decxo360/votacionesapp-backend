from sqlalchemy import Insert, Select
from model.Usuario import User
from middleware.auth import crear_contrasena_encriptada,validar_contrasena,crear_access_token
from schemas.request import loginRequest, usuarioRequest
from schemas.response import usuario, loginResponse
from config.bd import engine, connection
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix='/usuario')


@router.post("/crear")
async def crearUsuario(user: usuarioRequest.UsuarioRequest) -> usuario.UsuarioResponse:
    passEncrypt=crear_contrasena_encriptada(user.password)
    stmt = Insert(User).values({"apellidos": user.apellidos, "correo": user.correo, "descripcion": user.descripcion,
                                "nombre": user.nombre, "password": passEncrypt, "username": user.username})
    result = connection.execute(stmt)
    connection.commit()
    retorno = connection.execute(Select(User).where(
        User.idusuario == result.lastrowid)).first()
    if retorno.idusuario == None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Ha ocurrido algun error desde la base de datos'
        )
    response = usuario.UsuarioResponse(
        retorno.idusuario, retorno.descripcion, retorno.nombre, retorno.username, retorno.correo, retorno.apellidos)
    return response


@router.get("/todos")
async def obtenerTodosUsuarios():
    result = Select(User)
    print(result)
    return {
        "resultado": Session(engine).scalars(result).all()
    }


@router.get("/login")
def LogIn(login: loginRequest.LoginRequest) -> loginResponse.LoginResponse:
    stmt = Select(User).where(User.correo == login.correo)
    result = connection.execute(stmt).first() 
    if result == None:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, detail='No existe usuario con tales parametros'
        )
    if not validar_contrasena(login.password,result.password):
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Problemas con los datos'
        ) 
    else:
        expires=timedelta(minutes=100)
        token=crear_access_token(data={"username":result.username},vencimiento=expires)
        usuario = loginResponse.LoginResponse(
        result.idusuario, result.nombre, result.username, result.correo, result.apellidos,token)
  
    
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
