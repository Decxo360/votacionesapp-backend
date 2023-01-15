from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped


Base = declarative_base()

class PreguntasResuestas(Base):
    __tablename__ = 'preguntas_respuestas'

    id_pregunta:Mapped[int] = Column(ForeignKey('preguntas.idpreguntas'));
    id_respuesta:Mapped[int] = Column(ForeignKey('respuesta.respuesta'));

    def __repr__(self) -> str:
        return f'PreguntasRespuestas(id_pregunta={self.id_pregunta},id_respuesta={self.id_respuesta})'

