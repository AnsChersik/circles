
import sys
from random import randint
from PyQt6.QtCore import QPointF
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor, QPainter
from classui import Ui_MainWindow


class CircleDrawer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        painter.setBrush(QColor(*[randint(0, 255) for i in range(3)]))
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