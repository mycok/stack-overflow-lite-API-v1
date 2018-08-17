import unittest
import json
from tests.base import BaseTestCase


class TestCreateQuestion(BaseTestCase):
    """
    Test suite for QuestionsView Method View Class

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """
    # Test create a question

    def test_create_a_question(self):
        """
        Test successful POST request to create a question
        """
        with self.client:
            response = self.create_question()

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertTrue(data['status'], 'success')
            self.assertTrue(data['id'], 1)
            self.assertTrue(data['body'], "seriousness is needed")
            self.assertIsInstance(data['answers'], list)

    def test_create_question_with_a_missing_attribute(self):
        """
        Test unsuccessful POST request to
        create a question yet missing some required attribute
        """
        with self.client:
            response = self.create_creation_with_missing_attributes()

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['message'], 'missing required parameter')
            self.assertTrue(data['status'], 'failed')

    def test_create_question_with_wrong_content_type(self):
        """
         Test unsuccessful POST request to
        create a question with wrong content type
        """
        with self.client:
            response = self.client.post(
                '/api/v1/questions',
                content_type="xml",
                data=json.dumps(dict(title='seriousness',
                                     body='seriousness is needed', tag='LIFE'))
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['message'], 'request must be of type json')
            self.assertTrue(data['status'], 'failed')
