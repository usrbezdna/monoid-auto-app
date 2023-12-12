from algs import generate_alg, pdf_alg
import sys
import threading
from queue import Queue

from re import match
from menu import setup_goback_action, setup_menu
from PyQt5.QtCore import QRegExp, QSize
from PyQt5.QtGui import QFont, QIcon, QRegExpValidator, QPixmap
from PyQt5.QtWidgets import (QGridLayout, QLabel, QLineEdit, QMainWindow,
                             QMessageBox, QPushButton, QWidget)

sys.path.insert(0, 'src/algs')


class GenerateWindow(QMainWindow):
    def __init__(self, dialog_window):
        super().__init__()
        self.dialog_window = dialog_window
        self.grid_layout = None
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(QSize(600, 200))
        self.setWindowTitle('Окно генерации таблиц переходов ДКА')
        self.setWindowIcon(QIcon('resources\\choose.png'))

        menu_bar = setup_menu(self)
        setup_goback_action(self, self.dialog_window, menu_bar)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.grid_layout = QGridLayout()
        central_widget.setLayout(self.grid_layout)
        self.grid_layout.setSpacing(5)

        variants_line = self.current_line('Введите количество вариантов (1-30):',
                                          '([1-9]|[1-2][0-9]|30)', 'от 1 до 30', 0)
        nodes_line = self.current_line('Введите количество вершин (3 или 4):',
                                       '3|4', '3 или 4', 1)
        symbols_line = self.current_line(
            'Введите количество символов в алфавите (2 или 3):', '2|3', '2 или 3', 2)

        ok_button = QPushButton('OK', self)
        ok_button.setFont(QFont('Arial', 13))
        ok_button.clicked.connect(
            lambda: self.get_files(
                variants_line,
                nodes_line,
                symbols_line))

        self.grid_layout.addWidget(ok_button, 3, 1)

    def current_line(self, text, reg_exp, tip, row):
        label = QLabel(text, self)
        label.setFont(QFont('Arial', 13))

        line = QLineEdit(self)
        line.setValidator(QRegExpValidator(QRegExp(reg_exp)))
        line.setToolTip(tip)
        line.setFont(QFont('Arial', 13))

        self.grid_layout.addWidget(label, row, 0)
        self.grid_layout.addWidget(line, row, 1)

        return line

    def get_files(self, variants_number, nodes_number, symbols_number):
        if (variants_number.text() == '' or
                nodes_number.text() == '' or
                symbols_number.text() == ''):
            self.get_msg_box('Одно или несколько полей ещё не заполнены!',
                             'resources\\warning.png')
        elif match('([1-9]|[1-2][0-9]|30)', variants_number.text()) is None:
            self.get_msg_box('Неверное значение в первом поле!',
                             'resources\\warning.png')
        else:

            self.get_msg_box(
                'Запущен процесс генерации таблиц, дождитесь его окончания',
                'resources\\info2.png')

            queue = Queue()
            th = threading.Thread(
                target=generate_alg.generate, args=(
                    int(
                        variants_number.text()), int(
                        nodes_number.text()), int(
                        symbols_number.text()), queue))

            th.start()
            th.join()

            start_tables = queue.get()
            monoid_tables = queue.get()
            cayley_tables = queue.get()

            thread_list = []
            thread_list.append(threading.Thread(target=pdf_alg.pdf4_tables, args=(
                'gen_files/start_tables', 'Variants', int(nodes_number.text()), *start_tables)))
            thread_list.append(threading.Thread(target=pdf_alg.pdf4_tables, args=(
                'gen_files/monoid_tables', 'Monoid Tables', int(nodes_number.text()), *monoid_tables)))
            thread_list.append(
                threading.Thread(
                    target=pdf_alg.pdf4_cayley,
                    args=(
                        'gen_files/cayley_tables',
                        *cayley_tables)))

            for th in thread_list:
                th.start()

            for th in thread_list:
                th.join()

            self.get_msg_box(
                'Файлы вариантов таблиц переходов ДКА и ответы на них созданы!' +
                ' Их можно найти в директории gen_files, где располагаются файлы программы. ',
                'resources\\info2.png')

    def get_msg_box(self, text, pixmap_path):
        msg_box = QMessageBox(self)

        msg_box.setWindowIcon(QIcon('resources\\choose.png'))
        msg_box.setWindowTitle('Создание файлов')

        msg_box.setText(text)
        msg_box.setIconPixmap(QPixmap(pixmap_path))
        msg_box.exec_()
