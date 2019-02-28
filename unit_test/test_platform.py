from unittest import TestCase
from src.platform import platform

class TestPlatform(TestCase):
    def setUp(self):
        self.test = platform()

    def test_multiply_me(self):
        self.assertEqual(self.test.multiply_me(10, 2), 20)
