from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped


Base = declarative_base()

class Pregunta(Base):
    __tablename__ = 'preguntas'

    idpreguntas:Mapped[int] = Column(Integer,primary_key=True)
    texto:Mapped[str] = Column(String(45))
    id_votacion:Mapped[int] = Column(ForeignKey('votacion.idvotacion'))

    def __repr__(self) -> str:
        return f'Pregunta(idpreguntas={self.idpreguntas},texto={self.texto},id_votacion={self.id_votacion})'