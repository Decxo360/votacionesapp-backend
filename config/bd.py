from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

username_conf = os.getenv("DATABASE_USERNAME")
password_conf = os.getenv("DATABASE_PASSWORD")
host_conf = os.getenv("DATABASE_HOST")
dbname_conf = os.getenv("DATABASE_NAME")

print(username_conf)

db ='mysql+mysqlconnector://{username}:{password}@{host}/{dbname}'.format(
    username=username_conf,
    password=password_conf,
    host=host_conf,
    dbname=dbname_conf
)

engine=create_engine(db)

connection = engine.connect()