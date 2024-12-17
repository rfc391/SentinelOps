from flask import Flask, request, jsonify, render_template
from src.auth import AuthManager
from src.core import SentinelOps
from src.visualization import plot_data

app = Flask(__name__)
auth_manager = AuthManager()
ops = SentinelOps()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    token = auth_manager.authenticate(data.get("username"), data.get("password"))
    if token:
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/api/data', methods=['GET', 'POST'])
def manage_data():
    token = request.headers.get("Authorization")
    payload = auth_manager.verify_token(token)
    if isinstance(payload, str):
        return jsonify({"error": payload}), 401

    if request.method == 'POST':
        data = request.json
        ops.add_data(data)
        return jsonify({"message": "Data added successfully"}), 201
    return jsonify(ops.get_data())
