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
        producer_got_2_awards_faster_list = {
            'producer': '',
            'interval': 100,
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
            print(producer['name'], last_name)
            
            if last_name == producer['name']:
                print('EQ NAMES')
                interval = producer['year'] - last_year
                print(interval, producer_got_2_awards_faster_list['interval'])
                
                if producer_got_2_awards_faster_list['interval'] > interval:
                    producer_got_2_awards_faster_list['producer'] = producer['name']
                    producer_got_2_awards_faster_list['interval'] = interval
                    producer_got_2_awards_faster_list['previousWin'] = last_year
                    producer_got_2_awards_faster_list['followingWin'] = producer['year']
                
            else:
                last_name = producer['name']
                last_year = producer['year']


            # Produtor com maior intervalo entre dois prêmios consecutivos
            
            # Produtor que obteve dois prêmios mais rápido
            # interval = row[2] - row[1]
            # if len(producer_got_2_awards_faster_list) == 0:
            #     producer_got_2_awards_faster_list.append({
            #         'name': row[0], 
            #         'interval': interval
            #     })
            # else:
            #     if producer_got_2_awards_faster_list.interval > interval:
            #         producer_got_2_awards_faster_list.name = row[0]
            #         producer_got_2_awards_faster_list.interval = interval
        
        
        print(producer_got_2_awards_faster_list)
        
        return { 'detail': 'Get producers by prize ranges.' }
        