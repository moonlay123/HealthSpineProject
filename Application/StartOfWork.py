from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import *

from Application.Data import Data
from Application.Settings import Settings
from PoseController.FatigueDetect import FatigueDetect

class StartOfWork(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.setObjectName("StartOfWork")
        self.setWindowTitle("StartOfWork")
        self.move(300, 300)
        self.resize(575, 450)
        self.setStyleSheet(
            '''
            background-color: rgb(73,93,120)
            '''
        )

        title = QLabel("Введите начальные данные",self)
        title.move(125,25)
        title.setFont(QFont("Times", 14, QFont.Bold))
        title.setStyleSheet('''color: rgb(255, 255, 255);''')
        title.adjustSize()

        label1 = QLabel("Расстояние между вашими зрачками:",self)
        label1.move(25,100)
        label1.setFont(QFont("Times", 10))
        label1.setStyleSheet('''color: rgb(255, 255, 255);''')
        label1.adjustSize()

        edit1 = QLineEdit(self)
        edit1.resize(100,50)
        edit1.move(425,90)
        edit1.setFont(QFont("Times", 14))
        edit1.setAlignment(Qt.AlignCenter)
        edit1.setText("60")
        edit1.setStyleSheet("""
                QLineEdit{
                    border: 2px solid #FFFFFF;
                    border-radius: 10px;
                    color: rgb(255, 255, 255);
                }
                """)


        label2 = QLabel("Диагональ вашего монитора:",self)
        label2.move(25,200)
        label2.setFont(QFont("Times", 10))
        label2.setStyleSheet('''color: rgb(255, 255, 255);''')
        label2.adjustSize()

        edit2 = QLineEdit(self)
        edit2.resize(100, 50)
        edit2.move(425, 185)
        edit2.setFont(QFont("Times", 14))
        edit2.setAlignment(Qt.AlignCenter)
        edit2.setText("56")
        edit2.setStyleSheet("""
                        QLineEdit{
                            border: 2px solid #FFFFFF;
                            border-radius: 10px;
                            color: rgb(255, 255, 255);
                        }
                        """)

        label3 = QLabel("При отсутствии Ваших данных будут использоваться стандартные", self)
        label3.move(25, 300)
        label3.setFont(QFont("Times", 10))
        label3.setStyleSheet('''color: rgb(255, 255, 255);''')
        label3.adjustSize()

        startButton = QPushButton("Старт",self)
        startButton.resize(200,50)
        startButton.setFont(QFont("Times",14))
        startButton.move(200,375)
        startButton.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        startButton.setCursor(QCursor(Qt.PointingHandCursor))
        startButton.mousePressEvent = self.Start

    def Start(self,event):
        #self.fatigueDetect = FatigueDetect()
        #self.fatigueDetect.logic()
        data = Data()
        self.settings = Settings(data)
        self.settings.show()
        self.settings.showMinimized()
        self.close()


