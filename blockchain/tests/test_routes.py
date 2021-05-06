from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


class TestRoutes:

    def test_get_status(self):
        res = client.get('/api/status')
        assert res.status_code == 200

    def test_mine(self):
        res = client.get('/api/mine')
        assert res.status_code == 200

    def test_chain(self):
        res = client.get('/api/chain')
        assert res.status_code == 200

    def test_transaction_invalid(self):
        body = {
            'something wrong' : 'true'
        }
        response = client.post('/api/transactions/new', data=body)
        assert response.status_code == 422
