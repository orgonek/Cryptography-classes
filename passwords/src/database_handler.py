from models import Account
import sqlite3


class DatabaseHandler:
    """ Manages database operations """
    
    def __init__(self, file : str = "sqlite.db") -> None:
        self.connection = sqlite3.connect(file)
        self.connection.row_factory = self._dict_factory
        self.cursor = self.connection.cursor()

    def _dict_factory(self, cursor, row):
        """ Changes form of DB output"""
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __del__(self):
        self.connection.close()

    def create_users_table(self) -> None:
        """ Creates table in case it does not exist """
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,user TEXT UNIQUE, 
        password TEXT,salt TEXT)"""
        )
        
        self.connection.commit()

    def check_name_availability(self, name : str) -> bool:
        """ Checks if the specified user name is available """
        return self.cursor.execute(" SELECT 1 from users where user = ? ", (name,))\
            .fetchone() is None 

    def insert_user(self, user : Account) -> bool:
        """ Adds user to database if name is not occupied """
        user_inserted = False 
        
        if self.check_name_availability(user.name):
            sql = "INSERT INTO users(user, password, salt) VALUES (?,?,?)"
            self.cursor.execute(sql, (user.name, user.password, user.salt.hex()))
            self.connection.commit()
            user_inserted = True

        return user_inserted

    def get_user_data(self, name : str):
        """ Extracts required data from database (password, salt) """
        data = None
        if not self.check_name_availability(name):
            self.cursor.execute("SELECT password, salt from users where user = ?", (name,))
            data = self.cursor.fetchone()
        
        return data
        