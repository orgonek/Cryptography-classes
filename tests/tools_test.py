from src.utils import count_errors

class TestTools:
    """ Class containing tests for utils """

    def test_no_errors_word(self):
        assert count_errors('hello') == 0

    def test_errors_word(self):
        assert count_errors('pfsadasda') == 1

    def test_no_errors_sentence(self):
        assert count_errors('Hello, nice to meet You! How are you today?') == 0

    def test_errors_sentence(self):
        assert count_errors('sbabsa, dsadas, asdfgasd, pqwsppqd?') == 4

    def test_sentence_mixed(self):
        assert count_errors('Hello, maj friynd') == 2