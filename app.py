import os
import sys
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))


from flask_smorest import Api
from flask import Flask
from dotenv import load_dotenv
from routes.login.login_controller import login


# Load environment variables
load_dotenv()

class APIConfig :
    API_TITLE = 'Login API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/doc'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_SWAGGER_UI_PATH = '/swagger'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    OPENAPI_REDOC_URL = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'
    SECRET_KEY = os.getenv('SECRET_KEY')

server = Flask(__name__) 
server.config.from_object(APIConfig)
api = Api(server)
api.register_blueprint(login)

@server.route('/')
def index():
    return 'Hello World'

if __name__ == "__main__":
  server.run(debug=True, port=5050, host='0.0.0.0')