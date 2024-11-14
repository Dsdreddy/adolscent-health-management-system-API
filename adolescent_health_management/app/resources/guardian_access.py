# app/resources/guardian_access.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('guardian_access', __name__)

@bp.route('/guardian/access-request', methods=['POST'])
@jwt_required()
def request_access():
    data = request.json
    # Placeholder response for access request
    return jsonify({"message": "Access request submitted"}), 200

@bp.route('/guardian/view-data', methods=['GET'])
@jwt_required()
def view_data():
    # Mock data accessible by guardian
    data = {"health_data": {"sleep_hours": 7, "exercise_minutes": 45}}
    return jsonify(data), 200
