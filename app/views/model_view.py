from flask import Blueprint, request, jsonify
from flask.views import MethodView
from app.models.models import Question, Answer
from app.models.model_manager import question_manager
from app.response_helpers import response, response_for_creating_question
from app.response_helpers import convert_list_to_json
from app.response_helpers import response_for_get_all_questions
from app.response_helpers import response_to_fetch_single_question
from app.response_helpers import response_for_creating_an_answer
from app.response_helpers import response_for_get_all_answers


qtn_bp = Blueprint('question', __name__, url_prefix='/api/v1')


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
        return response_for_creating_question(
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

        respo = question_manager.get_question(qtn_id)
        if isinstance(respo, KeyError):
            return response('Question ' + str(respo) + ' does not exist',
                            'failed', 400)
        return response_to_fetch_single_question(respo.jsonify(), 200)

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

        respo = question_manager.get_question(qtn_id)
        if isinstance(respo, KeyError):
            return response('Question ' + str(respo) + ' does not exist',
                            'failed', 400)

        sent_data = request.get_json()
        title = sent_data.get('title')
        body = sent_data.get('body')
        tag = sent_data.get('tag')
        if title:
            respo.title = title
        if body:
            respo.body = body
        if tag:
            respo.tag = tag
        return response_to_fetch_single_question(respo.jsonify(), 202)

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
        if isinstance(respo, KeyError):
            return response('Question ' + str(respo) + ' does not exist',
                            'failed', 400)
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
        respo = question_manager.get_question(qtn_id)

        if isinstance(respo, KeyError):
            return response('Question ' + str(respo) + ' does not exist',
                            'failed', 400)
        answer = Answer(respo.id, body=body)
        respo.answers.append(answer.make_json())
        return response_for_creating_an_answer(respo, 201)

    # GET
    def get(self, qtn_id):
        """
        GET request to fetch all answers for a particular question

        Arguments:
            qtn_id {[type]} -- [description]
        """
        if not request.content_type == 'application/json':
            return response('request must be of type json', 'failed', 400)

        respo = question_manager.get_question(qtn_id)
        if isinstance(respo, KeyError):
            return response('Question ' + str(respo) + ' does not exist',
                            'failed', 400)
        answers = convert_list_to_json(respo.answers)
        return response_for_get_all_answers(answers, 200)


# Register a class as a view
question_list = QuestionsView.as_view('questions')
question = QuestionView.as_view('question')
answer = AnswerView.as_view('answer')


# Add url_rules for the API endpoints
qtn_bp.add_url_rule('/questions', view_func=question_list)
qtn_bp.add_url_rule('/questions/<int:qtn_id>', view_func=question)
qtn_bp.add_url_rule('/questions/<int:qtn_id>/answers', view_func=answer)
