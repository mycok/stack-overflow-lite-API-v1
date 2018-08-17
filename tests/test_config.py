import unittest
from tests.base import BaseTestCase
from app import create_app
from app.config import TestingConfig, ProductionConfig


class TestConfigClasses(BaseTestCase):
    """
     Test suite for configuration classes

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """

    def test_development_config(self):
        """
        Test development configuration
        """
        app = create_app()
        self.assertTrue(app.config['DEBUG'])

    def test_testing_config(self):
        """
        Test testing configuration
        """
        app = create_app(TestingConfig)
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])

    def test_production_config(self):
        """
        Test production configuration
        """
        app = create_app(ProductionConfig)
        self.assertTrue(app.config['DEBUG'])
