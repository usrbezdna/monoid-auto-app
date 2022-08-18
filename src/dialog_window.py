from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import *


class ChoosingButton(QPushButton):

    """
    Represents QPushButton with linked action
    (Closes choose window and opens new one)
    """

    def __init__(self, text, func_close):
        super().__init__(text)

        self.clicked.connect(func_close)


class ModeChooseWindow(QMainWindow):

    """
    This window allows user to choose type 
    of functionality he is willing to get
    """

    def __init__(self, form_window):
        super().__init__()
        self.form_window = form_window

        self.setMinimumSize(QSize(480, 200))
        self.setWindowTitle("Выбор режима работы")

        self.setWindowIcon(QtGui.QIcon('..//resources/choose.png'))

        layout = QVBoxLayout()

        layout.addWidget(
            ChoosingButton(
                "Режим построения моноида ДКА по таблице",
                self.form_on_clicked))
        layout.addWidget(
            ChoosingButton(
                "Режим генерации ДКА из 3-4 вершин",
                self.generate_on_clicked))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        widget.show()

    def form_on_clicked(self):
        self.close()
        print("Режим ввода таблицы построения")
        self.form_window.show()
        

    def generate_on_clicked(self):
        self.close()
        print("Режим генерации ДКА")

