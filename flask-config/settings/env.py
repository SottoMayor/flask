from os import environ

FLASK_APP=environ.get("FLASK_APP")
FLASK_ENV=environ.get("FLASK_ENV")
FLASK_DEBUG=environ.get("FLASK_DEBUG")
SECRET_KEY=environ.get("SECRET_KEY")
FLASK_HOST=environ.get("FLASK_HOST", 'localhost') # default value
FLASK_PORT=environ.get("FLASK_PORT", '5000') # default value