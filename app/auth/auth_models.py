from datetime import datetime
import re
# from app.ap import encrypt


class User(object):
    """
    A class that defines a user object
    """

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.created_timestamp = datetime.now()

    # @staticmethod
    # def make_password(raw_password):
    #     """
    #     Method used to generate a hashed password

    #     Arguments:
    #         raw_password  -- Unhashed password
    #     """

    #     return encrypt.generate_password_hash(raw_password)

    # def check_password(self, raw_password):
    #     """
    #     Method used to validate password

    #     Arguments:
    #         raw_password  --  Unhashed password
    #     """
    #     return encrypt.check_password_hash(self.password_hash, raw_password)

    @classmethod
    def validate_create_user(cls, username, email, password):
        """
        Method called to create a user object

        Arguments:
            username {string} -- username
            email {string} -- email
            password_hash {string} -- password
        """
        if not username or username == "" or username.isspace():
            return "username missing, please provide a username"
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "email missing/email is of an invalid format"
        if not password or len(password) < 8:
            return "password missing/password should be atleast 8 characters"

        return User(
            username=username, email=email, password=password)

    def jsonify(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_timestamp
        }
