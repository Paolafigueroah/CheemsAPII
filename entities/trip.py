from mysql.connector import Error
from persistence.db import get_connection

class Trip:
    def __init__(self, name, city, country, latitude, longitude):
        self.name = name
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        
    @classmethod
    def get(cls):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT id, name, city, country, latitude, longitude FROM trips')
            results = cursor.fetchall()

            for trip in results:
                trip['latitude'] = float(trip['latitude']) if trip['latitude'] not in (None, '', 'null') else 0.0
                trip['longitude'] = float(trip['longitude']) if trip['longitude'] not in (None, '', 'null') else 0.0

            return results
        except Error as e:
            print(str(e))
            return str(e)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def save(cls, trip):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO trips (name, city, country, latitude, longitude) VALUES(%s,%s,%s,%s,%s)', 
                         (trip.name, trip.city, trip.country, trip.latitude, trip.longitude))
            connection.commit()
            return cursor.lastrowid
        except Error as e:
            return str(e)
        finally: 
            cursor.close()
            connection.close()    
            
    @classmethod
    def update(cls, trip_id, trip_data):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = 'UPDATE trips SET name = %s, city = %s, country = %s, latitude = %s, longitude = %s WHERE id = %s'
            cursor.execute(query, (trip_data.name, trip_data.city, trip_data.country, trip_data.latitude, trip_data.longitude, trip_id))
            connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()
            
    @classmethod
    def delete(cls, trip_id):
        try: 
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('DELETE FROM trips WHERE id = %s', (trip_id, ))
            connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()