from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import DeclarativeBase,Mapped

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'usuario'

    idusuario: Mapped[int] = Column(Integer,primary_key=True,nullable=True)
    nombre:Mapped[str] = Column(String(45))
    apellidos:Mapped[str] = Column(String(45))
    correo:Mapped[str] = Column(String(45),unique=True)
    password:Mapped[str] = Column(String(45))
    descripcion:Mapped[str] = Column(String)
    username:Mapped[str] = Column(String)


    def __repr__(self) -> str:
        return f'User(id={self.idusuario}, nombre={self.nombre}, apellidos={self.apellidos}, correo={self.correo}, password={self.password}, descripcion={self.descripcion}, username={self.username} )'

    def __init__(self,nombre,apellidos,correo,password,descripcion,username):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.password = password
        self.descripcion = descripcion
        self.username = username
