from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
import tkinter as tk

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("앨범 정리 프로그램")
        self.setGeometry(100,100,1000,1000)
        
        self.central_stack = QStackedWidget(self)
        self.setCentralWidget(self.central_stack)
        
        self.main_frame = self.create_main_frame()
        self.photo_view_frame = self.organize_frame()
        
        self.central_stack.addWidget(self.main_frame)
        self.central_stack.addWidget(self.photo_organize_frame)
        self.central_stack.setCurrentWidget(self.main_frame)
        
    def create_main_frame(self):
        frame = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.add_buttons()
        
    def set_background(self):
        background_img = "D:/python_project/test_V2/photo_log/resources/img/album_img.webp"
        palette = QPalette()
        pixmap = QPixmap(background_img).scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding,Qt.SmoothTransformation)
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(palette)
    
    def resizeEvent(self, event):
        self.set_background()
        
    def button_action(self):
        sender = self.sender()
        
        if sender.text() == "사진 정리":
            album_organize();
        elif sender.text() == "사진 보기":
            print("사진 보기")
        elif sender.text() == "종료":
            QApplication.quit()