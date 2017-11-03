from helga_yelling import is_shout


class TestShoutDetection(object):

    def test_emoticon(self):
        assert is_shout(':)') is False

    def test_short_message(self):
        assert is_shout('I') is False

    def test_simple_shout(self):
        assert is_shout('YO') is True

    def test_actual_shout(self):
        assert is_shout('WHAT THE FUCK') is True

    def test_blank_message(self):
        assert is_shout('') is False
