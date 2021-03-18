from src.service import ApplicationService
import os

class TestService:
    """ Class for testing functionality of service app """

    def test_instance(self):
        app = ApplicationService()
        assert type(app) is ApplicationService

    def test_create_user_status(self):
        app = ApplicationService()
        
        user_name = os.urandom(32)
        password = 'sample'

        assert app.create_user(user_name, password) == True

    def test_authenticate_user(self):
        app = ApplicationService()
        user = 'name'
        password = 'test'

        app.create_user(user, password)

        assert app.authenticate_user(user,password) == True

