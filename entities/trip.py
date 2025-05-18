from mysql.connector import Error
from persistence.db import get_connection

class Trip:

    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country

    @classmethod
    def get(cls):
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT id, name, city, country FROM trip')
            trips = cursor.fetchall()
            return trips
        except Error as e:
            return {"error": str(e)}
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @classmethod
    def save(cls, trip):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO trip (name, city, country) VALUES (%s, %s, %s)', (trip.name, trip.city, trip.country))
            connection.commit()
            return cursor.lastrowid # Devuelve el ID de la ciudad recién registrada
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()
            