import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Importaciones de librerías:
# - sqlalchemy: Proporciona herramientas para trabajar con bases de datos relacionales en Python mediante ORM (Object Relational Mapping).
# - Column, Integer, String, ForeignKey: Permiten definir los tipos de columnas y relaciones entre tablas en los modelos de base de datos.
# - sqlalchemy.orm: Incluye utilidades para la gestión de relaciones y la declaración de modelos.
# - relationship: Permite definir relaciones entre tablas (por ejemplo, uno a muchos).
# - declarative_base: Se utiliza para crear una clase base a partir de la cual se definen los modelos ORM.

from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base

"""
Clase municipio del sistema. Cada instancia de esta clase corresponde a un municipio que tiene asociados territorios con diferente tipo de productos, 
almacenando información relevante como su nombre.
"""
class Municipio(Base):
    __tablename__ = 'municipios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    territorios = relationship('Territorio', back_populates='municipio', cascade='all, delete-orphan')


"""
La clase Territorio representa los productos que generan dentro de los municipios. Cada instancia de esta clase corresponde a un álbum específico, 
almacenando información como el título y la referencia a la banda a la que pertenece. Esta clase está mapeada a la tabla 'albums' en 
la base de datos y permite gestionar los álbumes, así como establecer la relación de pertenencia con una banda mediante una clave foránea.
"""

class Territorio(Base):
    __tablename__ = 'territorios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    producto = Column(String, nullable=False)
    municipio_id = Column(Integer, ForeignKey('municipios.id'), nullable=False)
    municipio = relationship('Municipio', back_populates='territorios')