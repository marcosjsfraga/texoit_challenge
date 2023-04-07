import logging
import sqlite3
from typing import Union, Optional

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

DATABASE_URI = "database.db"
# _connection: sqlite3.Connection

class Database():

    def get_connection(self):
        _connection = sqlite3.connect(database=DATABASE_URI, check_same_thread=False)
        return _connection

    def initialize_db(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, year INTEGER, title TEXT, studios TEXT, producers TEXT, winner INTEGER);"
        )
        
        cursor.close()
        connection.close()
