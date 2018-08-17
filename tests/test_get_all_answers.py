import unittest
import json
from tests.base import BaseTestCase


class TestAnswerView(BaseTestCase):
    """
    Test suite for AnswerView Method View Class

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """
    # GET

    def test_get_all_answers(self):
        """
        Test successful GET request
        to fetch all answer objects for a specific question
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
            self.assertEqual(response.status_code, 201)

            get_resp = self.client.get(
                '/api/v1/questions/1/answers',
                content_type='application/json'
            )
            data = json.loads(get_resp.data.decode())
            self.assertEqual(get_resp.status_code, 200)
            self.assertTrue(data['answers'], list)
            self.assertTrue(data['answers'][0]['id'], 1)

    def test_cant_get_all_answers_with_wrong_content_type(self):
        """
        Test unsuccessful GET request to fetch all answers
        for a specific question with content_type not of type json
        """
        with self.client:
            response = self.client.get(
                '/api/v1/questions/1/answers',
                content_type="xml")

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['message'], 'request must be of type json')
            self.assertTrue(data['status'], 'failed')

    def test_cant_get_all_answers_with_out_of_range_index(self):
        """
        Test unsuccessful GET request to
        fetch all answers for a specific question
        with an out of range question id
        """
        with self.client:
            # post a question
            _ = self.create_question()

            # post an answer
            response = self.client.get(
                '/api/v1/questions/5/answers',
                content_type='application/json')

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertRaises(KeyError)
            self.assertTrue(data['status'], 'failed')
