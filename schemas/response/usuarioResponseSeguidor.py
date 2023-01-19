from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class UsuarioSeguidorResponse():
    idusuario:int
    nombre: str
    username:str 
    apellidos:str
    descripcion:str

    def __init__(self,idusuario,nombre,username,apellidos,descripcion)->None:
        self.idusuario = idusuario
        self.nombre = nombre
        self.username = username
        self.apellidos = apellidos
        self.descripcion = descripcion