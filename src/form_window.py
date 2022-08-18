from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import *

class FormWindow(QMainWindow):
    
    """
    This class is responsible for creation
    table for user input of DFA
    """

    def __init__(self): 
        super().__init__()
        self.setMinimumSize(QSize(800, 600))

        self.setWindowTitle("Окно ввода таблицы переходов ДКА")

        
