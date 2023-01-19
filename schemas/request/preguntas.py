from pydantic import BaseModel
from .respuesta import Respuesta

class Pregunta(BaseModel):

    texto:str
    respuestas:list[Respuesta]

        