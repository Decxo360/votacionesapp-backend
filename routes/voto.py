from sqlalchemy import Insert, Select
from model.voto import Voto
from schemas.request import votoRequest,votoObtenerRequest
from schemas.response import responseGenerica,votoResponse
from config.bd import engine, connection
from typing import List
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix='/voto')

@router.post('/crear')
def crearVoto(voto: votoRequest.VotoRequest)->responseGenerica.ResponseGenerica:
    try:
        stmtVoto=Insert(Voto).values({"id_usuario":voto.id_usuario,"id_votacion":voto.id_votacion,"id_pregunta":voto.id_pregunta,"id_respuesta":voto.id_respuesta})
        result = connection.execute(stmtVoto)
        if result.lastrowid == None:
            HTTPException(
            status.HTTP_404_NOT_FOUND,detail="Ha ocurrido un error, porfavor comuniquese con desarrollo"
            )
        connection.commit()
        response = responseGenerica.ResponseGenerica(True,"el voto ha sido ingresado exitosamente")
        return response
    except NameError:
        HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,detail=f'Error {NameError}'
        )
    
    

@router.get("/obtenerRespuestas")
def ObtenerRespuestas(voto:votoObtenerRequest.VotoObtenerRequest)->List[votoResponse.VotoResponse]:
    respuestas = []
    stmt = Select(Voto).where(Voto.id_pregunta == voto.id_pregunta)
    result = connection.execute(stmt).all()
    if result == None:
            HTTPException(
            status.HTTP_404_NOT_FOUND,detail="Ha ocurrido un error, porfavor comuniquese con desarrollo"
        )
    for respuesta in result:
        votoRespuesta = votoResponse.VotoResponse(respuesta.id_usuario,respuesta.id_respuesta)
        respuestas.append(votoRespuesta)
    
    return respuestas
