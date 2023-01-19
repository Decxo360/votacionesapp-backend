from dataclasses import dataclass
from .respuestaResponse import Respuesta

@dataclass
class PreguntaResponse():
    idpreguntas:int
    texto:str
    respuestas:list[Respuesta]

    def __init__ (self,idpreguntas,texto,respuestas):
        self.idpreguntas=idpreguntas
        self.texto=texto
        self.respuestas=respuestas
        