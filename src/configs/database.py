import sqlite3


class Database():

    def get_connection(self):
        return sqlite3.connect(database="database.db", check_same_thread=False)

    def initialize_db(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, year INTEGER, title TEXT, studios TEXT, producers TEXT, winner INTEGER);"
        )
        
        cursor.close()
        connection.close()
