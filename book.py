import sys
import sqlite3
from PyQt5 import uic, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QWidget

class show_book(QWidget):
    def __init__(self, *args):
        for i in args:
            self.name = i
        super().__init__()
        uic.loadUi('book.ui', self)
        con = sqlite3.connect("librer.sqlite")
        cur = con.cursor()
        inf = cur.execute(f"""SELECT * FROM librer WHERE name = '{self.name}' """).fetchall()
        inf = inf[0]
        print(inf)
        self.pixmap = QPixmap(inf[3])
        self.smaller_pixmap = self.pixmap.scaled(181, 201, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.PICT.setPixmap(self.smaller_pixmap)
        self.NAME.setText(inf[0])
        self.AUTOR.setText(inf[1])
        self.DATE.setText(str(inf[2]))
        self.GANRE.setText(inf[4])



