from flask import Blueprint, request, jsonify
from flask.views import MethodView
from app.models.models import Question, Answer
from app.models.model_manager import question_manager
from app.response_helpers import response
from app.response_helpers import response_for_returning_single_question
from app.response_helpers import convert_list_to_json
from app.response_helpers import response_for_get_all_questions
from app.response_helpers import response_to_fetch_single_question
from app.response_helpers import response_for_get_all_answers
from app.response_helpers import convert_user_answers_list_to_json


qtn_bp = Blueprint('question', __name__, url_prefix='/api/v1')


# Helper function
def check_for_key_error(resp):
    """
    function used to return a custom response
     in case an out of index error is triggered.

    Arguments:
        resp -- object returned from the request
    """
    if isinstance(resp, KeyError):
            return 'Question ' + str(resp) + ' does not exist'


class QuestionsView(MethodView):

    methods = ['POST', 'GET']

    # POST
    def post(self):
        """
        POST request to create a question
        """

        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        sent_data = request.get_json()
        title = sent_data.get('title')
        body = sent_data.get('body')
        tag = sent_data.get('tag')

        if not title or not body or not tag:
            return response('missing required parameter', 'failed', 400)

        question = Question(title=title, body=body, tag=tag)
        question_manager.insert_question(question)
        return response_for_returning_single_question(
            question, 201)

    # GET
    def get(self):
        """
        GET request to fetch all questions
        """

        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        questions = question_manager.get_all_questions()
        return response_for_get_all_questions(
            convert_list_to_json(questions), 200)


class QuestionView(MethodView):

    methods = ['GET', 'PATCH', 'DELETE']

    # GET
    def get(self, qtn_id):
        """
        GET request to fetch a question by id
        """
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        resp = question_manager.get_question(qtn_id)
        message = check_for_key_error(resp)
        if message:
            return response(message, 'failed', 400)
        return response_to_fetch_single_question(resp.jsonify(), 200)

    # PATCH
    def patch(self, qtn_id):
        """
        PATCH request to update contents
        of a question by id

        Arguments:
            qtn_id {[type]} -- [description]
        """
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        res = question_manager.get_question(qtn_id)
        message = check_for_key_error(res)
        if message:
            return response(message, 'failed', 400)

        sent_data = request.get_json()
        title = sent_data.get('title')
        body = sent_data.get('body')
        tag = sent_data.get('tag')

        if title:
            res.title = title
        if body:
            res.body = body
        if tag:
            res.tag = tag
        return response_to_fetch_single_question(res.jsonify(), 202)

    # DELETE
    def delete(self, qtn_id):
        """
        DELETE request to delete a question by id
        Arguments:
            qtn_id {[type]} -- [description]
        """
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        respo = question_manager.delete_question(qtn_id)
        message = check_for_key_error(respo)
        if message:
            return response(message, 'failed', 400)
        return response(
            'Question {0} has been deleted'.format(qtn_id), 'success', 200)


class AnswerView(MethodView):

    methods = ['POST', 'GET']

    def post(self, qtn_id):
        """
        POST request to create an answer to a particular question

        Arguments:
            MethodView {[type]} -- [description]
            qtn {[type]} -- [description]
        """
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        sent_data = request.get_json()
        body = sent_data.get('body')
        respon = question_manager.get_question(qtn_id)
        message = check_for_key_error(respon)
        if message:
            return response(message, 'failed', 400)

        answer = Answer(respon.id, body=body)
        respon.answers.append(answer.make_json())
        return response_for_returning_single_question(respon, 201)

    # GET
    def get(self, qtn_id):
        """
        GET request to fetch all answers for a particular question

        Arguments:
            qtn_id {[type]} -- [description]
        """
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        respons = question_manager.get_question(qtn_id)
        message = check_for_key_error(respons)
        if message:
            return response(message, 'failed', 400)

        answers = convert_user_answers_list_to_json(respons.answers)
        return response_for_get_all_answers(answers, 200)


# Register a class as a view
question_list = QuestionsView.as_view('questions')
question = QuestionView.as_view('question')
answer = AnswerView.as_view('answer')


# Add url_rules for the API endpoints
qtn_bp.add_url_rule('/questions', view_func=question_list)
qtn_bp.add_url_rule('/questions/<int:qtn_id>', view_func=question)
qtn_bp.add_url_rule('/questions/<int:qtn_id>/answers', view_func=answer)
