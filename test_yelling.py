import unittest

from helga_yelling import is_shout


class ShoutDetectionTestCase(unittest.TestCase):

    def test_emoticon(self):

        self.assertFalse(is_shout(':)'))

    def test_short_message(self):

        self.assertFalse(is_shout('I'))

    def test_simple_shout(self):

        self.assertTrue(is_shout('YO'))

    def test_actual_shout(self):

        self.assertTrue(is_shout('WHAT THE FUCK'))

    def test_blank_message(self):

        self.assertFalse(is_shout(''))
