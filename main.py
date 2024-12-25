from app.views.main_window import MainWindow
from PyQt5.QtWidgets import QApplication

def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
