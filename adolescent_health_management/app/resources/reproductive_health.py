# app/resources/reproductive_health.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

bp = Blueprint('reproductive_health', __name__)

@bp.route('/reproductive-health/articles', methods=['GET'])
@jwt_required()
def get_articles():
    articles = [{"title": "Understanding Puberty", "content": "Details about puberty."}]
    return jsonify(articles), 200

@bp.route('/reproductive-health/menstrual-tracker', methods=['POST'])
@jwt_required()
def menstrual_tracker():
    data = request.json
    # Placeholder response for menstrual data tracking
    return jsonify({"message": "Menstrual data updated"}), 200

@bp.route('/reproductive-health/ask-question', methods=['POST'])
@jwt_required()
def ask_question():
    data = request.json
    # Mock response for submitting a question
    return jsonify({"message": "Your question has been submitted"}), 200
