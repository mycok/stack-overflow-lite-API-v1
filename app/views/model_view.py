from flask import Blueprint, request, jsonify
from flask.views import MethodView
from app.models.models import Question
from app.models.model_manager import question_manager
from app.response_helpers import response, response_for_creating_question


qtn_bp = Blueprint('question', __name__, url_prefix='/api/v1')


class QuestionsView(MethodView):

    methods = ['POST']

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

# Register a class as a view
question_list = QuestionsView.as_view('questions')


# Add url_rules for the API endpoints
qtn_bp.add_url_rule('/questions', view_func=question_list)
