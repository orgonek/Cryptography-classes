from database_handler import DatabaseHandler
from models import Account
from utils import hash_password


class ApplicationService:
    """ Class responsible for  """
    def __init__(self) -> None:
        self.db = DatabaseHandler()
        self.db.create_users_table()

    def create_user(self, name : str, password : str) -> bool:
        account = Account(name, password)
        return self.db.insert_user(account)

    def authenticate_user(self, name, password) -> bool:
        status = False
        data = self.db.get_user_data(name)
        if data and hash_password(password, bytes.fromhex(data['salt'])) == data['password']:
            status = True

        return status