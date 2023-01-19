from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5000


crypt = CryptContext(schemes=['bcrypt'])


def crear_access_token(data:dict ,vencimiento):
    acodificar = data.copy()
    print(acodificar)
    if vencimiento:
        vencimiento = datetime.utcnow() + vencimiento
    else:
        vencimiento = datetime.utcnow() + timedelta(minutes=15)
    acodificar.update({"exp":vencimiento})
    finaljwt = jwt.encode(acodificar,SECRET_KEY,ALGORITHM)
    return finaljwt

def validar_token(token):
     validacion_usuario = jwt.decode(token,SECRET_KEY,ALGORITHM)

def re_validar_token():
    return 'algo'

def crear_contrasena_encriptada(contrasena):
    contrasena_encriptada = crypt.hash(contrasena)
    return contrasena_encriptada

def validar_contrasena(contrasena,contrasena_encriptada):
    return crypt.verify(contrasena,contrasena_encriptada)
    