import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "album.db")

def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS photos(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       origin_file_name TEXT NOT NULL,
                       save_file_name TEXT,
                       taken_dt TEXT,
                       create_dt TEXT,
                       update_dt TEXT,
                       description TEXT DEFAULT NULL,
                       keywords TEXT DEFAULT NULL,
                       path TEXT NOT NULL
                   )
                ''')
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS albums(
                       id TEXT PRIMARY KEY,
                       name TEXT NOT NULL
                   )
                   ''')
    
    conn.commit()
    conn.close()
    

def get_db_connection():
    return sqlite3.connect('album.db')