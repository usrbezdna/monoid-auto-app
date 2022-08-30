
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp, Qt
from PyQt5.QtGui import *

from table import *
import sys
sys.path.insert(0, 'src/algs')

from cayley_alg import cayley_table
from monoid_alg import monoid_table


class MonoidWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(650, 700))

        self.setWindowTitle("Моноид для введённого ДКА")
        self.setWindowIcon(QtGui.QIcon('resources\\choose.png'))

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        qhbox_layout = QHBoxLayout()
        central_widget.setLayout(qhbox_layout)

        monoid_table_size = QSize(self.width() / 2, self.height() - 100)
        self.monoid_table = QTableWidget()

        self.monoid_table.setMaximumSize(monoid_table_size)
        self.monoid_table.setMinimumSize(monoid_table_size)

        self.cayley_table = QTableWidget()

        self.cayley_table.setMaximumSize(QSize(self.width() * 2, self.height() - 100))
        self.cayley_table.setMinimumSize(monoid_table_size)


        qhbox_layout.addWidget(self.monoid_table, 0, Qt.AlignVCenter)
        qhbox_layout.addWidget(self.cayley_table, 0, Qt.AlignVCenter)    

        qhbox_layout.setSpacing(30)
       

    def redraw_monoid_window(self, form_window):

        table_vars = read_table_vals(form_window)
        if table_vars is None:
            return

        monoid_data = monoid_table(table_vars)
        cayley_data = cayley_table(monoid_data)    

        self.move(form_window.geometry().right() + 10, form_window.geometry().top() + 10)

        fill_monoid_table(self.monoid_table, monoid_data)
        fill_cayley_table(self.cayley_table, cayley_data, monoid_data)

        self.show()
