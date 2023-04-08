import pandas as pd
from models.movies_model import Movies
from repositories.movies_repository import MoviesRepository


class CSVService():

    def import_movielist(self):
        movies_repository = MoviesRepository()
        rows_imported = 0
        
        movies_repository.delete_all_rows()
        
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
            
            movies_repository.create(movie)
            
            rows_imported += 1
            
        return { 'detail': 'File already imported', 'rows_imported': rows_imported }
