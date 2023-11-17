import os
from flask import Flask
from .Test_app import init_blue_print
from .utils import config_log
from Test_app.config import config


def create_app():
    config_log()
    app = Flask(__name__)
    env = os.environ.get('FLASK_ENV', 'default')
    app.config.from_object(config.get(env))
    init_blue_print(app)

    return app
