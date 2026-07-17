import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT", 3306)),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

    return connection


if __name__ == "__main__":
    try:
        connection = get_connection()

        if connection.is_connected():
            print("MySQL Connected Successfully!")

        connection.close()

    except Exception as e:
        print("Database Connection Error:", e)