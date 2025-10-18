import logging
from sqlalchemy.orm import Session
from typing import Optional
from models.territorio_model import Municipio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MunicipioRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self):
        logger.info("Obteniendo todos los municipios")
        return self.db.query(Municipio).all()

    def get_by_id(self, municipio_id: int):
        logger.info(f"Buscando municipio por ID: {municipio_id}")
        return self.db.query(Municipio).filter_by(id=municipio_id).first()

    def create(self, nombre: str, descripcion: Optional[str] = None):
        logger.info(f"Creando municipio: {nombre}")
        municipio = Municipio(nombre=nombre, descripcion=descripcion)
        self.db.add(municipio)
        self.db.commit()
        self.db.refresh(municipio)
        return municipio

    def update(self, municipio_id: int, nombre: Optional[str] = None, descripcion: Optional[str] = None):
        municipio = self.get_by_id(municipio_id)
        if municipio:
            logger.info(f"Actualizando municipio: {municipio_id}")
            if nombre:
                municipio.nombre = nombre
            if descripcion:
                municipio.descripcion = descripcion
            self.db.commit()
            self.db.refresh(municipio)
        else:
            logger.warning(f"Municipio no encontrado para actualizar: {municipio_id}")
        return municipio

    def delete(self, municipio_id: int):
        municipio = self.get_by_id(municipio_id)
        if municipio:
            logger.info(f"Eliminando municipio: {municipio_id}")
            self.db.delete(municipio)
            self.db.commit()
        else:
            logger.warning(f"Municipio no encontrado para eliminar: {municipio_id}")
        return municipio
