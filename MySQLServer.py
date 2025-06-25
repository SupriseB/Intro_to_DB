import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (adjust user/password/host as needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    cursor = connection.cursor()

    # Try creating database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

except mysql.connector.Error as err:
    print(f"Failed to connect to MySQL: {err}")

finally:
    # Close cursor and connection if they were opened
    try:
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
    except:
        pass
