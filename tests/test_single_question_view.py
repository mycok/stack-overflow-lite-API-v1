import unittest
import json
from tests.base import BaseTestCase


class TestGetQuestion(BaseTestCase):
    """
    Test suite for QuestionView Method View Class

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """
    # GET

    def test_get_question_by_id(self):
        """
        Test successful GET request to fetch a question by id
        """
        with self.client:
            # post a question
            _ = self.create_question()

            # get that question by id
            response = self.client.get(
                '/api/v1/questions/1',
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['status'], 'success')
            self.assertTrue(data['question']['title'], 'second endpoint')
            self.assertIn('question', data)
            self.assertIsInstance(data['question']['answers'], list)

    def test_cant_get_question_with_out_of_range_index(self):
        """
        Test unsuccessful GET request to fetch
         a question with an out of range id index
        """
        with self.client:
            # post a question
            _ = self.create_question()

            # get that question by id
            response = self.client.get(
                '/api/v1/questions/20',
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertRaises(KeyError)
            self.assertTrue(data['status'], 'failed')

    def test_get_question_with_wrong_content_type(self):
        """
        Test unsuccessful GET request to
        fetch a question with wrong content type
        """
        with self.client:
            response = self.client.get(
                '/api/v1/questions/1',
                content_type='xml'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['status'], 'failed')
            self.assertTrue(data['message'], 'request must be of type json')
