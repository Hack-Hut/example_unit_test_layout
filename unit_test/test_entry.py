from unittest import TestCase
from src.entry_point import Entry

class TestEntry(TestCase):
    def setUp(self):
        # This is run before EVERY test
        self.test = Entry()

    def tearDown(self):
        pass

    def test_adder(self):
        self.assertEqual(self.test.adder(1, 2), 3)

    def test_subtractor(self):
        self.assertEqual(self.test.subtractor(1, 2), -1)
        self.assertNotEqual(self.test.subtractor(1, 3), -3)
