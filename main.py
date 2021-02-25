import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('ui.ui', self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        rand = randint(0, 150)
        qp.drawEllipse(QRect(150 - rand, 150 - rand, 2 * rand, 2 * rand))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
