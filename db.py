from sqlalchemy import create_engine #Motor para conectarme con la base de datos
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
import sys
import os
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Forzar codificación UTF-8 en Windows
if os.name == 'nt':  # Solo en Windows
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

url = URL.create( 
    #enlace de conexion
    #Creacion de la url
    drivername="postgresql", 
    username="postgres",
    password="password",
    host="127.0.0.1",
    database="api",
    port=5432
)

#engine = create_engine(url, connect_args= {"options": "-c client_encoding=utf8"}) #Crear un motor para gestionar mi conexion utilizando la (url que creamos)
engine = create_engine(
    url,
    connect_args={"client_encoding": "utf8"},
)
Session = sessionmaker(bind=engine)
session = Session()

try:
    from sqlalchemy import create_engine
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
    with engine.connect() as conn:
        print("Conexión exitosa")
except Exception as e:
    print(f"Error al conectar: {e}")
