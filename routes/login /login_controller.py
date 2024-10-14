from flask_smorest import Blueprint
from flask import request, jsonify

from dto.request.login_request import LoginRequest
from dto.response.login_response import LoginResponse   


# Create a blueprint
login_bp = Blueprint('login', 'login', url_prefix='/login')


