from pydantic import BaseModel

class UsuarioRequest(BaseModel):
    nombre: str
    username:str 
    correo:str 
    password:str 
    apellidos:str
    descripcion:str
