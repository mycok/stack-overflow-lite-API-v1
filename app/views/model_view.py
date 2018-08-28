from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flasgger import swag_from
from app.models.models import Question, Answers, Comment
from app.models.model_manager import question_manager
from app.response_helpers import response
from app.response_helpers import response_for_returning_single_question
from app.response_helpers import convert_list_to_json
from app.response_helpers import response_for_get_all_questions
from app.response_helpers import response_to_fetch_single_question
from app.response_helpers import response_for_get_all_answers
from app.response_helpers import convert_user_answers_list_to_json


qtn_bp = Blueprint('question', __name__, url_prefix='/api/v1')


# # Swagger dict:
# specs_dict = {
#   "parameters": [
#     {
#       "title": "string",
#       "body": "string"
#     }
#   ],
#   "definitions": {
#     "Question": {
#       "type": "object",
#       "properties": {
#         "title": {
#           "type": "Dict",
#           "items": {

#           }
#         }
#       }
#     },
#     "body": {
#       "type": "string"
#     }
#   },
#   "responses": {
#     "200": {
#       "description": "A list of questions (may be filtered by id)",
#       },
#     }
#   }


# # Helper function
# def check_for_key_error(resp):
#     """
#     function used to return a custom response
#      in case an out of index error is triggered.

#     Arguments:
#         resp -- object returned from the request
#     """
#     if isinstance(resp, KeyError):
#             return 'Question ' + str(resp) + ' does not exist'


# class QuestionsView(MethodView):

#     methods = ['POST', 'GET']

#     # POST
#     @swag_from(specs_dict)
#     def post(self):
#         """
#         POST request to create a question
#         """

#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)

#         sent_data = request.get_json()
#         author = sent_data.get('author')
#         title = sent_data.get('title')
#         body = sent_data.get('body')
#         tag = sent_data.get('tag')

#         if not title or not body or not tag or not author:
#             return response('missing required parameter', 'failed', 400)
#         if title == '' or title.isspace() or body == '' or body.isspace() or author == '' or author.isspace():
#             return response(
#                 'please provide all required parameters', 'failed', 400)

#         question = Question(author=author.strip(), title=title.strip(), body=body, tag=tag)
#         # question_manager.insert_question(question)
#         qtn = question_manager.insert_question(question)
#         if isinstance(qtn, str):
#             return response(qtn, 'failed', 400)
#         return response_for_returning_single_question(question, 201)

#     # GET
#     @swag_from(specs_dict)
#     def get(self):
#         """
#         GET request to fetch all questions
#         """

#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)

#         questions = question_manager.get_all_questions()
#         if isinstance(questions, str):
#             return response(questions, 'failed', 400)
#         return response_for_get_all_questions(
#             convert_list_to_json(questions), 200)


# class QuestionView(MethodView):

#     methods = ['GET', 'PATCH', 'DELETE']

#     # GET
#     @swag_from(specs_dict)
#     def get(self, qtn_id):
#         """
#         GET request to fetch a question by id
#         """
#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)

#         resp = question_manager.get_question_by_id(qtn_id)
#         if isinstance(resp, str):
#             return response(resp, 'failed', 400)
#         # message = check_for_key_error(resp)
#         # if message:
#         #     return response(message, 'failed', 400)
#         return response_to_fetch_single_question(resp.jsonify(), 200)

#     # PATCH
#     @swag_from(specs_dict)
#     def patch(self, qtn_id):
#         """
#         PATCH request to update contents
#         of a question by id

#         Arguments:
#             qtn_id --int-- A unique integer id assigned to a single question
#         """
#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)

#         res = question_manager.get_question_by_id(qtn_id)
#         if isinstance(res, str):
#             return response(res, 'failed', 400)
#         # message = check_for_key_error(res)
#         # if message:
#         #     return response(message, 'failed', 400)

#         sent_data = request.get_json()
#         title = sent_data.get('title')
#         body = sent_data.get('body')
#         tag = sent_data.get('tag')

#         if title:
#             res.title = title
#         if body:
#             res.body = body
#         if tag:
#             res.tag = tag
#         return response_to_fetch_single_question(res.jsonify(), 202)

#     # DELETE
#     @swag_from(specs_dict)
#     def delete(self, qtn_id):
#         """
#         DELETE request to delete a question by id

#         Arguments:
#             qtn_id --int-- A unique integer id assigned to a single question
#         """
#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)

#         respo = question_manager.delete_question_by_id(qtn_id)
#         if isinstance(respo, str):
#             return response(respo, 'failed', 400)
#         # message = check_for_key_error(respo)
#         # if message:
#         #     return response(message, 'failed', 400)
#         return response(
#             'Question {0} has been deleted'.format(qtn_id), 'success', 200)


# class QuestionAuthor(MethodView):

#     methods = ['GET']

#     # GET
#     @swag_from(specs_dict)
#     def get(self, author):
#         """
#         GET request to fetch all questions that belong to a specific user/author.

#         Arguments:
#             author --str-- A unique string that identifies a specific user
#         """
#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)

#         questions = question_manager.get_all_questions_by_author(author)
#         if isinstance(questions, str):
#             return response(questions, 'failed', 400)
#         return response_for_get_all_questions(
#             convert_list_to_json(questions), 200)


