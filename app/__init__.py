import logging
import os
from app.database.__init__ import initialize_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

BASE_DIR = os.path.dirname("../")
DB_PATH = os.path.join(BASE_DIR, "image_db", "album.db")

if not os.path.exists(os.path.dirname(DB_PATH)):
    os.makedirs(os.path.dirname(DB_PATH))

print(f"Database Path: {DB_PATH}")

initialize_db()

logging.info("앱 초기화 완료")