import sys
from builtins import range, len

from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit, QLabel, QPlainTextEdit, QPushButton, QDialog, QStatusBar
from PyQt5.QtGui import QPalette, QColor, QPixmap, QImage, QPainter
#from PyQt5.QtCore import
from PyQt5 import uic
from random import randint

class Example(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.image = QImage(391, 181, QImage.Format_ARGB32_Premultiplied)

        painter = QPainter()
        painter.begin(self.image)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRect(0, 0, 391, 181)
        painter.end()
        self.label.setPixmap(QPixmap(self.image))
        self.pushButton.clicked.connect(self.run)

    def run(self):
        painter = QPainter()
        painter.begin(self.image)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawRect(0, 0, 391, 181)
        painter.end()
        painter = QPainter()
        painter.begin(self.image)
        painter.setBrush(QColor(255, 255, 0))
        o = randint(10, 100)
        painter.drawEllipse(150, 50, o, o)
        painter.end()

        self.label.setPixmap(QPixmap(self.image))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())