
# Logger para el modelo
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from sqlalchemy.orm import Mapped, mapped_column
from models.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)