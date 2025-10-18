import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SASession
from sqlalchemy.exc import OperationalError
from models.db import Base  # Aquí defines Base = declarative_base() en models/db.py

logging.basicConfig(level=logging.INFO)

MYSQL_URI = os.getenv('MYSQL_URI')  # Asegúrate que esté en .env o variable de entorno
SQLITE_URI = 'sqlite:///territorios_local.db'  # fallback local

def get_engine():
    if MYSQL_URI:
        try:
            engine = create_engine(MYSQL_URI, echo=True)
            conn = engine.connect()
            conn.close()
            logging.info('Conexión a MySQL exitosa.')
            return engine
        except OperationalError:
            logging.warning('No se pudo conectar a MySQL. Usando SQLite local.')
    engine = create_engine(SQLITE_URI, echo=True)
    return engine

engine = get_engine()
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)  # type: ignore[attr-defined]

def get_db_session() -> SASession:
    return SessionLocal()
