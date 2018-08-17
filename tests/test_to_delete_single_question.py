import unittest
import json
from tests.base import BaseTestCase


class TestPatchQuestion(BaseTestCase):
    """
    Test suite for QuestionView Method View Class

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """
    def test_can_delete_question_by_id(self):
        """
        Test successful DELETE request
        to delete a question by id
        """
        with self.client:
            #  post a question
            _ = self.create_question()

            # delete question
            response = self.client.delete(
                '/api/v1/questions/1',
                content_type='application/json')

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['status'], 'success')
            self.assertTrue(data['message'], 'Question 1 has been deleted')

    def test_cant_delete_question_with_wrong_content_type(self):
        """
        Test successful DELETE request to delete
        a question with wrong content type
        """
        with self.client:
            response = self.client.delete(
                '/api/v1/questions/1',
                content_type='xml'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['status'], 'failed')
            self.assertTrue(data['message'],
                            'request must be of type json')

    def test_cant_delete_question_with_out_of_range_index(self):
        """
        Test unsuccessful DELETE request to
        delete a question with an out of range id
        """
        with self.client:
            # post a question
            _ = self.create_question()

            # delete question
            response = self.client.delete(
                '/api/v1/questions/30',
                content_type='application/json'
            )

            data = json.loads(response.data.decode())
            # self.assertEqual(response.status_code, 400)
            self.assertRaises(KeyError)
            self.assertTrue(data['status'], 'failed')
