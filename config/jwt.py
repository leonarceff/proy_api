import os
from datetime import timedelta

# Valores por defecto para JWT. Pueden ser sobreescritos con variables de entorno.
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'change-me-in-production')
JWT_TOKEN_LOCATION = os.getenv('JWT_TOKEN_LOCATION', 'headers')
# Duración por defecto del access token: 15 minutos
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES_MINUTES', '15')))
JWT_HEADER_NAME = os.getenv('JWT_HEADER_NAME', 'Authorization')
JWT_HEADER_TYPE = os.getenv('JWT_HEADER_TYPE', 'Bearer')

__all__ = [
    'JWT_SECRET_KEY',
    'JWT_TOKEN_LOCATION',
    'JWT_ACCESS_TOKEN_EXPIRES',
    'JWT_HEADER_NAME',
    'JWT_HEADER_TYPE',
]
