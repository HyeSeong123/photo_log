from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLabel
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
import tkinter as tk
import album_organize
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
        self.photo_view_frame = self.create_photo_organize_frame()
        
        self.central_stack.addWidget(self.main_frame)
        self.central_stack.addWidget(self.photo_organize_frame)
        self.central_stack.setCurrentWidget(self.main_frame)
        
    def create_main_frame(self):
        frame = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        button_texts = ["사진 정리", "사진 보기", "종료"]
        for text in button_texts:
            button = QPushButton(text)
            button.setFont(QFont("Arial",14))
            button.setStyleSheet("""
                                    QPushButton(
                                        border: 2px solid #FFFFFF;
                                        border-radius: 15px;
                                        font-size: 16px;
                                        color: white;
                                        padding: 10px 20px;
                                        background-color: rgba(0, 0, 0, 0.6);
                                    )
                                    QPushButton:hover{
                                        background-color: rgba(255, 255, 255, 0.3);
                                        color: black;
                                    }
                                    QPushButton:pressed{
                                        background-color: rgba(255, 255, 255, 0.5);
                                    }
                                 """)
            button.setCursor(Qt.PointingHandCursor)
            button.clicked.connect(self.button_action)
            layout.addWidget(button)
        
        frame.setLayout(layout)
        return frame
    
    def create_photo_organize_frame(self):
        frame = QWidget()
        label = QLabel("앨범 정리")
        label.setFont(QFont("Arial",20))
        label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        frame.setLayout(layout)
        return frame
        
    def button_action(self):
        sender = self.sender()
        
        if sender.text() == "사진 정리":
            print("사진 보기")
        elif sender.text() == "사진 보기":
            print("사진 보기")
        elif sender.text() == "종료":
            QApplication.quit()
    
    def start_photo_organize(self):
        self.switch_frame(self.photo_organize_frame)
        
        album_organize.organize_photos()
    
    def switch_frame(self, frame):
        current_rect = self.central_stack.geometry()
        target_rect = QRect(current_rect.x() + self.width(), current_rect.y(), self.width(), self.heigth())
        
        animation = QPropertyAnimation(self.central_stack, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(current_rect)
        animation.setEndValue(target_rect)
        animation.finished.connect(lambda: self.central_stack.setCurrentWidget(frame))
        animation.start()