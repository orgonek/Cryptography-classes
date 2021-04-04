from routers.symmetric_view import router
from fastapi.testclient import TestClient

client = TestClient(router)


class TestRouterSymmetric:

    def test_key(self):
        res = client.get('/api/symmetric/key')
        assert res.status_code == 200

    def test_key_invalid(self):
        body = {
            "key": "hello"
        }
        response = client.post('/api/symmetric/key', data=body)
        assert response.status_code == 405

    def test_encode_message(self):
        body = {
            'message': 'hii'
        }
        response = client.post('/api/symmetric/encode', data=body)
        assert response.status_code == 200
