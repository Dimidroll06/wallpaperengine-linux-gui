import sys

from src import Application


def main():
    app = Application()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
