from models.db import Base
from config.database import engine
from flask import Flask
from config.jwt import JWT_SECRET_KEY, JWT_TOKEN_LOCATION, JWT_ACCESS_TOKEN_EXPIRES, JWT_HEADER_NAME, JWT_HEADER_TYPE
from controllers.territorio_controllers import territorio_bp
from controllers.municipio_controllers import municipio_bp
from controllers.users_controllers import users_bp, register_jwt_error_handlers
from flask_jwt_extended import JWTManager



app = Flask(__name__)

# Configurar JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

jwt = JWTManager(app)

# Registrar el blueprint 
app.register_blueprint(territorio_bp)
app.register_blueprint(municipio_bp)
app.register_blueprint(users_bp)

# Registrar manejadores personalizados de error JWT (si los hay)
register_jwt_error_handlers(app)

if __name__ == "__main__":
    # Crear tablas automáticamente si no existen
    print("Verificando y creando tablas de base de datos si es necesario...")
    Base.metadata.create_all(engine)
    print("Tablas listas.")
    app.run(debug=True)