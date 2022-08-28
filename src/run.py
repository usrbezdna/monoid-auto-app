from PyQt5.QtWidgets import *
from dialog_window import *
from form_window import *

import sys


def main():
    """
    This is an entry point of the program
    """

    app = QApplication(sys.argv)

    # TODO: add basic functionality
    # generate_window = GenerateWindow()

    ch_window = ModeChooseWindow()
    ch_window.show()

    app.exec()


if __name__ == '__main__':
    main()
