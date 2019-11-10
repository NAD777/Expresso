import sys
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QDate
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
    QFormLayout, QLineEdit, QDialog
import sqlite3
from UI.main_ui import Ui_MainWindow
from UI.addEditCoffeeForm_ui import Ui_Form
import UI.Part_ui


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Latte")
        
        self.scrollLayout = QFormLayout()
        self.scrollWidget = QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        
        self.con = sqlite3.connect("coffee")
        self.cur = self.con.cursor()

        self.add_btn.clicked.connect(self.add_part)

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
            
            self.scrollLayout.addWidget(Part(id=el[0], name=el[1], degree=st, type=tp, desc=el[4], price=el[5], size=el[6], parent=self))

    def add_part(self):
        quest = editCoffee()
        quest.show()
        quest.exec()
        self.refresh()
    
    def mousePressEvent(self, event):
        '''When we click on an empty space the window will update list of parts'''
        self.refresh()


class editCoffee(QDialog, Ui_Form):
    def __init__(self, id=None, name='', degree='', type='', desc='', price='', size=''):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Edit")
        self.id = id
        self.name = name
        self.degree = degree
        self.type = type
        self.desc = desc
        self.price = price
        self.size = size

        self.name_text.setText(str(self.name))
        self.degree_text.setText(str(self.degree))
        self.type_text.setText(str(self.type))
        self.textEdit.setText(str(self.desc))
        self.price_text.setText(str(self.price))
        self.size_text.setText(str(self.size))

        if self.id is None:
            self.accept_btn.setText("Добавить")

        self.accept_btn.clicked.connect(self.accept_method)
        self.reject_btn.clicked.connect(self.reject_method)
    
    def accept_method(self):
        self.con = sqlite3.connect('coffee')
        self.cur = self.con.cursor()
        if self.id is None:
            deg = self.cur.execute(f"""SELECT id FROM Degrees WHERE title='{self.degree_text.text()}'""").fetchone()
            if deg is None:
                self.cur.execute(f"""INSERT INTO Degrees(title) VALUES('{self.degree_text.text()}')""")
                self.con.commit()
            deg = self.cur.execute(f"""SELECT id FROM Degrees WHERE title='{self.degree_text.text()}'""").fetchone()[0]

            tp = self.cur.execute(f"""SELECT id FROM Types WHERE title='{self.type_text.text()}'""").fetchone()
            if tp is None:
                self.cur.execute(f"""INSERT INTO Types(title) VALUES('{self.type_text.text()}')""")
                self.con.commit()
            tp = self.cur.execute(f"""SELECT id FROM Types WHERE title='{self.type_text.text()}'""").fetchone()[0]
            # print(self.cur.insert_id())
            self.cur.execute(f"""INSERT INTO Coffee(name, degree, type, desc, price, size) VALUES('{self.name_text.text()}', 
                    '{deg}', '{tp}', '{self.textEdit.toPlainText()}', '{self.price_text.text()}', '{self.size_text.text()}')""")
            self.con.commit()
        else:
            deg = self.cur.execute(f"""SELECT id FROM Degrees WHERE title='{self.degree_text.text()}'""").fetchone()
            if deg is None:
                self.cur.execute(f"""INSERT INTO Degrees(title) VALUES('{self.degree_text.text()}')""")
                self.con.commit()
            deg = self.cur.execute(f"""SELECT id FROM Degrees WHERE title='{self.degree_text.text()}'""").fetchone()[0]

            tp = self.cur.execute(f"""SELECT id FROM Types WHERE title='{self.type_text.text()}'""").fetchone()
            if tp is None:
                self.cur.execute(f"""INSERT INTO Types(title) VALUES('{self.type_text.text()}')""")
                self.con.commit()
            tp = self.cur.execute(f"""SELECT id FROM Types WHERE title='{self.type_text.text()}'""").fetchone()[0]
            self.cur.execute(f"""UPDATE Coffee SET name='{self.name_text.text()}', degree='{deg}', type='{tp}', desc='{self.textEdit.toPlainText()}',
                    price='{self.price_text.text()}', size='{self.size_text.text()}' WHERE id='{self.id}'""")
            self.con.commit()
        self.accept()

    def reject_method(self):
        self.reject()


class Part(QWidget, UI.Part_ui.Ui_Form):
    def __init__(self, id=None, name='', degree='', type='', desc='', price='', size='', parent=''):
        super().__init__()
        self.setupUi(self)
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
        self.lineEdit.setText(str(self.name))

        self.lineEdit.clicked.connect(self.click_line_edit)
        self.delete_btn.clicked.connect(self.delete_self)
        self.edit_btn.clicked.connect(self.edit_self)
        
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

    def edit_self(self):
        quest = editCoffee(id=self.id, name=self.name, degree=self.degree, type=self.type, desc=self.desc, price=self.price, size=self.size)
        quest.show()
        quest.exec()
        self.parent.refresh()

    def delete_self(self):
        self.con = sqlite3.connect("coffee")
        self.cur = self.con.cursor()
        self.cur.execute(f"""DELETE FROM Coffee WHERE id={self.id}""")
        self.con.commit()
        self.parent.refresh()

    def click_line_edit(self):
        self.textEdit.show()

        self.degree_text.show()
        self.type_text.show()
        self.price_text.show()
        self.size_text.show()
        self.edit_btn.show()
        self.delete_btn.show()

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
        self.edit_btn.hide()
        self.degree_text.hide()
        self.type_text.hide()
        self.price_text.hide()
        self.size_text.hide()
        self.delete_btn.hide()
    

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