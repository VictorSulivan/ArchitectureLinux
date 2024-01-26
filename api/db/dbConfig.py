import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from the .env file
load_dotenv()


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = {
            "host": os.getenv("DATABASE_HOST"),
            "database": os.getenv("DATABASE_NAME"),
            "user": os.getenv("DATABASE_USER"),
            "password": os.getenv("DATABASE_PASSWORD"),
            "port": os.getenv("DATABASE_PORT")
        }

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
