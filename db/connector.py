# db/connector.py
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')

def get_db_connection():
    return mysql.connector.connect(
        host= os.getenv('DB_HOST'),  # Use the service name defined in docker-compose.yml
        user=os.getenv('DB_USER'),  # The user you've defined in MYSQL_USER
        password=os.getenv('MYSQL_PASSWORD'),  # The password you've defined in MYSQL_PASSWORD
        database=os.getenv('MYSQL_DATABASE')  # The database name you've defined in MYSQL_DATABASE
    )

def log_chat(input_text, output_text):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO chat_history (input_text, output_text) VALUES (%s, %s)"
    cursor.execute(query, (input_text, output_text))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_chat_history():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chat_history ORDER BY timestamp DESC")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records
