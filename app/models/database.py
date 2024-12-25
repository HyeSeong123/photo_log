import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "album.db")

def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS photos(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       filename TEXT NOT NULL,
                       width INTEGER,
                       height INTEGER,
                       creation_date TEXT,
                       modification_date TEXT,
                       text TEXT DEFAULT NULL,
                       keywords TEXT DEFAULT NULL
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