from app.models.models import Question


class QuestionManager():
    """
    Manager class for storing and controlling
    manipulations for question objects.

    [last_id] -- class property used to INCREMENT the question_id
    whenever a new instance of the question object is created.

    [insert_question] -- method called to INSERT a question.
    object into the questions dictionary.

    [get_question] -- method called to GET a question
    object with a specified question_id from the questions dictionary.

    [delete_question] -- method called to DELETE a question
    object with a specified question_id from the questions dictionary.

    [get_all_questions] -- method called to GET ALL question
    objects from the questions dictionary.
    """

    last_id = 0

    def __init__(self):
        self.questions = {}

    def insert_question(self, question):
        self.__class__.last_id += 1
        question.id = self.__class__.last_id
        self.questions[self.__class__.last_id] = question

    def get_question(self, qtn_id):

        try:
            return self.questions[qtn_id]

        except KeyError as e:
            return e

    def delete_question(self, qtn_id):
        try:
            del self.questions[qtn_id]

        except KeyError as e:
            return e

    def get_all_questions(self):
        return [value for value in self.questions.values()]

# A question manager instance
question_manager = QuestionManager()
