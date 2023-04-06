import pandas as pd
from movies.model import Movies
from movies.repository import create_movie

def import_csv():
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
        
        create_movie(movie)
        

