import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "album.db")

def get_connection():
    return sqlite3.connect(DB_PATH)