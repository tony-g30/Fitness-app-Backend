from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from models import db, User
from config import Config
from auth import register, login
from middleware import requires_auth

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

jwt = JWTManager(app)

with app.app_context():
    db.create_all()

# User Registration
@app.route('/register', methods=['POST'])
def register_user():
    return register()

# User Login
@app.route('/login', methods=['POST'])
def login_user():
    return login()

# Secure Route
@app.route('/secure', methods=['GET'])
@requires_auth
def secure_route():
    return jsonify({'msg': 'This is a secure route'}), 200

if __name__ == '_main_':
    app.run(debug=True)