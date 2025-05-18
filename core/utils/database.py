import sqlite3

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect("db.sqlite3", check_same_thread=False)
        return cls._instance

    def get_connection(self):
        return self.connection