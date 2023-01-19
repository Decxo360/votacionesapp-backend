from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped


Base = declarative_base()

class Voto(Base):
    __tablename__ = 'voto'

    idvoto:Mapped[int] = Column(primary_key=True)
    id_usuario:Mapped[int] = Column(ForeignKey("usuario.idrespuesta"))
    id_votacion:Mapped[int] = Column(ForeignKey("votacion.idrespuesta"))
    id_pregunta:Mapped[int] = Column(ForeignKey("preguntas.idrespuesta"))
    id_respuesta:Mapped[int] = Column(ForeignKey("respuesta.idrespuesta"))
 
    def __repr__(self) -> str:
        return f'Voto(id_usuario={self.id_usuario},id_votacion={self.id_votacion},id_pregunta={self.id_pregunta},id_respuesta={self.id_respuesta})'
