from pydantic import BaseModel
import datetime

class SeguidorRequest(BaseModel):

    id_usuario_seguidor:int
    id_usuario_seguido:int

        