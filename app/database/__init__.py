import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../image_db/album.db")

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
                       path TEXT NOT NULL UNIQUE
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
    
def get_connection():
    return sqlite3.connect(DB_PATH)