# class AnswerView(MethodView):

#     methods = ['POST', 'GET']

#     @swag_from(specs_dict)
#     def post(self, qtn_id):
#         """
#         POST request to create an answer to a particular question.

#         Arguments:
#             qtn_id --int-- A unique integer id assigned to a single question
#         """
#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)

#         sent_data = request.get_json()
#         body = sent_data.get('body')

#         respon = question_manager.get_question_by_id(qtn_id)
#         if isinstance(respon, str):
#             return response(respon, 'failed', 400)
#         # message = check_for_key_error(respon)
#         # if message:
#         #     return response(message, 'failed', 400)

#         if body == '' or body == '' or body.isspace():
#             return response('missing required parameter', 'failed', 400)
#         answer = Answers(id=respon.id, body=body)
#         respon.answers.append(answer.make_json())
#         return response_for_returning_single_question(respon, 201)

#     # GET
#     @swag_from(specs_dict)
#     def get(self, qtn_id):
#         """
#         GET request to fetch all answers for a particular question.

#         Arguments:
#             qtn_id --int-- A unique integer id assigned to a single question.
#         """
#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)

#         respons = question_manager.get_question_by_id(qtn_id)
#         if isinstance(respons, str):
#             return response(respons, 'failed', 400)
#         # message = check_for_key_error(respons)
#         # if message:
#         #     return response(message, 'failed', 400)

#         answers = convert_user_answers_list_to_json(respons.answers)
#         return response_for_get_all_answers(answers, 200)


# class Answer(MethodView):

#     methods = ['PUT', 'POST']

#     # PUT / Edit answer
#     @swag_from(specs_dict)
#     def put(self, qtn_id, ans_id):
#         """
#         PUT request to update a specific answer for a particular question.

#         Arguments:
#             qtn_id --int-- A unique integer id assigned to a single question.
#             ans_id --int-- A unique integer id assigned to a single answer.
#         """
#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)
#         sent_data = request.get_json()
#         body = sent_data.get('body')
#         accepted = sent_data.get('accepted')

#         if not body or not accepted:
#             return response('missing required parameters', 'failed', 400)
#         if body == "" or body.isspace() or accepted == "" or accepted.isspace():
#             return response('empty strings not allowed', 'failed', 400)

#         respons = question_manager.get_question_by_id(qtn_id)
#         if isinstance(respons, str):
#             return response(respons, 'failed', 400)

#         qtn_author = 'kibu'
#         answer_author = 'myco'
#         answers = respons.answers

#         if respons.author == qtn_author:
#             for ans in answers:
#                 if ans['qtn_id'] == ans_id:
#                     ans['accepted'] = accepted
#                     return response('Answer was updated', 'success', 201)
#                 return response('Answer doesnot exist', 'failed', 400)
#             return response('No answers available', 'failed', 400)

#         for ans in answers:
#             if ans['author'] == answer_author:
#                 ans['body'] = body
#                 return response('Answer body  update successful', 'success', 201)
#             return response('Author mis-match', 'failed', 400)
#         return response('No answers available', 'failed', 400)

#     def post(self, qtn_id, ans_id):
#         """
#         POST request to add a comment to  a specific
#         answer for a particular question.

#         Arguments:
#             qtn_id --int-- A unique integer id assigned to a single question.
#             ans_id --int-- A unique integer id assigned to a single answer.
#         """
#         if not request.content_type == 'application/json':
#             return response('request must be of type json', 'failed', 400)
#         sent_data = request.get_json()
#         username = sent_data.get('username')
#         body = sent_data.get('body')

#         if not username or not body:
#             return response('missing required parameters', 'failed', 400)
#         if username == "" or username.isspace() or body == "" or body.isspace():
#             return response('empty strings not allowed', 'failed', 400)

#         respons = question_manager.get_question_by_id(qtn_id)
#         if isinstance(respons, str):
#             return response(respons, 'failed', 400)

#         answers = respons.answers
#         print(answers)
#         comment = Comment(username=username, body=body, id=ans_id)
#         for ans in answers:
#             if ans['qtn_id'] == ans_id:
#                 print(ans)
#                 ans['comments'].append(comment.make_json())
#                 return response('Comment addition successful', 'success', 201)
#             return response('Answer doesnot exist', 'failed', 400)
#         return response('No answers available', 'failed', 400)


# Register a class as a view
# question_list = QuestionsView.as_view('questions')
# question = QuestionView.as_view('question')
# answer = AnswerView.as_view('answer')
# update = Answer.as_view('update')
# author = QuestionAuthor.as_view('author')


# Add url_rules for the API endpoints
# qtn_bp.add_url_rule('/questions', view_func=question_list)
# qtn_bp.add_url_rule('/questions/<int:qtn_id>', view_func=question)
# qtn_bp.add_url_rule('/questions/<int:qtn_id>/answers', view_func=answer)
# qtn_bp.add_url_rule('/questions/<int:qtn_id>/answers/<int:ans_id>', view_func=update)
# qtn_bp.add_url_rule('/questions/<string:author>', view_func=author)
