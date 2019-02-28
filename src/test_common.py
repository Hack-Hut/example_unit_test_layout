from unittest import TestCase
from src.common import *

class test_common(TestCase):
    def test_exists(self):
        self.assertTrue(exists("/etc/passwd"))
        self.assertFalse(exists("/setc/passwd"))

    def test_extension(self):
        self.assertEqual(extension("test.txt"), ".txt")