import psycopg2
from psycopg2 import sql
# Database connection parameters
DB_NAME = 'mydbsql'
DB_USER = "testuser"
DB_PASSWORD = "testpassword"
DB_HOST = 'localhost'  # Change this if your DB is hosted elsewhere
DB_PORT = '5432'       # Default PostgreSQL port

# Connect to the PostgreSQL database
def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None



