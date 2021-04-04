from utils.symmetric_cryptography import Symmetric


class TestAsymmetric:

    def test_instance(self):
        s = Symmetric()
        assert type(s) is Symmetric

    def test_create_key(self):
        s = Symmetric()
        assert s.create_key() != ''

    def test_set_key(self):
        s = Symmetric()
        key = s.create_key()
        s.create_key()
        assert s.set_key(key)

    def test_set_key_invalid(self):
        s = Symmetric()
        assert not s.set_key('try')

    def test_encrypt_message(self):
        s = Symmetric()
        assert s.encode_message('hello world') != 'hello world'

    def test_decode_message(self):
        s = Symmetric()
        message = s.encode_message('welcome')
        decrypted_message = s.decode_message(message)
        assert 'welcome' == decrypted_message
