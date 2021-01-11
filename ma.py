import sqlite3
import sys

import shutil
from random import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from book import show_book


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.CP.addItem("name")
        self.CP.addItem("autor")
        self.GL = []
        self.PB.clicked.connect(self.choiseBook)

    def choiseBook(self):
        for i in reversed(range(self.VL.count())):
             self.VL.itemAt(i).widget().setParent(None)
        con = sqlite3.connect("librer.sqlite")
        cur = con.cursor()
        esult = []
        print(self.CP.currentText(), self.LE.text())
        for i in cur.execute(f"""SELECT name FROM librer WHERE {self.CP.currentText()} = '{self.LE.text()}' """).fetchall():
            esult.append(i[0])
            print(i[0])
        for i in esult:
            a = QPushButton(i)
            a.clicked.connect(self.onClick)
            self.GL.append(a)
            self.VL.addWidget(a)

    def onClick(self):
        self.r = show_book(self, self.sender().text())
        self.r.show()














def except_hook(cls, exception, traceback):
        sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = ex
    sys.exit(app.exec_())
