import os
import sys

from src import Application

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    app = Application()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
