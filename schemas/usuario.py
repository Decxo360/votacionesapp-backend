from pydantic import BaseModel


class Usuario(BaseModel):
    nombre: str
    username:str
    correo:str
    password:str
    apellidos:str
    descripcion:str

    class Config:
        orm_mode = True