from repositories.territorio_repository import TerritorioRepository
from repositories.municipio_repository import MunicipioRepository
from sqlalchemy.orm import Session
from typing import Optional

class TerritorioService:
    def __init__(self, db_session: Session):
        self.territorio_repo = TerritorioRepository(db_session)
        self.municipio_repo = MunicipioRepository(db_session)

    def listar_territorios(self):
        return self.territorio_repo.get_all()

    def obtener_territorio(self, territorio_id: int):
        return self.territorio_repo.get_by_id(territorio_id)

    def crear_territorio(self, nombre: str, producto: str, municipio_id: int):
        municipio = self.municipio_repo.get_by_id(municipio_id)
        if not municipio:
            raise ValueError("Municipio no encontrado")
        return self.territorio_repo.create(nombre, producto, municipio_id)

    def actualizar_territorio(self, territorio_id: int, nombre: Optional[str] = None, producto: Optional[str] = None):
        return self.territorio_repo.update(territorio_id, nombre, producto)

    def eliminar_territorio(self, territorio_id: int):
        return self.territorio_repo.delete(territorio_id)
