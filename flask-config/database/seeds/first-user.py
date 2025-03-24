from flask_seeder import Seeder
from models import UserModel


class FirstUser(Seeder):

    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 1

    
    def run(self):
        user = {
            "name": "David Sotto",
            "age": 24,
            "email": "david@test.com"
        }

        userInstance = UserModel(**user)
        
        self.db.session.add(userInstance)
        self.db.session.commit()
        

