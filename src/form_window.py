from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp, Qt
from PyQt5.QtGui import *
from menu import setup_menu 

class FormWindow(QMainWindow):
    
    """
    This class is responsible for creation
    table for user input of DFA
    """

    def __init__(self): 
        super().__init__()
        self.setMinimumSize(QSize(500, 350))

        self.setWindowTitle("Окно ввода таблицы переходов ДКА")
        self.setWindowIcon(QtGui.QIcon('resources\\choose.png'))
        
        setup_menu(self)

        central_widget = QWidget(self)              
        self.setCentralWidget(central_widget)      

        grid_layout = QGridLayout(self)         
        central_widget.setLayout(grid_layout)   

        table = self.create_table()
        grid_layout.addWidget(table, 0, 0)   


    def create_table(self):

        table = QTableWidget(self)  

        coloumn_cnt = 8
        row_cnt = 3

        table.setColumnCount(coloumn_cnt)     
        table.setRowCount(row_cnt)  

        hor_hdrs = [str(i+1) for i in range(coloumn_cnt)]
        print(hor_hdrs)
        vert_hdrs = [el for i, el in enumerate(list("abc")) if i < row_cnt]
        print(vert_hdrs)

        table.setHorizontalHeaderLabels(hor_hdrs)
        table.setVerticalHeaderLabels(vert_hdrs)

        for i in range(coloumn_cnt):
            table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)

        for i in range(coloumn_cnt):
              for j in range(row_cnt):
                 table.setItem(j, i, QTableWidgetItem(f"In {(i, j)}"))
                

        table.resizeColumnsToContents()

        return table