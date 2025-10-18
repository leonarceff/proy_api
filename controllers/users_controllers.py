import logging
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from config.database import get_db_session
from services.users_services import UsersService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

users_bp = Blueprint('users_bp', __name__)
service = UsersService(get_db_session())


@users_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'username and password required'}), 400

    user = service.authenticate_user(username, password)
    if not user:
        return jsonify({'error': 'invalid credentials'}), 401

    access_token = create_access_token(identity={'id': user.id, 'username': user.username})
    return jsonify({'access_token': access_token}), 200


def register_jwt_error_handlers(app):
    # Minimal JWT error handlers so imports in main.py work even if app doesn't need custom handling
    from flask_jwt_extended.exceptions import NoAuthorizationError
    @app.errorhandler(NoAuthorizationError)
    def handle_no_auth(e):
        return jsonify({'error': 'authorization required'}), 401
