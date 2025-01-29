from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QGridLayout
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt
from tkinter import Tk, Frame, Label, Button, Canvas, Scrollbar
from ..models.photo import Photo
from PIL import Image, ImageTk
from ..models.database import get_db_connection
import os

class PhotoViewFrame(QWidget):
    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, Qt.black)
        self.setPalette(palette)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)
        
        self.title = QLabel("사진 보기", self)
        self.title.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("font-size: 24px; font-weight: bold; color:white;")
        layout.addWidget(self.title)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QGridLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        layout.addWidget(self.scroll_area)
        
        self.load_photos()
    
    def load_photos(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        photos = Photo.fetch_photos_by_date()
        if not photos:
            no_photos_label = QLabel("저장된 사진이 없습니다.")
            no_photos_label .setStyleSheet("font-size : 18px; color:white;")
            self.scroll_layout.addWidget(no_photos_label, 0, 0, Qt.AlignCenter)
            return
        
        for i, photo in enumerate(photos):
            photo_path = photo['path']
            if os.path.exists(photo_path):
                pixmap = QPixmap(photo_path).scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                photo_label = QLabel(self.scroll_content)
                photo_label.setPixmap(pixmap)
                self.scroll_layout.addWidget(photo_label, i // 4, i % 4)
        
        conn.commit()
        conn.close()
        self.completed.emit()