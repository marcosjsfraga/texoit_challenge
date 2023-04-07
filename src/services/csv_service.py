import pandas as pd
from models.movies_model import Movies
from repositories.movie_repository import MoviesRepository


class CSVService():

    def import_movielist(self):
        moviesRepository = MoviesRepository()
        
        csv_file = pd.read_csv('movielist.csv', delimiter=';')
        
        for index, row in csv_file.iterrows():        
            movie = Movies(
                id = index, 
                year = row['year'], 
                title = row['title'], 
                studios = row['studios'], 
                producers = row['producers'], 
                winner = 1 if row['winner'] == 'yes' else 0
            )
            
            moviesRepository.create(movie)
            

