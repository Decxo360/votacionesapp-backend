from sqlalchemy import Insert, Select, Delete, Join
from model.seguidor import Seguidor
from model.Usuario import User
from schemas.request import seguidorRequest, seguidorRequesEliminar,seguidorObtenerSeguidoresReques
from schemas.response import seguidorResponse, usuarioResponseSeguidor
from config.bd import connection
from typing import List
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix='/seguidor')

@router.post('/crear')
def crearSeguidor(seguidor:seguidorRequest.SeguidorRequest)->seguidorResponse.SeguidorResponse:
    stmt = Insert(Seguidor).values({"id_usuario_seguidor":seguidor.id_usuario_seguidor,"id_usuario_seguido":seguidor.id_usuario_seguido})
    result = connection.execute(stmt)
    connection.commit()
    response=connection.execute(Select(Seguidor).where(Seguidor.id_seguidor==result.lastrowid)).first()
    if response == None:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail='Hubo un error, comuniquese con desarrollo'
        )
    print(response.id_seguidor,response.id_usuario_seguidor)
    responseSeguidor = seguidorResponse.SeguidorResponse(response.id_usuario_seguidor,  response.id_usuario_seguido,response.id_seguidor , response.fecha_seguimiento)
    print(responseSeguidor)
    return responseSeguidor

@router.put("/eliminar")
def eliminarSeguirdor(seguidor: seguidorRequesEliminar.SeguidorRequestEliminar):
    stmt= Delete(Seguidor).where(Seguidor.id_seguidor==seguidor.id_seguidor)
    result = connection.execute(stmt)
    connection.commit()
    return{
        "ok":True,
        "msg":"seguidor eliminado exitosamente"
    }

@router.get("/ObtenerSeguidores")
def ObntenerSeguidores(user:seguidorObtenerSeguidoresReques.SeguidorObtenerRequest)->List[usuarioResponseSeguidor.UsuarioSeguidorResponse]:
    usuarioList = []
    stmt = Select(Seguidor).where(Seguidor.id_usuario_seguido == user.idusuario).limit(10)
    result = connection.execute(stmt).all()
    print(result)
    for usuario in result:
        stmt2 = Select(User).where(User.idusuario == usuario.id_usuario_seguidor)
        result2 = connection.execute(stmt2).first()
        newuser = usuarioResponseSeguidor.UsuarioSeguidorResponse(result2.idusuario,result2.nombre,result2.username,result2.apellidos,result2.descripcion)
        usuarioList.append(newuser)
    return usuarioList