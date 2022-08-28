from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp, Qt
from PyQt5.QtGui import *

class MonoidWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(600, 650))

        self.setWindowTitle("Моноид для введённого ДКА")
        self.setWindowIcon(QtGui.QIcon('resources\\choose.png'))

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        qhbox_layout = QHBoxLayout()
        central_widget.setLayout(qhbox_layout)


        monoid_table = QTableWidget()
        cayley_table = QTableWidget()


        qhbox_layout.addWidget(monoid_table, 0, Qt.AlignTop)
        qhbox_layout.addWidget(cayley_table, 0, Qt.AlignTop)    

        qhbox_layout.setSpacing(50)
        qhbox_layout.addStretch()


    
    def show_monoid_window(self, form_window):
        self.move(form_window.geometry().right() + 10, form_window.geometry().top() + 10)
        self.show()


        print('Showed', self)