from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class Profiles(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        names = ["Павел", "Максим", "Артем", "Алексей"]
        layout = QGridLayout(self)
        self.setObjectName("Profiles")
        self.setWindowTitle("Profiles")
        self.move(300, 300)
        self.resize(700, 450)
        self.setStyleSheet(
            '''
            background-color: rgb(73,93,120)
            '''
        )

        title = QLabel("Добро пожаловать! Кто в данный момент\nсидит за компьютером?",self)
        title.move(125,25)
        title.setFont(QFont("Times", 14, QFont.Bold))
        title.setStyleSheet('''color: rgb(255, 255, 255);''')
        title.adjustSize()
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title,0,0,1,3)
        many_buttons = 4
        column = 1
        sizes = (250, 50)
        btn = ButtonFabric("Кнопка", sizes)
        for step in range(many_buttons):
            btn = ButtonFabric(names[step], sizes)
            layout.addWidget(btn, 1+step // column, 1+step % column,2,1)


class ButtonFabric(QPushButton):
    def __init__(self, text, size):  # !!!
        super().__init__()

        self.setText(f'{text}')  # !!! {text} {num}
        self.setFixedSize(*size)  # !!! (*size)
        self.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 4px;}"
                               "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        self.setFont(QFont("Times", 14, QFont.Bold))
