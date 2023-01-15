from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped


Base = declarative_base()

class Votacion(Base):
    __tablename__ = 'votacion'

    idvotacion:Mapped[int] = Column(Integer,primary_key=True)
    id_usuario:Mapped[int] = Column(ForeignKey("usuario.idvotacion"))

    def __repr__(self) -> str:
        return f'Votacion(idvotacion={self.idvotacion},id_usuario={self.id_usuario})'
