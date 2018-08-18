from flask import make_response, jsonify


def response(message, status, status_code):
    return make_response(jsonify({
        "message": message,
        "status": status
    })), status_code


def response_for_returning_single_question(question, status_code):
    return make_response(jsonify({
        'status': 'success',
        'id': question.id,
        'title': question.title,
        'body': question.body,
        'tag': question.tag,
        'date_posted': question.posted_date,
        'answers': question.answers
    })), status_code


def response_for_get_all_questions(questions, status_code):
    return make_response(jsonify({
        'status': 'success',
        'questions': questions
    })), status_code


def response_to_fetch_single_question(question, status_code):
    return make_response(jsonify({
        'status': 'success',
        'question': question
    })), status_code


def response_for_get_all_answers(answers, status_code):
    return make_response(jsonify({
        'status': 'success',
        'answers': answers
    })), status_code


def convert_user_answers_list_to_json(answers):
    """
    convert answers list to json
    Arguments:
        lst -- list of answers
    """

    lst = []
    for answer in answers:
        lst.append(answer)
    return lst


def convert_list_to_json(lsty):
    """
    converts a list to json
    Arguments:
        lst -- list of objects
    """

    lst = []
    for l in lsty:
        lst.append(l.jsonify())
    return lst
