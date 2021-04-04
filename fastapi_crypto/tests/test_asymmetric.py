from utils.asymmetric_cryptography import Asymmetric


class TestAsymmetric:

    def test_instance(self):
        a = Asymmetric()
        assert type(a) is Asymmetric

    def test_create_keys(self):
        a = Asymmetric()
        assert a.create_keys() != ''

    def test_create_keys_ssh(self):
        a = Asymmetric()
        assert a.create_ssh_keys() != ''

    def test_set_keys_invalid(self):
        a = Asymmetric()
        assert not a.set_keys('1', '2')

    def test_set_keys_valid(self):
        a = Asymmetric()
        keys = a.keys
        a.create_keys()
        assert a.set_keys(keys['public'], keys['private'])

    def test_sign_message(self):
        a = Asymmetric()
        message = "hello world"
        assert a.sign_message(message) != message

    def test_verify_message(self):
        a = Asymmetric()
        signature = a.sign_message('hello')
        assert a.verify_message('hello', signature)

    def test_verify_message_invalid(self):
        a = Asymmetric()
        signature = 'invalid'
        assert a.verify_message('hello', signature) is False

    def test_encode_message(self):
        a = Asymmetric()
        message = 'hello'
        assert a.encode_message(message) != message

    def test_decode_message(self):
        a = Asymmetric()
        message = a.encode_message('hello')
        assert 'hello' == a.decode_message(message)
