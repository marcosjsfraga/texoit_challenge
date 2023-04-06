import logging
import sqlite3
from movies.model import Movies
from database import DATABASE_URI

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_movie(movies: Movies) -> None:
    connection = sqlite3.connect(DATABASE_URI)
    cursor = connection.cursor()
    
    query = "INSERT INTO movies(id, year, title, studios, producers, winner) VALUES (?, ?, ?, ?, ?, ?)"
    
    data_values = (
        movies.id,
        movies.year,
        movies.title,
        movies.studios,
        movies.producers,
        movies.winner,
    )
    
    # cursor.execute(query, data_values)

    # connection.commit()
    cursor.close()
    connection.close()
    
    # logger.debug(f"{movies} inserted successfully to DB!")
