from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class UsuarioResponse():
    idusuario:int
    nombre: str
    username:str 
    correo:str 
    apellidos:str
    descripcion:str

    def __init__(self,idusuario,descripcion,nombre,username,correo,apellidos)->None:
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.username = username
        self.descripcion = descripcion
        self.idusuario = idusuario