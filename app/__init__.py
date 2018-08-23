from flask import Flask
from app.views.model_view import qtn_bp
from flasgger import Swagger
from app.config import DevelopmentConfig


def create_app(config_object=None):
    app = Flask(__name__)
    if config_object is not None:
        app.config.from_object(config_object)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(qtn_bp)
    swagger = Swagger(app)
    return app
