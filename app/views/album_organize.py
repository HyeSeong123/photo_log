from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QProgressBar, QPushButton, QDialog, QFileDialog
from PyQt5.QtCore import Qt,QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil

class OrganizeThread(QThread):
    progress_updated = pyqtSignal(int)
    completed = pyqtSignal()
    
    def __init__(self, source_folder, target_folder, folder_name, save_path, parent=None):
        super().__init__(parent)
        self.source_folder = source_folder
        self.target_folder = target_folder
        self.folder_name = folder_name
        self.save_path = save_path
        
    def run(self):
        total_files = 0
        processed_files = 0
        
        for root, dirs, files in os.walk(self.source_folder):
            total_files += len([file for file in files if file.lower().endswith((".jpg", ".jpeg", ".png"))])
            
        for root, dirs, files in os.walk(self.source_folder):
            for file in files:
                if file.lower().endswith((".jpg", ".jpeg", ".png")):
                    file_path = os.path.join(root, file)
                    taken_date = self.extract_taken_date(file_path)
                    if not taken_date:
                        continue
                    
                    date_folder = os.path.join(self.save_path, taken_date)
                    os.makedirs(date_folder, exist_ok=True)
                    
                    new_file_path = os.path.join(date_folder, file)
                    shutil.copy(file_path, new_file_path)
                    
                    processed_files += 1
                    progress = int((processed_files / total_files) * 100)
                    self.progress_updated.emit(progress)
        
        self.completed.emit()
        
    def extract_taken_date(self, file_path):
        file_name = os.path.basename(file_path)
        try:
            timestamp = int(file_name.split('.')[0])
            if len(str(timestamp)) == 13:
                timestamp = timestamp / 1000
                
            date = datetime.fromtimestamp(timestamp)
            return date.strftime("%Y-%m-%d")
        except (ValueError, OSError):
            pass
        
        if file_name.startswith("KakaoTalk_"):
            try:
                date_str = file_name.split("_")[1].split(".")[0]
                print(f"date_str={date_str}")
                return datetime.strptime(date_str, "%Y%m%d").strftime("%Y-%m-%d")
            except ValueError:
                pass
            
        try:
            image = Image.open(file_path)
            exif_data = image._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if tag_name == "DateTimeOriginal":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d")
        except Exception as e :
            print(f"EXIF 데이터를 읽을 수 없습니다: {e}")
        
        return datetime.now().strftime("%Y-%m-%d")
class AlbumOrganize(QWidget):
    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.main_window = main_window
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 90)

        button_style = """
            QPushButton {
                background-color: #f8f9fa;
                border: 2px solid #dedede;
                border-radius : 10px;
                font-size: 14px;
                color : #3e2723;
            }
            QPushButton:hover {
                background-color: #d7ccc8;
            }
        """
        
        input_style = """
            QLineEdit {
                border: 2px solid #dedede;
                border-radius: 10px;
                padding: 5px;
                font-size: 14px;
                color: #3e2723;
            }
            QLineEdit:focus {
                border: 2px solid #d7ccc8;
            }
        """
        
        progress_style = """
            QProgressBar {
                border: 2px solid #dedede;
                border-radius: 10px;
                text-align: center;
                font-size: 14px;
                color: #3e2723;
            }
            QProgressBar::chunk{
                background-color: #d7ccc8;
                border-radius: 10px;
            }
        """
        source_folder_button = QPushButton("정리 폴더 선택")
        source_folder_button.setObjectName("source_folder_button")
        source_folder_button.clicked.connect(self.select_folder)
        layout.addWidget(source_folder_button, alignment=Qt.AlignCenter)
        
        self.source_folder_input = QLineEdit()
        self.source_folder_input.setPlaceholderText("정리할 폴더 경로")
        self.source_folder_input.setReadOnly(True)
        layout.addWidget(self.source_folder_input, alignment=Qt.AlignCenter)
        
        target_folder_button = QPushButton("저장 폴더 선택")
        target_folder_button.setObjectName("target_folder_button")
        target_folder_button.clicked.connect(self.select_folder)
        layout.addWidget(target_folder_button, alignment=Qt.AlignCenter)
        
        self.target_folder_input = QLineEdit()
        self.target_folder_input.setPlaceholderText("저장할 폴더 경로")
        self.target_folder_input.setReadOnly(True)
        layout.addWidget(self.target_folder_input, alignment=Qt.AlignCenter)
        
        self.folder_name_input = QLineEdit()
        self.folder_name_input.setPlaceholderText("폴더 이름")
        layout.addWidget(self.folder_name_input, alignment=Qt.AlignCenter)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar, alignment=Qt.AlignCenter)
        
        start_button = QPushButton("정리하기")
        start_button.clicked.connect(self.start_organize)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)
        
        back_button = QPushButton("뒤로가기")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)
        
        buttons = [source_folder_button, target_folder_button, start_button, back_button]
        for button in buttons:
            button.setStyleSheet(button_style)
            button.setFixedSize(150,40)
        
        inputs = [self.source_folder_input, self.target_folder_input, self.folder_name_input]
        for input_box in inputs:
            input_box.setStyleSheet(input_style)
            input_box.setFixedSize(300, 30)
            
        self.progress_bar.setStyleSheet(progress_style)
        self.progress_bar.setFixedSize(300,30)
        
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
    
    def select_folder(self):
        sender = self.sender()
        folder_path = QFileDialog.getExistingDirectory(self, f"{sender.text()}")
        print(folder_path)
        if folder_path:
            if sender.objectName() == "source_folder_button":
                self.source_folder_input.setText(folder_path)
            elif sender.objectName() == "target_folder_button":
                self.target_folder_input.setText(folder_path)
    
    def start_organize(self):
        source_folder = self.source_folder_input.text()
        target_folder = self.target_folder_input.text()
        folder_name = self.folder_name_input.text()
        
        if not source_folder or not target_folder:
            QMessageBox.warning(self, "경고", "정리 폴더와 저장 폴더를 모두 선택해주세요")
            return
        
        if not folder_name:
            QMessageBox.warning(self, "경고", "폴더 이름을 입력해주세요.")
            return
        
        save_path = os.path.join(target_folder, folder_name)
        os.makedirs(save_path, exist_ok=True)

        self.progress_bar.setValue(0)
        
        self.organize_thread = OrganizeThread(source_folder, target_folder, folder_name, save_path)
        self.organize_thread.progress_updated.connect(self.update_progress_bar)
        self.organize_thread.completed.connect(self.on_organize_complete)
        self.organize_thread.start()
        
    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)
    
    def on_organize_complete(self):
        QMessageBox.information(self, "완료", "사진 정리가 완료되었습니다.")
    
    def save_to_db(self, path, name ,taken_date):
        cursor = self.conn.cursor()
        created_at = datetime.now().strftime("%Y-%m-%d")
        updated_at = created_at
        
        cursor.execute("""
                       INSERT INTO photos (origin_file_name, save_file_name, taken_date, create_dt, update_dt, path)
                       VALUES (?, ?, ?, ?, ?)
                       """ ,(name, name, taken_date, created_at, updated_at, path))
        self.conn.commit()
        
    def go_back(self):
        if self.main_window:
            self.main_window.go_back_to_main()