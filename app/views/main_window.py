from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel,QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("앨범 프로그램")
        self.setGeometry(100, 100, 800, 1000)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.add_buttons()
    
    
    def add_buttons(self):
        organize_button = QPushButton("사진 정리")
        view_button = QPushButton("사진 보기")
        exit_button = QPushButton("종료")
        
        
        self.layout.addWidget(organize_button)
        self.layout.addWidget(view_button)
        self.layout.addWidget(exit_button)