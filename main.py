from app.views.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
