import unittest
import json
from app import app
from app.config import TestingConfig


class BaseTestCase(unittest.TestCase):
    """[summary]

    Arguments:
        unittest {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    def setUp(self):
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()

    def create_question(self):
        """
        send a POST request to create a question object
        """
        return self.client.post(
            '/api/v1/questions', content_type='application/json',
            data=json.dumps(dict(title="seriousness",
                            body="seriousness is needed", tag="LIFE")))

    def create_creation_with_missing_attributes(self):
        """
        send a POST request to create a question object
        with missing required parameters.
        """
        return self.client.post(
            '/api/v1/questions', content_type='application/json',
            data=json.dumps(dict(title="seriousness",
                            body="seriousness is needed")))

    def get_all_questions(self):
        """
        send a GET request to fetch all question objects
        """
        return self.client.get(
             '/api/v1/questions', content_type='application/json')
