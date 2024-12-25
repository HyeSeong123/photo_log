from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("앨범 정리 프로그램")
        self.setGeometry(100,100,1000,1000)
        
        self.set_background()
        
        self.add_buttons()
        
    def set_background(self):
        background_img = "D:/python_project/test_V2/photo_log/resources/img/album_img.webp"
        palette = QPalette()
        pixmap = QPixmap(background_img).scaled(self.width(), self.height(), Qt.KeepAspectRatioByExpanding,Qt.SmoothTransformation)
        palette.setBrush(QPalette.Background, QBrush(pixmap))
        self.setPalette(palette)
    
    def resizeEvent(self, event):
        self.set_background()
    
    def add_buttons(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        
        btn_layout = QVBoxLayout()
        btn_layout.setAlignment(Qt.AlignCenter)
        
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        btn_layout.addSpacerItem(spacer)
        
        button_texts = ["사진 정리", "사진 보기", "종료"]
        for text in button_texts:
            button = QPushButton(text)
            button.setStyleSheet("""
                                 QPushButton {
                                     background-color: rgba(0, 0, 0, 0.6);
                                     border: 2px solid #FFFFFF;
                                     border-radius: 15px;
                                     margin-left : 55px;
                                     margin-bottom : 15px;
                                     font-size: 16px;
                                     font-weight : bold;
                                     color: white;
                                     padding: 10px 20px;
                                 }
                                 QPushButton:hover {
                                    background-color: rgba(255,255,255, 0.3);
                                    color : black;
                                 }
                                 QPushButton:pressed {
                                     background-color: rgba(255,255,255,0.5);
                                 }
                                 """)
            button.setFont(QFont("Arial",14))
            button.setCursor(Qt.PointingHandCursor)
            button.clicked.connect(self.button_action)
            btn_layout.addWidget(button)
            
        btn_layout.addSpacerItem(spacer)
        
        central_widget = QWidget()
        central_widget.setLayout(btn_layout)
        self.setCentralWidget(central_widget)
        
    def button_action(self):
        sender = self.sender()
        
        if sender.text() == "사진 정리":
            print("사진 정리")
        elif sender.text() == "사진 보기":
            print("사진 보기")
        elif sender.text() == "종료":
            QApplication.quit()