import unittest
import json
from tests.base import BaseTestCase


class TestPatchQuestion(BaseTestCase):
    """
    Test suite for QuestionView Method View Class

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """

    def test_can_update_question_attributes_by_id(self):
        """
        test successful PATCH request to update question attributes
        """
        with self.client:
            # post a question
            _ = self.create_question()

            # patch question
            response = self.client.patch(
                '/api/v1/questions/1',
                content_type='application/json',
                data=json.dumps(dict(title='challenges',
                                     body='challenges are good', tag='AGE'))
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 202)
            self.assertTrue(data['status'], 'success')
            self.assertIn('question', data)

    def test_cant_update_question_with_out_of_range_index(self):
        """
        Test unsuccessful PATCH request to
        fetch a question with an out of range id
        """
        with self.client:
            # post a question
            _ = self.create_question()

            # patch question
            response = self.client.patch(
                '/api/v1/questions/20',
                content_type='application/json',
                data=json.dumps(dict(title='challenges are good'))
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertRaises(KeyError)
            self.assertTrue(data['status'], 'failed')

    def test_cant_update_question_with_wrong_content_type(self):
        """
        Test successful GET request to fetch
        a question with wrong content type
        """
        with self.client:
            response = self.client.patch(
                '/api/v1/questions/1',
                content_type='xml'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['status'], 'failed')
            self.assertTrue(data['message'], 'request must be of type json')
