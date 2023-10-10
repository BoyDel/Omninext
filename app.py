import json
from flask import Flask, request
from user_service import UserService

app = Flask(__name__)
table = UserService("users")

@app.route('/users', methods=['POST'])
def create_user():
    return table.create_user(json.loads(request.data))

@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    return table.get_user_by_id(user_id)