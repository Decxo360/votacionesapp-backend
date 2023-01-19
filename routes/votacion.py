from sqlalchemy import Insert, Select, Delete, Join
from model.votacion import Votacion
from model.preguntas import Pregunta
from model.respuesta import Respuesta
from model.preguntas_respuestas import PreguntasRespuestas
from schemas.request import votacionRequest,usuarioVotacionRequest
from schemas.response import votacionResponse,preguntaResponse,respuestaResponse
from config.bd import connection
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix='/votacion')

@router.post("/crear")
def crearVotacion(votacion:votacionRequest.VotacionRequest):
    print(votacion)
    stmtvotacion = Insert(Votacion).values({"id_usuario":votacion.idusuario,"titulo":votacion.titulo})
    resultVotacion = connection.execute(stmtvotacion)
    for pregunta in votacion.preguntas:
        stmtpregunta = Insert(Pregunta).values({"texto":pregunta.texto,"id_votacion":resultVotacion.lastrowid})
        resultPregunta = connection.execute(stmtpregunta)
        for respuesta in pregunta.respuestas:
            stmtrespuesta = Insert(Respuesta).values({"texto":respuesta.texto})
            resultRespuesta = connection.execute(stmtrespuesta)
            stmtPreguntaRespuesta = Insert(PreguntasRespuestas).values({"id_respuesta":resultRespuesta.lastrowid,"id_pregunta":resultPregunta.lastrowid})
            connection.execute(stmtPreguntaRespuesta)
    connection.commit()
    return {
        "ok":True,
        "msg":"La votacion ha sido creada con exito"
    }

@router.get('/ObtenerVotaciones')
def obtenerVotaciones(user:usuarioVotacionRequest.UsuarioVotacionRequest)->votacionResponse.VotacionResponse:
    stmtVotacion = Select(Votacion).where(Votacion.id_usuario==user.idusuario)
    resultVotacion = connection.execute(stmtVotacion).all()
    for votacion in resultVotacion:
        preguntas=[]
        stmtPregunta = Select(Pregunta).where(Pregunta.id_votacion == votacion.idvotacion)
        resultPregunta = connection.execute(stmtPregunta).all()
        votacionR = votacionResponse.VotacionResponse(votacion.id_usuario,votacion.idvotacion,votacion.titulo,preguntas)
        for pregunta in resultPregunta:
            respuestas=[]
            stmtRespuesta = Select(PreguntasRespuestas).where(PreguntasRespuestas.id_pregunta == pregunta.idpreguntas)
            resulResuesta = connection.execute(stmtRespuesta).all()
            preguntaR = preguntaResponse.PreguntaResponse(pregunta.idpreguntas,pregunta.texto,respuestas)
            preguntas.append(preguntaR)
            print(resulResuesta)
            for respuesta in resulResuesta:
                stmtTexto = Select(Respuesta).where(Respuesta.idrespuesta == respuesta.id_respuesta)
                resultTexto = connection.execute(stmtTexto).first()
                respuestaR = respuestaResponse.Respuesta(resultTexto.idrespuesta,resultTexto.texto)
                respuestas.append(respuestaR)
    return votacionR