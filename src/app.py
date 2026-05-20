import sys

from PyQt6.QtWidgets import QApplication

from .core import SingletonManager
from .widgets import Window


class Application(QApplication):
    def __init__(self) -> None:
        super().__init__([])
        self.window = Window()
        self.singletonManager = SingletonManager("linux_wallpapermanager_gui")
        self.singletonManager.showUI.connect(self.showUI)

        if not self.singletonManager.startServer():
            sys.exit(0)

    def showUI(self, show: bool) -> None:
        if show:
            self.window.show()

    def exec(self) -> int:
        return super().exec()
