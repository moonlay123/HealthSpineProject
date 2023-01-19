import sys

from PyQt5.QtWidgets import QApplication

from Application.Data import Data
from Application.MainWindow import MainWindow
from Application.Profiles import Profiles
from Application.Settings import Settings
from Application.StartOfWork import StartOfWork

data = Data()
data.save()
app = QApplication(sys.argv)
win = MainWindow()
#win1 = StartOfWork()
#win2 = Settings(data)
#win3 = Profiles()
win.show()
#win1.show()
#win2.show()
#win3.show()
sys.exit(app.exec_())