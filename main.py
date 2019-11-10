import sys
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QDate
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QFormLayout, QLineEdit, QDialog
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.setWindowTitle("Expresso")
        


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())