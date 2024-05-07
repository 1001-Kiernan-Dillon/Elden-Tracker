import psycopg2

def db_connect():
    # Database connection parameters
    params = {
        "dbname": "Elden_Tracker",
        "user": "postgres",
        "password": "password",
        "host": "localhost"
    }

    # Connect to the PostgreSQL database
    return psycopg2.connect(**params)
