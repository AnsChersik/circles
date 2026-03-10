
import sys
from random import randint
from PyQt6.QtCore import QPointF
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPainter
from PyQt6 import uic


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawButton.clicked.connect(self.draw_circles)
        self.should_draw = False

    def draw_circles(self):
        self.should_draw = True
        self.update()

    def paintEvent(self, event):
        if self.should_draw:
            painter = QPainter()
            painter.begin(self)
            self.render_circles(painter)
            painter.end()

    def render_circles(self, painter):
        radius = randint(20, 100)
        painter.setBrush(QColor('yellow'))
        painter.drawEllipse(
            QPointF(randint(0, 355), randint(0, 355)),
            radius,
            radius
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())