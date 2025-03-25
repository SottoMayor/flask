from flask_smorest import Blueprint
from flask.views import MethodView

blp = Blueprint('user', __name__, url_prefix="/", description='user\'s blueprint.')

@blp.route('/')
class User(MethodView):
    def get(self):
        return { "message": "Hello World" }
    
@blp.route('/<string:id>')
class User(MethodView):
    def get(self, id):
        return { "message": "Hello World", "id": id }
    
@blp.route('/test')
class User(MethodView):
    def get(self):
        return { "message": "test" }
    
@blp.route('/test/<string:id>')
class User(MethodView):
    def get(self, id):
        return { "message": "test", "id": id }