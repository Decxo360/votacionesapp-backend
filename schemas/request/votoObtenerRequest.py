from pydantic import BaseModel


class VotoObtenerRequest(BaseModel):
    id_pregunta:int
    

        