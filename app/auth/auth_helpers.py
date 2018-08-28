from flask import make_response, jsonify


def check_for_user_key_error(resp):
    """[summary]

    Arguments:
        resp {[type]} -- [description]
    """
    if isinstance(resp, KeyError):
            return 'user with email ' + str(resp) + ' does not exist'


def response_for_get_all_users(users, status_code):
    return make_response(jsonify({
        'status': 'success',
        'users': users
    })), status_code
