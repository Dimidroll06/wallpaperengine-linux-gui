import sys

from PyQt6.QtWidgets import QApplication

from .widgets.window import Window


class Application(QApplication):
    def __init__(self) -> None:
        super().__init__(sys.argv)
        self.window = Window()
        self.window.show()

    def exec(self) -> int:
        return super().exec()
