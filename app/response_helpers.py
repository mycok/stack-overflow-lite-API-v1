from flask import make_response, jsonify


def response(message, status, status_code):
    return make_response(jsonify({
        "message": message,
        "status": status
    })), status_code


def response_for_creating_question(question, status_code):
    return make_response(jsonify({
        'status': 'success',
        'id': question.id,
        'title': question.title,
        'body': question.body,
        'tag': question.tag,
        'date_posted': question.posted_date,
        'answers': question.answers
    })), status_code
