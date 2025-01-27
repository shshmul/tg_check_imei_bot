# api.py
from flask import Flask, request, jsonify
from services.imei_service import validate_imei, get_imei_info
from config import API_TOKEN

app = Flask(__name__)

@app.route('/api/check-imei', methods=['POST'])

def check_imei():
    token = request.json.get('token')
    imei = request.json.get('imei')

    if token != API_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    if not imei or not validate_imei(imei):
        return jsonify({"error": "Invalid IMEI"}), 400

    imei_info = get_imei_info(imei)
    return jsonify(imei_info)
