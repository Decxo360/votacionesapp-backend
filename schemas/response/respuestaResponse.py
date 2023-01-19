from dataclasses import dataclass

@dataclass
class Respuesta():

    idrespuesta:int
    texto:str

    def __init__(self,idrespuesta,texto) :
        self.idrespuesta= idrespuesta
        self.texto= texto
