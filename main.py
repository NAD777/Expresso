import sys
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QDate
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QFormLayout, QLineEdit, QDialog
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Expresso")
        
        self.scrollLayout = QFormLayout()
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        
        self.con = sqlite3.connect("coffee")
        self.cur = self.con.cursor()

        self.refresh()

    def clean_list(self):
        while self.scrollLayout.itemAt(0) is not None:
            self.scrollLayout.itemAt(0).widget().update()
            self.scrollLayout.removeRow(0)

    def refresh(self):
        self.clean_list()
        for el in self.cur.execute("""SELECT * FROM Coffee""").fetchall():
            st = self.cur.execute(f"SELECT title FROM Degrees WHERE id='{el[2]}'").fetchone()[0]
            tp = self.cur.execute(f"SELECT title FROM Types WHERE id='{el[3]}'").fetchone()[0]
            
            self.scrollLayout.addWidget(Part(id=el[0], name=el[1], degree=st, type=tp, desc=el[4], price=el[5], size=el[6]))

    def add_part(self):
        part = Part(parent=self)
        self.scrollLayout.addRow(part)
        # part.text_edit_clicked()
    
    def mousePressEvent(self, event):
        '''When we click on an empty space the window will update list of parts'''
        self.refresh()


class Part(QWidget):
    def __init__(self, id=None, name='', degree='', type='', desc='', price='', size='', parent=''):
        super().__init__()
        uic.loadUi('part.ui', self)
        self.id = id
        self.name = name
        self.parent = parent
        self.degree = degree
        self.type = type
        self.desc = desc
        self.price = price
        self.size = size

        self.lineEdit = cQLineEdit(self)
        self.lineEdit.setStyleSheet("padding:5px;")
        self.lineEdit.setText(self.name)

        self.lineEdit.clicked.connect(self.click_line_edit)
        
        self.gridLayout.addWidget(self.lineEdit, 0, 0)

        self.gridLayout.addWidget(self.degree_text, 1, 0)
        self.gridLayout.addWidget(self.type_text, 2, 0)
        self.gridLayout.addWidget(self.textEdit, 3, 0)
        self.gridLayout.addWidget(self.price_text, 4, 0)
        self.gridLayout.addWidget(self.size_text, 5, 0)

        self.degree_text.setText("Степень обжарки: " + str(self.degree))
        self.type_text.setText(f"Тип: {str(self.type)}")
        self.textEdit.setText('Описание: ' + str(self.desc))
        self.price_text.setText("Цена: " + str(self.price))
        self.size_text.setText("Объем: " + str(self.size))

        self.type_text.hide()
        self.price_text.hide()
        self.size_text.hide()

        self.setLayout(self.gridLayout)

        self.hide()

    def click_line_edit(self):
        self.textEdit.show()

        self.degree_text.show()
        self.type_text.show()
        self.price_text.show()
        self.size_text.show()

        self.lineEdit.setStyleSheet(
                """background-color: rgb(213, 224, 252); 
                padding:5px;border-radius: 8px;""")
        self.textEdit.setStyleSheet(
                """background-color: rgb(213, 224, 252); 
                padding:5px;border-radius: 8px;""")
        self.degree_text.setStyleSheet(
                """background-color: rgb(213, 224, 252); 
                padding:5px;border-radius: 8px;""")
        self.type_text.setStyleSheet(
                """background-color: rgb(213, 224, 252); 
                padding:5px;border-radius: 8px;""")
        self.price_text.setStyleSheet(
                """background-color: rgb(213, 224, 252); 
                padding:5px;border-radius: 8px;""")
        self.size_text.setStyleSheet(
                """background-color: rgb(213, 224, 252); 
                padding:5px;border-radius: 8px;""")

    def hide(self):
        self.lineEdit.setStyleSheet(
                """background-color: rgb(255, 255, 255); 
                padding:5px;border-radius: 8px;
                border-color: black;border-width: 3px;""")
        self.textEdit.hide()
        self.degree_text.hide()
        self.type_text.hide()
        self.price_text.hide()
        self.size_text.hide()
    

class cQLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def __init__(self, widget):
        super().__init__(widget)
        self.setStyleSheet(
                """background-color: rgb(255, 255, 255); 
                padding:5px;border-radius: 8px;
                border-color: black;border-width: 3px;""")
        self.setPlaceholderText('Название')

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())