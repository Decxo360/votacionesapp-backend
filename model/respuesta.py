from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped


Base = declarative_base()

class Respuesta(Base):
    __tablename__ = 'respuesta'

    idrespuesta:Mapped[int] = Column(Integer,primary_key=True)
    texto:Mapped[str] = Column(String)

    def __repr__(self) -> str:
        return f'Respuesta(idrespuesta={self.idrespuesta},texto={self.texto})'