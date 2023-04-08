from configs.database import Database

        
class MoviesRepository():

    def __init__(self):
        self.database = Database()

    def create(self, movies):
        connection = self.database.get_connection()
        cursor = connection.cursor()
        
        query = 'INSERT INTO movies(id, year, title, studios, producers, winner) VALUES (?, ?, ?, ?, ?, ?)'
        
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

    def delete_all_rows(self):
        connection = self.database.get_connection()
        cursor = connection.cursor()

        query = 'DELETE FROM movies'
        
        cursor.execute(query)
        connection.commit()        

        cursor.close()
        connection.close()
        
    def get_producers_by_prize_ranges(self):
        connection = self.database.get_connection()
        cursor = connection.cursor()
        producers_list = []
        producer_got_2_awards_faster = {
            'producer': '',
            'interval': 100,
            'previousWin': 0,
            'followingWin': 0
        }
        producer_with_longest_gap_between_two_awards = {
            'producer': '',
            'interval': 0,
            'previousWin': 0,
            'followingWin': 0
        }
                
        last_name = ''
        last_year = 0
        
        query = """
            SELECT producers, year
            FROM movies
            WHERE winner = 1
            ORDER BY producers, year
        """
        cursor.execute(query)

        for row in cursor.fetchall():
            names = row[0].replace(' and ', ', ').split(', ')
            for name in names:
                producers_list.append({
                    'name': name, 
                    'year': row[1]
                })
            
        # Sort list by name, year
        producers_list = sorted(producers_list, key=lambda x: (x['name'], x['year']))

        for producer in producers_list:
            if last_name == producer['name']:
                interval = producer['year'] - last_year

                if producer_got_2_awards_faster['interval'] > interval:
                    producer_got_2_awards_faster['producer'] = producer['name']
                    producer_got_2_awards_faster['interval'] = interval
                    producer_got_2_awards_faster['previousWin'] = last_year
                    producer_got_2_awards_faster['followingWin'] = producer['year']

                if producer_with_longest_gap_between_two_awards['interval'] < interval:
                    producer_with_longest_gap_between_two_awards['producer'] = producer['name']
                    producer_with_longest_gap_between_two_awards['interval'] = interval
                    producer_with_longest_gap_between_two_awards['previousWin'] = last_year
                    producer_with_longest_gap_between_two_awards['followingWin'] = producer['year']
            else:
                last_name = producer['name']
                last_year = producer['year']

        return { 
                'min': [
                    producer_got_2_awards_faster
                ], 
                'max': [
                    producer_with_longest_gap_between_two_awards
                ] 
            }
