from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base
from db import engine
from sqlalchemy import event
import traceback
import sys
import os

# Forzar codificación UTF-8 en Windows
if os.name == 'nt':  # Solo en Windows
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

Base = declarative_base()

class Todo(Base):
    __tablename__="todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(255 )) #text = Column(String(collation="utf8_general_ci"))
    is_done = Column(Boolean, default=False)

@event.listens_for(engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    print("Ejecutando consulta:", statement)

try:
    Base.metadata.create_all(engine)
    print("Tablas creadas con éxito.")
except UnicodeDecodeError as e:
    print(f"Error de Unicode: {e}")
    traceback.print_exc()  # Muestra la traza completa
except Exception as e:
    print(f"Error al crear tablas: {e}")
    traceback.print_exc()  # Muestra la traza completa

"""
try:
    with engine.connect() as connection:
        connection.execute(
            """ """CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, text_column VARCHAR(255))""" """
        ) 
    print("Tabla creada manualmente correctamente.")
except Exception as e:
    print(f"Error al crear la tabla manualmente: {e}")
"""