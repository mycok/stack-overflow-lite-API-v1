from flask import Flask
from flasgger import Swagger
from app.views.model_view import qtn_bp
from app.auth.auth_views import auth_bp
from app.config import DevelopmentConfig
# from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(qtn_bp)
app.register_blueprint(auth_bp)
swagger = Swagger(app)
# encrypt = Bcrypt(app)
