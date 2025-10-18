import logging
from config.database import get_db_session
from models.territorio_model import Municipio, Territorio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_municipio(session):
    neiva = session.query(Municipio).filter(Municipio.nombre == "Neiva").first()
    if not neiva:
        neiva = Municipio(nombre="Neiva", descripcion="Municipio ubicado a 1600 msnm con clima cálido.")
        session.add(neiva)
        session.commit()
        logger.info("Municipio 'Neiva' creado.")
    else:
        logger.info("Municipio 'Neiva' ya existe.")
    return neiva

def seed_territorios(session, municipio):
    territorios_data = [
        ("Territorio Norte", "Café"),
        ("Territorio Sur", "Cacao"),
    ]

    for nombre, producto in territorios_data:
        existente = session.query(Territorio).filter(
            Territorio.nombre == nombre,
            Territorio.municipio_id == municipio.id
        ).first()

        if existente:
            logger.info(f"Ya existe el territorio: {nombre}")
            continue

        t = Territorio(nombre=nombre, producto=producto, municipio_id=municipio.id)
        session.add(t)
        logger.info(f"Territorio creado: {nombre} (Producto: {producto})")

    session.commit()
    logger.info("Territorios insertados correctamente.")

def seed_all():
    session = get_db_session()
    try:
        municipio = seed_municipio(session)
        seed_territorios(session, municipio)
    finally:
        session.close()

if __name__ == "__main__":
    seed_all()
