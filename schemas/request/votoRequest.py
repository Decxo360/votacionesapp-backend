from pydantic import BaseModel


class VotoRequest(BaseModel):

    id_usuario:int
    id_votacion:int
    id_pregunta:int
    id_respuesta:int
    

        