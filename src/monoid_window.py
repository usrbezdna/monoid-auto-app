
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp, Qt
from PyQt5.QtGui import *

from table import *
import sys
sys.path.insert(0, 'src/algs')

from cayley_alg import (cayley_table, group_check,
                        inverse_element_check, zero_element_check)
from monoid_alg import monoid_table


class MonoidWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.zero_data = None
        self.inverse_data = None
        self.group_data = None
        self.setMinimumSize(QSize(650, 700))

        self.setWindowTitle("Моноид для введённого ДКА")
        self.setWindowIcon(QtGui.QIcon('resources\\choose.png'))

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        qhbox_layout = QHBoxLayout()
        qvbox_layout = QVBoxLayout()
        central_widget.setLayout(qvbox_layout)

        monoid_table_size = QSize(round(self.width() / 2), self.height() - 100)
        self.monoid_table = QTableWidget()

        self.monoid_table.setMaximumSize(monoid_table_size)
        self.monoid_table.setMinimumSize(monoid_table_size)

        self.cayley_table = QTableWidget()

        self.cayley_table.setMaximumSize(QSize(self.width() * 2, self.height() - 100))
        self.cayley_table.setMinimumSize(monoid_table_size)

        self.monoid_properties = QPushButton('Характеристика моноида', self)
        self.monoid_properties.setFont(QFont('Arial', 11))
        self.monoid_properties.clicked.connect(lambda:
                                               self.get_properties(self.zero_data,
                                                                   self.inverse_data,
                                                                   self.group_data))

        qhbox_layout.addWidget(self.monoid_table, 0, Qt.AlignVCenter)
        qhbox_layout.addWidget(self.cayley_table, 0, Qt.AlignVCenter)
        qvbox_layout.addLayout(qhbox_layout)
        qvbox_layout.addWidget(self.monoid_properties, 0, Qt.AlignRight)
        qvbox_layout.setAlignment(Qt.AlignCenter)

        qhbox_layout.setSpacing(30)


    def redraw_monoid_window(self, form_window):

        table_vars = read_table_vals(form_window)
        if table_vars is None:
            return

        monoid_data = monoid_table(table_vars)
        cayley_data = cayley_table(monoid_data)
        self.zero_data = zero_element_check(cayley_data)
        self.inverse_data = inverse_element_check(cayley_data)
        self.group_data = group_check(cayley_data)

        self.move(form_window.geometry().right() + 10, form_window.geometry().top() + 10)

        fill_monoid_table(self.monoid_table, monoid_data)
        fill_cayley_table(self.cayley_table, cayley_data, monoid_data)

        self.show()

    def get_properties(self, zero_data, inverse_data, group_data):
        msg_box = QMessageBox(self)
        msg_box.setWindowIcon(QIcon('resources\\choose.png'))
        msg_box.setWindowTitle('Характеристика моноида')
        msg_box.setIconPixmap(QPixmap('resources\\info2.png'))
        msg_box.setText('Нули моноида:\n'
                        f'Левые нули: {", ".join(zero_data[0]) if len(zero_data[0]) != 0 else "нет"}\n'
                        f'Правые нули: {", ".join(zero_data[1]) if len(zero_data[1]) != 0 else "нет"}\n'
                        f'Нули: {", ".join(zero_data[2]) if len(zero_data[2]) != 0 else "нет"}\n\n'
                        f'Обратимые моноида:\n'
                        f'Левые обратимые: {", ".join(inverse_data[0]) if len(inverse_data[0]) != 0 else "нет"}\n'
                        f'Правые обратимые: {", ".join(inverse_data[1]) if len(inverse_data[1]) != 0 else "нет"}\n'
                        f'Обратимые: {", ".join(inverse_data[2]) if len(inverse_data[2]) != 0 else "нет"}\n\n'
                        f'Данный моноид {"является группой" if group_data[0] else "не является группой"}'
                        f'{", причём коммутативной" if group_data[1] else ""}')
        msg_box.exec_()
