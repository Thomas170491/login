import os 
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

from config.database import db,User

class UserRepository: 
    def __init__(self):
        self.db = db

    def get_all(self):
        return self.db.session.query(User).all()

    def get_by_id(self, id):
        return self.db.session.query(User).get(id)

    def create(self, data):
        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=data['password_hash']
        )
        self.db.session.add(new_user)
        self.db.session.commit()
        return new_user

    def update(self, id, data):
        user = self.db.session.query(User).get(id)
        user.username = data['username']
        user.email = data['email']
        user.password_hash = data['password_hash']
        self.db.session.commit()
        return user

    def delete(self, id):
        user = self.db.session.query(User).get(id)
        self.db.session.delete(user)
        self.db.session.commit()
        return user