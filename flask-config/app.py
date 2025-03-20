from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# CORS
CORS(app)

# Env vars
app.config.from_pyfile('settings/env.py')
FLASK_APP = app.config['FLASK_APP']
FLASK_HOST = app.config['FLASK_HOST']
FLASK_PORT = app.config['FLASK_PORT']

@app.route('/')
def hello_world():
    return "Hello World!"

print(f'App running on {FLASK_HOST}:{FLASK_PORT} | entryfile: {FLASK_APP} 🚀')