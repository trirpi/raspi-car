from flask import Flask
from settings import secret_key

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key

import rcar.routes
