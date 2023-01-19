from dataclasses import dataclass
from datetime import datetime
from typing import Union

@dataclass
class SeguidorResponse():

    id_seguidor:int
    id_usuario_seguidor:int
    id_usuario_seguido:int
    fecha_seguimiento: Union[datetime,None]

    def __init__(self,id_usuario_seguidor,id_usuario_seguido,id_seguidor,fecha_seguimiento):
        self.id_usuario_seguidor = id_usuario_seguidor
        self.id_usuario_seguido = id_usuario_seguido
        self.id_seguidor=id_seguidor
        self.fecha_seguimiento=fecha_seguimiento
        
        