import sys
import io
import sqlite3
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        # abc = io.StringIO(template)
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.create(qp)
        # Завершаем рисование
        qp.end()
        self.create(qp)

    def create(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        a = randint(1, 100)
        x, y = randint(a, 800 - a), randint(a, 600 - a)
        qp.drawEllipse(QPoint(int(x), int(y)), a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
