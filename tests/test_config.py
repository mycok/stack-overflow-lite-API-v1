import unittest
from tests.base import BaseTestCase
from app.ap import app
from app.config import TestingConfig, ProductionConfig
from app.config import DevelopmentConfig


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
        app = self.app
        app.config.from_object(DevelopmentConfig)
        self.assertTrue(app.config['DEBUG'])

    def test_testing_config(self):
        """
        Test testing configuration
        """
        app = self.app
        app.config.from_object(TestingConfig)
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])

    def test_production_config(self):
        """
        Test production configuration
        """
        app = self.app
        app.config.from_object(ProductionConfig)
        self.assertTrue(app.config['DEBUG'])
