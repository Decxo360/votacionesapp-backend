from dataclasses import dataclass
from .preguntaResponse import PreguntaResponse

@dataclass
class VotacionResponse():

    idusuario:int
    idvotacion:int
    titulo:str
    preguntas:list[PreguntaResponse]

    def __init__(self,idusuario,idvotacion,titulo,preguntas):
        self.idusuario=idusuario
        self.idvotacion=idvotacion
        self.titulo=titulo
        self.preguntas=preguntas

        