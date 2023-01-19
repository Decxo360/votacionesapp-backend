from pydantic import BaseModel
import datetime

class SeguidorObtenerRequest(BaseModel):
    idusuario:int
