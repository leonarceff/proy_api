import logging
from sqlalchemy.orm import Session
from typing import Optional
from models.territorio_model import Territorio, Municipio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TerritorioRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self):
        logger.info("Obteniendo todos los territorios")
        return self.db.query(Territorio).all()

    def get_by_id(self, territorio_id: int):
        logger.info(f"Buscando territorio por ID: {territorio_id}")
        return self.db.query(Territorio).filter_by(id=territorio_id).first()

    def create(self, nombre: str, producto: str, municipio_id: int):
        logger.info(f"Creando territorio: {nombre}")
        territorio = Territorio(nombre=nombre, producto=producto, municipio_id=municipio_id)
        self.db.add(territorio)
        self.db.commit()
        self.db.refresh(territorio)
        return territorio

    def update(self, territorio_id: int, nombre: Optional[str] = None, producto: Optional[str] = None):
        territorio = self.get_by_id(territorio_id)
        if territorio:
            logger.info(f"Actualizando territorio: {territorio_id}")
            if nombre:
                territorio.nombre = nombre
            if producto:
                territorio.producto = producto
            self.db.commit()
            self.db.refresh(territorio)
        else:
            logger.warning(f"Territorio no encontrado para actualizar: {territorio_id}")
        return territorio

    def delete(self, territorio_id: int):
        territorio = self.get_by_id(territorio_id)
        if territorio:
            logger.info(f"Eliminando territorio: {territorio_id}")
            self.db.delete(territorio)
            self.db.commit()
        else:
            logger.warning(f"Territorio no encontrado para eliminar: {territorio_id}")
        return territorio
