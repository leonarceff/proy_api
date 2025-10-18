from repositories.municipio_repository import MunicipioRepository
from sqlalchemy.orm import Session
from typing import Optional

class MunicipioService:
    def __init__(self, db_session: Session):
        self.municipio_repo = MunicipioRepository(db_session)

    def listar_municipios(self):
        return self.municipio_repo.get_all()

    def obtener_municipio(self, municipio_id: int):
        return self.municipio_repo.get_by_id(municipio_id)

    def crear_municipio(self, nombre: str, descripcion: Optional[str] = None):
        return self.municipio_repo.create(nombre, descripcion)

    def actualizar_municipio(self, municipio_id: int, nombre: Optional[str] = None, descripcion: Optional[str] = None):
        return self.municipio_repo.update(municipio_id, nombre, descripcion)

    def eliminar_municipio(self, municipio_id: int):
        return self.municipio_repo.delete(municipio_id)
