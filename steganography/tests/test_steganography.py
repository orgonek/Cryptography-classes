from steganography import Steganography


class TestSteganography:

    def test_instance(self):
        s = Steganography()
        assert type(s) is Steganography

    def test_encode(self):
        assert Steganography.encode('img/test.jpg', 'bad message', 'img/file') != 'Error'
        
    def test_encode_error(self):
        assert Steganography.encode('incorrectpath', 'aaa', 'new') == 'Error'

    def test_decode(self):
        assert Steganography.decode('img/file.png') == 'bad message'
