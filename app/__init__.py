from flask import Flask
from flasgger import Swagger
from app.views.model_view import qtn_bp
from app.config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(qtn_bp)
swagger = Swagger(app)
