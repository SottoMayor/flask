from flask_seeder import Seeder
from models import UserModel


class SecondUser(Seeder):

    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 2

    
    def run(self):
        user = {
            "name": "John Doe",
            "age": 30,
            "email": "john@doe.com"
        }

        userInstance = UserModel(**user)
        
        self.db.session.add(userInstance)
        self.db.session.commit()