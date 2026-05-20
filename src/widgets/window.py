from PyQt6.QtWidgets import QMainWindow, QWidget

from .layouts import MainLayout


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Wallpaper Loader")
        self.mainLayout = MainLayout()

        self.container = QWidget()
        self.container.setLayout(self.mainLayout)

        self.setCentralWidget(self.container)

    def closeEvent(self, a0):
        a0.ignore()
        self.hide()
