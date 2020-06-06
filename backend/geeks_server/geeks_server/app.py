from flask import Flask
from .config import DevelopmentConfig
from .views import helloworld
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)
    CORS(app)

    app.register_blueprint(helloworld)

    return app
