from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Application.Data import Data
from Application.Settings import Settings
from Application.StartOfWork import StartOfWork


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setWindowTitle("Main")
        self.move(300,300)
        self.resize(856,572)
        #Why doesn't work
        oImage = QPixmap("./Application/man.png")
        sImage = oImage.scaled(856, 572)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        labelStart = QPushButton("Старт",self)
        labelSettings = QPushButton("Настройки",self)
        labelExit = QPushButton("Выход",self)

        labelStart.move(375,125)
        labelStart.resize(100,50)
        labelStart.setFont(QFont("Times", 10))
        labelStart.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 4px;}"
                              "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        labelStart.setCursor(QCursor(Qt.PointingHandCursor))
        labelStart.mousePressEvent = self.Start

        labelSettings.move(625,160)
        labelSettings.resize(100,50)
        labelSettings.setFont(QFont("Times", 10))
        labelSettings.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 4px;}"
                              "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        labelSettings.setCursor(QCursor(Qt.PointingHandCursor))
        labelSettings.mousePressEvent = self.Settings

        labelExit.move(100,100)
        labelExit.resize(100,50)
        labelExit.setFont(QFont("Times", 10))
        labelExit.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 4px;}"
                              "QPushButton:pressed {background-color:rgb(31,101,163) ; }")
        labelExit.setCursor(QCursor(Qt.PointingHandCursor))
        labelExit.mousePressEvent = self.Exit

    def Start(self, event):
        self.start = StartOfWork()
        self.start.show()
        self.close()
    def Settings(self,event):
        data = Data()
        self.settings = Settings(data)
        self.settings.show()
        self.close()
    def Exit(self,event):
        self.close()