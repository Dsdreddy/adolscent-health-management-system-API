# app/resources/mental_health.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('mental_health', __name__)

@bp.route('/mentalhealth/resources', methods=['GET'])
@jwt_required()
def get_resources():
    # Example response for mental health resources
    resources = [{"title": "Mindfulness Tips", "type": "article"}, {"title": "Stress Relief", "type": "video"}]
    return jsonify(resources), 200

@bp.route('/mentalhealth/self-assessment', methods=['POST'])
@jwt_required()
def self_assessment():
    data = request.json
    # Mock response for self-assessment processing
    return jsonify({"message": "Self-assessment submitted successfully"}), 200

@bp.route('/mentalhealth/book-session', methods=['POST'])
@jwt_required()
def book_session():
    data = request.json
    # Example response for booking a session
    return jsonify({"message": "Appointment booked with therapist"}), 200
