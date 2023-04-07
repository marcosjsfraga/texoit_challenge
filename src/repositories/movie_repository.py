from configs.database import Database


class MoviesRepository():

    def __init__(self):
        self.database = Database()
        
    def create(self, movies):
        connection = self.database.get_connection()
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
        
        cursor.execute(query, data_values)
        connection.commit()

        cursor.close()
        connection.close()
        