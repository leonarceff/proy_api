"""
controllers package initialization
"""

from .municipio_controllers import municipio_bp
from .territorio_controllers import territorio_bp
from .users_controllers import users_bp, register_jwt_error_handlers

__all__ = ['municipio_bp', 'territorio_bp', 'users_bp', 'register_jwt_error_handlers']
