from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp, Qt
from PyQt5.QtGui import *

from table import *
from monoid_window import *
from menu import setup_menu, setup_goback_action



class FormWindow(QMainWindow):

    """
    This class is responsible for creation
    table for user input of DFA
    """

    def __init__(self, dialog_window):

        super().__init__()

        self.setMinimumSize(QSize(500, 350))

        self.setWindowTitle("Окно ввода таблицы переходов ДКА")
        self.setWindowIcon(QtGui.QIcon('resources\\choose.png'))

        self.monoid_window = MonoidWindow()

        menu_bar = setup_menu(self)
        setup_goback_action(self, dialog_window, menu_bar)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        table = create_input_table(3, 3)
        self.table = table

        btn1, btn2, btn3, btn4, clr_btn, proc_btn = self.create_btns()

        qvbox_layout = QVBoxLayout()
        self.add2_col_layout(qvbox_layout, 10, btn1, btn2)

        qhbox_layout = QHBoxLayout()
        self.add2_row_layout(qhbox_layout, 10, btn3, btn4)

        grid_layout.addLayout(qvbox_layout, 0, 3)
        grid_layout.addLayout(qhbox_layout, 3, 0)

        grid_layout.setSpacing(30)

        grid_layout.addWidget(self.table, 0, 0)
        grid_layout.addWidget(clr_btn, 3, 3)
        grid_layout.addWidget(proc_btn, 2, 3)

    def create_btns(self):
        buttons = [QPushButton(bnt_txt) for bnt_txt in [
            "Добавить столбец",
            "Удалить столбец",
            "Добавить строку",
            "Удалить строку",
            "Очистить таблицу",
            "Построить моноид"]
        ]

        for button in buttons:
            button.setFont(QFont('Arial', 13))

        buttons[0].clicked.connect(
            lambda: redraw_input_table(
                self,
                self.table.columnCount() + 1,
                self.table.rowCount()))
        buttons[1].clicked.connect(
            lambda: redraw_input_table(
                self,
                self.table.columnCount() - 1,
                self.table.rowCount()))

        buttons[2].clicked.connect(
            lambda: redraw_input_table(
                self,
                self.table.columnCount(),
                self.table.rowCount() + 1))
        buttons[3].clicked.connect(
            lambda: redraw_input_table(
                self,
                self.table.columnCount(),
                self.table.rowCount() - 1))

        buttons[4].clicked.connect(lambda: clear_table(self))
        buttons[5].clicked.connect(lambda: self.monoid_window.redraw_monoid_window(self))

        return buttons

    def add2_col_layout(self, qvbox_layout, spacing, *buttons):
        qvbox_layout.setSpacing(spacing)
        for button in buttons:
            qvbox_layout.addWidget(button, 0, Qt.AlignTop)
        qvbox_layout.addStretch()

    def add2_row_layout(self, qhbox_layout, spacing, *buttons):
        qhbox_layout.setSpacing(spacing)
        for button in buttons:
            qhbox_layout.addWidget(button, 0, Qt.AlignLeft)
        qhbox_layout.addStretch()
