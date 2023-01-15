from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped


Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'

    idusuario: Mapped[int] = Column(Integer,primary_key=True)
    nombre:Mapped[str] = Column(String(45))
    apellidos:Mapped[str] = Column(String(45))
    correo:Mapped[str] = Column(String(45),unique=True)
    password:Mapped[str] = Column(String(45))
    descripcion:Mapped[str] = Column(String)

    def __repr__(self) -> str:
        return f'User(id={self.idusuario}, nombre={self.nombre}, apellidos={self.apellidos}, correo={self.correo}, password={self.password}, descripcion={self.descripcion} )'
