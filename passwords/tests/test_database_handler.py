from src.database_handler import DatabaseHandler
from src.database_handler import DatabaseHandler
from src.models import Account


class TestDatabaseHandler:
    """ Class responsible for testing database operations"""

    def test_instance(self):
        db = DatabaseHandler()
        assert db

    def test_check_name(self):
        a = Account('Greg', '1234')
        db=  DatabaseHandler()
        db.create_users_table()
        db.insert_user(a)
        assert db.check_name_availability(a.name) == False


