from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
import datetime


Base = declarative_base()

class Seguidor(Base):
    __tablename__ = 'seguidor'

    id_seguidor:Mapped[int] = Column(Integer,primary_key=True)
    id_usuario_seguidor:Mapped[int] = Column(ForeignKey("usuario.idusuario"),autoincrement=False)
    id_usuario_seguido:Mapped[int] = Column(ForeignKey("usuario.idusuario"), autoincrement=False)
    fecha_seguimiento:Mapped[str] = Column(default=datetime.datetime.now)

    def __repr__(self) -> str:
        return f'Seguidor(id_seguidor={self.id_seguidor},id_usuario_seguidor={self.id_usuario_seguidor},id_usuario_seguido={self.id_usuario_seguido},fecha_seguimiento={self.fecha_seguimiento})'

    