# app/resources/symptoms.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('symptoms', __name__)

@bp.route('/symptoms/check', methods=['POST'])
@jwt_required()
def check_symptoms():
    data = request.json.get("symptoms", [])
    # Mock response for symptom advice
    advice = "Consider resting and drinking water" if "fever" in data else "Contact a doctor"
    return jsonify({"advice": advice}), 200
