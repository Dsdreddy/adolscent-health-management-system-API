# app/resources/dashboard.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard():
    # Placeholder response for dashboard data
    data = {
        "sleep_hours": 8,
        "exercise_minutes": 30,
        "water_intake_liters": 2,
        "mood": "happy"
    }
    return jsonify(data), 200

@bp.route('/dashboard/update', methods=['POST'])
@jwt_required()
def update_dashboard():
    data = request.json
    # Logic to update health metrics
    return jsonify({"message": "Health data updated successfully"}), 200
