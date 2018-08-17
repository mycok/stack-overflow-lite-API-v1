from datetime import datetime


class Question(object):
    """
    Question Model
    """

    def __init__(self, title, body, tag):
        self.id = 0
        self.posted_date = datetime.now()
        self.title = title
        self.body = body
        self.tag = tag
        self.answers = []

    def jsonify(self):
        return {
            "id": self.id,
            "date_posted": self.posted_date,
            "title": self.title,
            "body": self.body,
            "tag": self.tag,
            "answers": self.answers
        }
