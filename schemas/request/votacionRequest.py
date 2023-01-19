from pydantic import BaseModel
from .preguntas import Pregunta

class VotacionRequest(BaseModel):

    idusuario:int
    titulo:str
    preguntas:list[Pregunta]
 

        