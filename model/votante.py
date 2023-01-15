from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped


Base = declarative_base()

class Votante(Base):
    __tablename__ = 'votante'

    id_votacion:Mapped[int] =Column(ForeignKey("votacion.idvotacion"))
    id_usuario:Mapped[int] = Column(ForeignKey("usuario.idusuario"))
    
    def __repr__(self) -> str:
        return f'Votante(id_votacion={self.id_votacion},id_usuario={self.id_usuario})'