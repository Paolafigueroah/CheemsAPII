import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='cheemstour.c1gciu680qg5.us-east-2.rds.amazonaws.com',
        user='admin',
        password='Lapiz123',
        database='cheemstour'
    )

    