from flask_smorest import Blueprint
from flask import request, jsonify

from dto.request.login_request import LoginRequest
from dto.response.login_response import LoginResponse   

from login_service import LoginService 


# Create a blueprint
login = Blueprint('login', 'login', url_prefix='/login')

login_service = LoginService()

@login.route("/", methods = ['POST'])
@login.arguments(LoginRequest)
@login.response(status_code=200,schema=LoginResponse)
@login.response(status_code=401)
def login_func(login_req : dict):
    try :
        return {"token ": login_service.login()}, 200
    except Exception as e :
        return {'error' : 'Wrong credentials' }, 401


