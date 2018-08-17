import unittest
import json
from tests.base import BaseTestCase


class TestGetAllQuestions(BaseTestCase):
    """
    Test class for QuestionsView Method View Class

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """
    # Test get all questions
    def test_get_all_questions(self):
        """
        Test successful GET request to
        fetch all questions
        """
        with self.client:
            # create a question
            post_response = self.create_question()
            self.assertEqual(post_response.status_code, 201)

            # get all questions
            get_response = self.get_all_questions()

            data = json.loads(get_response.data.decode())
            self.assertEqual(get_response.status_code, 200)
            self.assertIsInstance(data['questions'], list)
            self.assertTrue(data['status'], 'success')
            self.assertEqual(data['questions'][0]['id'], 1)
            self.assertTrue(data['questions'][0]['title'], "seriousness")

    def test_get_all_questions_with_wrong_content_type(self):
        """
        Test unsuccessful GET request to
        fetch all questions with wrong content type
        """
        with self.client:
            response = self.client.get(
                '/api/v1/questions',
                content_type='xml'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertTrue(data['message'], 'request must be of type json')
            self.assertTrue(data['status'], 'failed')
