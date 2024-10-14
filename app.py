from flask_smorest import Api, Blueprint 
from flask import Flask

server = Flask(__name__) 
api = Api(server)

# Create a blueprint
login_bp = Blueprint('login', 'login', url_prefix='/login')

class APIConfig :
    API_TITLE = 'Login API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/doc'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    OPENAPI_REDOC_URL = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'