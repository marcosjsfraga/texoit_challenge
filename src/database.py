import logging
import sqlite3
from typing import Union, Optional

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

DATABASE_URI = "database.db"
_connection: sqlite3.Connection

def init_db(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, year INTEGER, title TEXT, studios TEXT, producers TEXT, winner INTEGER);"
    )

def get_connection() -> sqlite3.Connection:
    global _connection
    _connection = sqlite3.connect(database=DATABASE_URI, check_same_thread=False)
    return _connection


def get_sql_cursor(connection: Optional[sqlite3.Connection] = None) -> sqlite3.Cursor:
    global _connection
    _connection = connection or sqlite3.connect(database=DATABASE_URI, check_same_thread=False)
    return _connection.cursor()

def get_or_create_db():
    global cursor
    cursor = get_sql_cursor()
    init_db(cursor=cursor)
    
    cursor.close()
