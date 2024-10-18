from flask import Flask,jsonify
from auth import register, login
from middleware import requires_auth

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
    return register()

@app.route('/login', methods=['POST'])
def login_user():
    return login()

@app.route('/secure', methods=['GET'])
@requires_auth
def secure_route():
    return jsonify({'msg': 'This is a secure route'}), 200