from cipher import CustomCipher


class TestAsymmetric:

    def test_instance(self):
        cipher = CustomCipher(2)
        assert type(cipher) is CustomCipher

    def test_generated_alphabet(self):
        cipher = CustomCipher(10)
        assert cipher.alphabet is not None

    def test_reverse_row(self):
        data = 'hello'
        assert 'olleh' == CustomCipher._reverse_row(data)

    def test_encrypt_message(self):
        c = CustomCipher(3)
        with open('testdata.txt') as f:
            data = f.read()

        assert data != c.encrypt('testdata.txt')








