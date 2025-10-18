"""Seed script para crear dos municipios de ejemplo.

Ejecutar desde la raíz del proyecto:
  python scripts/seed_municipios.py

El script usa la función get_db_session() para obtener una sesión y crea
dos municipios si no existen (por nombre).
"""
from config.database import get_db_session
from models.territorio_model import Municipio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def seed():
    session = get_db_session()
    try:
        names = [
            ("Neiva", " se encuentra a 1600 msnm y tiene un clima cálido."),
            ("Tello", "se encuentra a 2000 msnm y tiene un clima templado."),
        ]
        created = []
        for nombre, descripcion in names:
            existing = session.query(Municipio).filter(Municipio.nombre == nombre).first()
            if existing:
                logger.info(f"Ya existe: {nombre} (id={existing.id})")
            else:
                m = Municipio(nombre=nombre, descripcion=descripcion)
                session.add(m)
                created.append(nombre)
        if created:
            session.commit()
            logger.info(f"Municipios creados: {created}")
        else:
            logger.info("No se crearon municipios (ya existían)")
    finally:
        session.close()


if __name__ == '__main__':
    seed()
