import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../image_db/album.db")


def get_db_connection():
    return sqlite3.connect('album.db')