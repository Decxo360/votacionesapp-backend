from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class LoginResponse():
    idusuario:int 
    nombre: str 
    username:str
    correo:str 
    apellidos:str 
    token:str

    def __init__(self,idusuario,nombre,username,correo,apellidos,token)->None:
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.username = username
        self.idusuario = idusuario
        self.token = token