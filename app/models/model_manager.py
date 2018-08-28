# from app.models.models import Question


# class QuestionManager():
#     """
#     Manager class for storing and controlling
#     manipulations for question objects.

#     [last_id] -- class property used to INCREMENT the question_id
#     whenever a new instance of the question object is created.

#     [insert_question] -- method called to INSERT a question.
#     object into the questions dictionary.

#     [get_question] -- method called to GET a question
#     object with a specified question_id from the questions dictionary.

#     [delete_question] -- method called to DELETE a question
#     object with a specified question_id from the questions dictionary.

#     [get_all_questions] -- method called to GET ALL question
#     objects from the questions dictionary.

#     """

#     last_id = 0

#     def __init__(self):
#         self.questions = []
#     #     self.dict_questions = {}

#     # # Dict methods
#     # def insert_question_in_dict(self, question):
#     #     self.__class__.last_id += 1
#     #     question.id = self.__class__.last_id
#     #     self.dict_questions[__class__.last_id] = question

#     # def get_question(self, qtn_id):

#     #     try:
#     #         return self.dict_questions[qtn_id]

#     #     except KeyError as e:
#     #         return e

#     # def delete_question(self, qtn_id):

#     #     try:
#     #         del self.dict_questions[qtn_id]

#     #     except KeyError as e:
#     #         return e

#     # def get_all_questions_in_dict(self):
#     #     if len(self.dict_questions) > 0:
#     #         return [value for value in self.dict_questions.values()]
#     #     return "No questions available"

#     # List methods
#     def insert_question(self, question):
#         for q in self.questions:
#             if q.title == question.title:
#                 return 'Question with title ' + question.title + ' already exists'
#         self.__class__.last_id += 1
#         question.id = self.__class__.last_id
#         self.questions.append(question)

#     def get_question_by_id(self, qtn_id):
#         for q in self.questions:
#             if q.id == qtn_id:
#                 return q
#         return 'Question ' + str(qtn_id) + ' doesnot exist'

#     def get_question_by_author(self, author):
#         for q in self.questions:
#             if q.author == author:
#                 return q
#         return 'Question ' + author + ' doesnot exist'

#     def delete_question_by_id(self, qtn_id):
#         for q in self.questions:
#             if q.id == qtn_id:
#                 return self.questions.remove(q)
#         return 'Question ' + str(qtn_id) + ' doesnot exist'

#     def get_all_questions(self):
#         if len(self.questions) > 0:
#             return [q for q in self.questions]
#         return "No questions available"

#     def get_all_questions_by_author(self, author):
#         if len(self.questions) > 0:
#             qtns = [q for q in self.questions if q.author == author]
#             if len(qtns) > 0:
#                 return qtns
#         return "No questions available"

#     def get_all_questions_with_most_answers(self):
#         if len(self.questions) > 0:
#             qtns = [q for q in self.questions if len(q.anwers) > 0]
#             if len(qtns) > 0:
#                 return "No answers available"
#             if len(qtns) == 1:
#                 return qtns
#             highest = 2
#             super = object
#             for q in qtns:
#                 if len(q.answers) > highest:
#                     super = q







# # A question manager instance
# question_manager = QuestionManager()
