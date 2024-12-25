import sqlite3

class Photo:
    def __init__(self, photo_name, width, height, creation_date, modification_date, text=None, keywords=None):
        self.photo_name = photo_name
        self.width = width
        self.height = height
        self.creation_date = creation_date
        self.modification_date = modification_date
        self.text = text
        self.keywords = keywords
        
    def save(self):
        conn = sqlite3.connect('database/album.db')
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO photos ( photo_name, width, height, creation_date, modification_date, text, keywords)
                       VALUSE(?,?,?,?,?,?,?)
                       ''', (self.photo_name, self.width, self.height, self.creation_date, self.modification_date, self.text, self.keywords))
        conn.commit()
        conn.close()
        
        