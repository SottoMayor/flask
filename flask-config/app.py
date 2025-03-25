from flask import Flask
from flask_cors import CORS
from database.connection import db
from flask_migrate import Migrate
import models
from flask_seeder import FlaskSeeder
from flask_smorest import Api
from controllers.user import blp as UserBlueprint
from middlewares.log_middleware import log_middleware

app = Flask(__name__)

# CORS
CORS(app)

# Env vars
app.config.from_pyfile('settings/env.py')
FLASK_APP = app.config['FLASK_APP']
FLASK_HOST = app.config['FLASK_HOST']
FLASK_PORT = app.config['FLASK_PORT']

# DB
db.init_app(app)

# Migrations
migrate = Migrate(app, db)

# Seeds
seeder = FlaskSeeder()
seeder.init_app(app, db)

# Middlewares
log_middleware(app)

# Blueprints
api = Api(app)
api.register_blueprint(UserBlueprint)


print(f'App running on {FLASK_HOST}:{FLASK_PORT} | entryfile: {FLASK_APP} 🚀')