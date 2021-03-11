from src.hash_all import HashAll
import os

class TestHashAll:
    """ Class containing tests for HashAll class """

    def test_instance(self):
        h = HashAll()
        assert type(h) is HashAll

    def test_perform_hashing(self):
        h = HashAll()
        result = h.perform_hashing(text = 'Have a nice day')

        assert result['md5']['hexdigest'] == 'f65f2bc6704b044c5804cf89bd6b88f7'
        assert result['sha256']['hexdigest'] == 'c69a4016495ec54e179ef51384f3c9fe7fb39f6d0933cbdc7b5bd67e16c7feda'

    def test_hashing_shake_algorithm(self):
        h = HashAll()
        result = h.perform_hashing(text = 'Experience is not the best teacher. '\
            'The consequence from experience is the best teacher. No consequence no lesson.')

        assert result['shake_256']['hexdigest'] == 'aceebdfc9d916dd3055c7e9b28c289b8bbbaa161b09c'\
            '6a27a84693ed1a38e695acc8f4ca3016e4a235ab3e62d4ec68dd6b8b602aa186e0a9181c14ef0ccedeb4'


    def test_perform_file_hashing(self):
        h = HashAll()
        path = os.path.join(os.getcwd(),'hashing', 'tests', 'poem_text.txt')
        assert h.perform_file_hashing(path, '') == 'ba1ec51296cd10d41d17e48055c3440fdc9c7cde047f865c9b2fce25d0d1ac52'