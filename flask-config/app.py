from flask import Flask
from flask_cors import CORS
from database.connection import db
from flask_migrate import Migrate
import models
from flask_seeder import FlaskSeeder
from flask_smorest import Api
from controllers.user import blp as UserBlueprint

app = Flask(__name__)

# CORS
CORS(app)

# Env vars
app.config.from_pyfile('settings/env.py')
FLASK_APP = app.config['FLASK_APP']
FLASK_HOST = app.config['FLASK_HOST']
FLASK_PORT = app.config['FLASK_PORT']
OPENAPI_SWAGGER_UI_PATH = app.config['OPENAPI_SWAGGER_UI_PATH']

# DB
db.init_app(app)

# Migrations
migrate = Migrate(app, db)

# Seeds
seeder = FlaskSeeder()
seeder.init_app(app, db)

# Blueprints
api = Api(app)
api.register_blueprint(UserBlueprint)


print(f'App running on {FLASK_HOST}:{FLASK_PORT} | entryfile: {FLASK_APP} 🚀')