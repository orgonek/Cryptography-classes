from routers.asymmetric_view import router
from fastapi.testclient import TestClient

client = TestClient(router)


class TestRouterSymmetric:

    def test_keys(self):
        res = client.get('/api/asymmetric/keys')
        assert res.status_code == 200

    def test_keys_ssh(self):
        res = client.get('/api/asymmetric/keys')
        assert res.status_code == 200

    def test_sign_message(self):
        body = {
            'message': 'hello world'
        }
        res = client.post('/api/asymmetric/sign', body)
        assert res.status_code == 200
        assert res.json() != {'Signature': 'Invalid key'}

    def test_encode_message(self):
        body = {
            'message': 'message to encode'
        }
        res = client.post('/api/asymmetric/encode', body)
        assert res.status_code == 200
        assert res.json() != 'message to encode'
