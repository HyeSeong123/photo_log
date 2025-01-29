import sqlite3

class Photo:
    def __init__(self, db_path):
        print(f"db_path: {db_path}")
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        
    def fetch_photos_by_date(self):
        query = """
        SELECT CREATION_DATE, FILE_NAME, FILE_PATH FROM PHOTOS
        ORDER BY CREATION_DT ASC;
        """
        self.cursor.execute(query)
        photos = self.cursor.fetchall()
        result = {}
        
        for date, name, path in photos:
            if date not in result:
                result[date] = []
                result[date].append({'name': name, 'path': path})
        return result