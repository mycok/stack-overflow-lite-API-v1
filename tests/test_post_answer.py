import unittest
import json
from tests.base import BaseTestCase


class TestAnswerView(BaseTestCase):
    """
    Test suite for AnswerView Method View Class

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """
    # POST

    def test_create_an_answer(self):
        """
        Test successful POST request to
        create an answer for a specific question
        """
        with self.client:
            # post a question
            post_resp = self.create_question()
            self.assertEqual(post_resp.status_code, 201)

            # post an answer
            response = self.client.post(
                '/api/v1/questions/1/answers',
                content_type='application/json',
                data=json.dumps(dict(body='an answer body'))
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertTrue(data['status'], 'success')
            self.assertTrue(data['id'], 1)
            self.assertTrue(data['body'], 'an answer body')
            self.assertIsInstance(data['answers'], list)

    def test_create_answer_with_wrong_content_type(self):
        """
        Test unsuccessful POST request to
        create an answer with content_type not of type json
        """
        with self.client:
            response = self.client.post(
                '/api/v1/questions/1/answers',
                content_type="xml",
                data=json.dumps(dict(body='an answer body'))
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['message'], 'request must be of type json')
            self.assertTrue(data['status'], 'failed')

    def test_cant_create_answer_with_out_of_range_index(self):
        """
        Test unsuccessful POST request to
        create an answer with an out of range question id
        """
        with self.client:
            # post a question
            _ = self.create_question()

            # post an answer
            response = self.client.post(
                '/api/v1/questions/56/answers',
                content_type='application/json',
                data=json.dumps(dict(body='an answer body'))
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertRaises(KeyError)
            self.assertTrue(data['status'], 'failed')
