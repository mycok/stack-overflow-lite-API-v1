from flask import Blueprint, request, jsonify
from flask.views import MethodView
from app.auth.auth_models import User
from app.auth.auth_helpers import check_for_user_key_error
from app.auth.auth_model_manager import user_manager
from app.response_helpers import response
from app.auth.auth_helpers import response_for_get_all_users
from app.response_helpers import convert_list_to_json


auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1')


class RegistrationView(MethodView):
    """[summary]

    Arguments:
        MethodView {[type]} -- [description]
    """
    methods = ['POST', 'GET']

    def post(self):
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        sent_data = request.get_json()
        username = sent_data.get('username')
        email = sent_data.get('email')
        password = sent_data.get('password')

        user = User.validate_create_user(
            username=username, email=email, password=password)
        if not isinstance(user, User):
            return response(user, 'failed', 400)

        # ext_user = user_manager.check_if_user_exists(email)
        # if not isinstance(ext_user, bool):
        #     return response(ext_user, 'failed', 400)

        user_manager.insert_user(user)
        return response('user registered successfully', 'success', 201)

    def get(self):
        """[summary]
        """
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        users = convert_list_to_json(user_manager.get_all_users())
        return response_for_get_all_users(users, 200)


class Login(MethodView):
    """[summary]

    Arguments:
        MethodView {[type]} -- [description]
    """

    def post(self):
        """[summary]
        """
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        sent_data = request.get_json()
        username = sent_data.get('username')
        email = sent_data.get('email')
        password = sent_data.get('password')

        user = User.validate_create_user(
            username=username, email=email, password=password)

        if not isinstance(user, User):
            return response(user, 'failed', 400)

        resp = user_manager.get_user_by_email(email)

        message = check_for_user_key_error(resp)
        if message:
            return response(message, 'failed', 400)
        return response('user has logged in', 'success', 200)


# Register a class as a view
register = RegistrationView.as_view('register')
login = Login.as_view('login')


# Add url_rules for the API endpoints
auth_bp.add_url_rule('/auth/signup', view_func=register)
auth_bp.add_url_rule('/auth/login', view_func=login)