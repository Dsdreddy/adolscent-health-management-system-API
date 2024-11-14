# app/utils/jwt_manager.py
from flask_jwt_extended import JWTManager

def setup_jwt(app):
    jwt = JWTManager(app)
    
    # Define custom error messages, e.g., 401 Unauthorized
    @jwt.unauthorized_loader
    def unauthorized_response(callback):
        return jsonify({"message": "Missing authorization header"}), 401
