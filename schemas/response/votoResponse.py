from dataclasses import dataclass

@dataclass
class VotoResponse():

    id_usuario:int
    id_respuesta:int

    def __init__(self,id_usuario,id_respuesta):
        self.id_usuario=id_usuario
        self.id_respuesta=id_respuesta


        