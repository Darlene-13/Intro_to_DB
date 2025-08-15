import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Imorting .env file to get database credentials
load_dotenv('.env') 

config = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT', 3306),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def create_db_connection():
    # Try to establish a connection to the database
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print( "Connection to the database was successful.")
            return connection
    except Error as e:
        print(f"Error while connecting to the database: {e}")
        return None
    
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    
    # Create a database connection
    db_connection = create_db_connection()
    
    if db_connection:
        # Close the connection if it was successful
        db_connection.close()
        print("Database connection closed.")
    else:
        print("Failed to connect to the database.")