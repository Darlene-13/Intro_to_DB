import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv('.env')

# Configure the database connection
config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '#Nasimiyu1'),
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'port': os.getenv('DB_PORT', 3306),
    'database': os.getenv('DB_NAME', 'alx_book_store')
}

# Create connection to MySQL server
def create_connection():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        cursor.close()
        connection.close()
        if connection.is_connected():
            print("Database 'alx_book_store' created successfully!")
            return connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    

# Open and close the database connection
def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    connection = create_connection()
    close_connection(connection)
# This script creates a connection to a MySQL database using credentials from a .env file.