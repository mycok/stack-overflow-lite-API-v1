from app.auth.auth_models import User
from app.db.db_manager import db


class UserManager(object):
    """
    Manager class for handling and storing user data
    """
    def __init__(self):
        self.users = {}

    # check if user exits based on an email address
    def check_if_user_exists(self, email):
        """[summary]
        """
        try:
            self.users[email]
            return "user exists"

        except KeyError:

            return False

    def insert_user(self, user):
        # self.users[user.email] = user
        db.create_tables()
        db.insert_user()

    # def get_user_by_email(self, email):

    #     try:
    #         return self.users[email]

    #     except KeyError as e:
    #         return e

    # def get_all_users(self):
    #     return [v for v in self.users.values()]


# A user manager instance
user_manager = UserManager()
