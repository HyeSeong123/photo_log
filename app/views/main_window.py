from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLineEdit, QProgressBar
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont, QFontDatabase
from PyQt5.QtCore import Qt
from .album_organize import AlbumOrganize
from .photo_view import PhotoViewFrame
import os

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Photo Log")
        self.setGeometry(100,100,1000,1000)
        font_path = os.path.abspath("resources/font/BMDOHYEON_ttf.ttf")
        if os.path.exists(font_path):
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id != -1:
                self.custom_font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            else:
                print("폰트 로드 실패")
                self.custom_font_family = "Arial"  # 기본 폰트로 대체
        else:
            print("폰트 파일을 찾을 수 없음")
            self.custom_font_family = "Arial"  # 기본 폰트로 대체
            
        self.central_stack = QStackedWidget(self)
        self.setCentralWidget(self.central_stack)
        
        self.main_frame = self.create_main_frame()
        self.central_stack.addWidget(self.main_frame)
        
        self.organize_frame = AlbumOrganize(self.central_stack, self)
        self.central_stack.addWidget(self.organize_frame)
        
        self.photo_view_frame = PhotoViewFrame(self.central_stack, self)
        self.central_stack.addWidget(self.photo_view_frame)
        
        self.central_stack.setCurrentWidget(self.main_frame)
        # self.set_background("D:/python_project/test_V2/photo_log/resources/img/album_img.webp")
        self.set_background(os.path.abspath("resources/img/album_img.webp"))
    def set_background(self, img_path):
        if os.path.exists(img_path):
            pixmap = QPixmap(img_path).scaled(
                self.width(),
                self.height(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(pixmap))
            self.setPalette(palette)
        else:
            print(f"배경 이미지 {img_path}를 찾을 수 없습니다.")
            
        
    def create_main_frame(self):
        frame = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        custom_font = QFont(self.custom_font_family, 16)
        
        button_texts = ["사진 정리", "사진 보기", "종료"]
        for text in button_texts:
            button = QPushButton(text)
            button.setFont(custom_font)
            button.setStyleSheet(f"""
                                    QPushButton{{
                                        border: 2px solid #FFFFFF;
                                        margin-left : 60px;
                                        margin-bottom : 15px;
                                        border-radius: 15px;
                                        color: black;
                                        padding: 10px 20px;
                                        background-color: rgba(0, 0, 0, 0);
                                    }}
                                    QPushButton:hover{{
                                        background-color: rgba(255, 255, 255, 0.3);
                                        color: black;
                                    }}
                                    QPushButton:pressed{{
                                        background-color: rgba(255, 255, 255, 0.5);
                                    }}
                                 """)
            button.setCursor(Qt.PointingHandCursor)
            button.clicked.connect(self.button_action)
            layout.addWidget(button)
        
        frame.setLayout(layout)
        return frame
    
    def button_action(self):
        sender = self.sender()
        
        if sender.text() == "사진 정리":
            self.set_background(os.path.abspath("resources/img/polaroid.webp"))
            self.show_organize_frame()
        elif sender.text() == "사진 보기":
            self.show_photo_view_frame()
        elif sender.text() == "종료":
            QApplication.quit()

    def show_organize_frame(self):
        self.central_stack.setCurrentWidget(self.organize_frame)
    
    def show_photo_view_frame(self):
        self.photo_view_frame.setAutoFillBackground(True)
        self.central_stack.setCurrentWidget(self.photo_view_frame)
    
    def go_back_to_main(self):
        self.set_background(os.path.abspath("resources/img/album_img.webp"))
        self.central_stack.setCurrentWidget(self.main_frame)