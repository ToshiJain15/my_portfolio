import os
import MySQLdb
from dotenv import load_dotenv

load_dotenv()

# Connect to MySQL Server (not the specific DB yet)
try:
    db = MySQLdb.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        passwd=os.getenv('DB_PASSWORD', ''),
        port=int(os.getenv('DB_PORT', 3306))
    )
    cursor = db.cursor()
    
    db_name = os.getenv('DB_NAME', 'portfolio')
    print(f"Attempting to create database: {db_name}")
    
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
    print(f"Database '{db_name}' created successfully (or already existed).")
    
    cursor.close()
    db.close()
except Exception as e:
    print(f"Error creating database: {e}")
