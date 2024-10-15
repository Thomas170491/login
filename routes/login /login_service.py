import os
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

import hashlib 
from utils.my_jwt import create_token
from routes.users.users_repository import UserRepository

class LoginService:
    def __init__(self):
        self.user_repository = UserRepository()

    def login(self, data : dict):
        user = self.user_repository.get_by_username(data['username'])

        if user:
            if user.password_hash == hashlib.sha256(data['password'].encode()).hexdigest():
                return create_token(user.id)
            else:
                return 'Invalid password', 400
        else:
            return 'User not found', 404

