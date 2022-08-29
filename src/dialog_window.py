from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import *
from menu import setup_menu
from dialog_window import *
from generate_window import *
from form_window import *

class ChoosingButton(QPushButton):

    """
    Represents QPushButton with linked action
    (Closes choose window and opens new one)
    """

    def __init__(self, text, func_close, icon_path):
        super().__init__(text)

        self.clicked.connect(func_close)
        self.setIcon(QtGui.QIcon(icon_path))
        self.setGeometry(200, 150, 100, 40)
        self.setFont(QFont('Times', 14))


class ModeChooseWindow(QMainWindow):

    """
    This window allows user to choose type
    of functionality he is willing to get
    """

    def __init__(self):
        super().__init__()

        self.form_window = FormWindow(self)
        self.generate_window = GenerateWindow(self)

        self.setMinimumSize(QSize(480, 200))
        self.setWindowTitle("Выбор режима работы")

        self.setWindowIcon(QIcon('resources\\choose.png'))

        setup_menu(self)

        layout = QVBoxLayout()

        layout.addWidget(
            ChoosingButton(
                " Режим построения моноида ДКА по таблице",
                self.form_on_clicked,
                'resources\\form.png'))
        layout.addWidget(
            ChoosingButton(
                " Режим генерации ДКА из 3-4 вершин",
                self.generate_on_clicked,
                'resources\\generate.jpg'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        widget.show()

    def form_on_clicked(self):
        self.hide()
        print("Режим ввода таблицы построения")
        self.form_window.show()

    def generate_on_clicked(self):
        self.hide()
        print("Режим генерации ДКА")
        self.generate_window.show()
    
