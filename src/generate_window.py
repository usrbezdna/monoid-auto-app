from re import match

from PyQt5.QtCore import QRegExp, QSize
from PyQt5.QtGui import QFont, QIcon, QRegExpValidator, QPixmap
from PyQt5.QtWidgets import (QGridLayout, QLabel, QLineEdit, QMainWindow,
                             QMessageBox, QPushButton, QWidget)

from menu import setup_goback_action, setup_menu


class GenerateWindow(QMainWindow):
    def __init__(self, dialog_window):
        super().__init__()
        self.dialog_window = dialog_window
        self.grid_layout = None
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(QSize(500, 200))
        self.setWindowTitle('Окно генерации таблиц переходов ДКА')
        self.setWindowIcon(QIcon('resources\\choose.png'))

        menu_bar = setup_menu(self)
        setup_goback_action(self, self.dialog_window, menu_bar)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.grid_layout = QGridLayout(self)
        central_widget.setLayout(self.grid_layout)
        self.grid_layout.setSpacing(5)

        variants_line = self.current_line('Введите количество вариантов:',
                                          '2[5-9]|30', 'от 25 до 30', 0)
        nodes_line = self.current_line('Введите количество вершин:',
                                       '3|4', '3 или 4', 1)
        symbols_line = self.current_line('Введите количество символов в алфавите:',
                                         '2|3', '2 или 3', 2)

        ok_button = QPushButton('OK', self)
        ok_button.setFont(QFont('Arial', 13))
        ok_button.clicked.connect(lambda: self.get_files(variants_line, nodes_line, symbols_line))
        self.grid_layout.addWidget(ok_button, 3, 1)

    def current_line(self, text, reg_exp, tip, row):
        label = QLabel(text, self)
        label.setFont(QFont('Times', 11))

        line = QLineEdit(self)
        line.setValidator(QRegExpValidator(QRegExp(reg_exp)))
        line.setToolTip(tip)
        line.setFont(QFont('Times', 11))

        self.grid_layout.addWidget(label, row, 0)
        self.grid_layout.addWidget(line, row, 1)

        return line

    def get_files(self, variants_number, nodes_number, symbols_number):
        if (variants_number.text() == '' or
                nodes_number.text() == '' or
                symbols_number.text() == ''):
            self.get_msg_box('Одно или несколько полей ещё не заполнены!',
                             'resources\\warning.png')
        elif match('2[5-9]|30', variants_number.text()) is None:
            self.get_msg_box('Неверное значение в первом поле!',
                             'resources\\warning.png')
        else:
            self.get_msg_box('Файлы вариантов таблиц переходов ДКА и ответы на них созданы',
                             'resources\\info2.png')

        # TODO: add output

    def get_msg_box(self, text, pixmap_path):
        msg_box = QMessageBox(self)
        msg_box.setWindowIcon(QIcon('resources\\choose.png'))
        msg_box.setWindowTitle('Создание файлов')
        msg_box.setText(text)
        msg_box.setIconPixmap(QPixmap(pixmap_path))
        msg_box.exec_()
