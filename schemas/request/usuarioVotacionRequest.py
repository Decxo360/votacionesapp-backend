from pydantic import BaseModel

class UsuarioVotacionRequest(BaseModel):
    idusuario: int
