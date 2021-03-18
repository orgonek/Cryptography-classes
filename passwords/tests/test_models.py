from src.models import Account

class TestAccountModel:
    """ Test for account models """
    def test_instance(self):
        a = Account()
        assert a

    def test_get_name(self):
        a = Account("adam","1234")
        assert a.name == "adam"

    def test_set_password(self):
        a = Account("Elon","password")
        a.password = "new_password"
        assert a.password != "new_password"
