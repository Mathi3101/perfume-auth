import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mathi@310100",     # replace this
        database="perfume_auth"
    )
