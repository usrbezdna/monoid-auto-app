from custom_warn import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, QRegExp, Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from turtle import color
from algs import monoid_alg, cayley_alg
import sys
sys.path.insert(0, '~/src/algs')


def create_table(coloumn_cnt, row_cnt):

    table = QTableWidget()

    table.setColumnCount(coloumn_cnt)
    table.setRowCount(row_cnt)

    form_headers(table, coloumn_cnt, row_cnt)

    for i in range(coloumn_cnt):
        for j in range(row_cnt):
            new_item = create_table_item()
            table.setItem(j, i, new_item)

    table.resizeColumnsToContents()
    return table


def create_table_item():

    item = QTableWidgetItem()
    item.setData(Qt.EditRole, 0)

    item.setBackground(QtGui.QColor(75, 180, 75))
    item.setTextAlignment(Qt.AlignCenter)

    return item


def form_headers(table, coloumn_cnt, row_cnt):

    hor_hdrs = [str(i + 1) for i in range(coloumn_cnt)]
    vert_hdrs = [
        el for i, el in enumerate(
            list("abcdefg")[
                0:row_cnt]) if i < row_cnt]

    table.setHorizontalHeaderLabels(hor_hdrs)
    table.horizontalHeader().setFont(QFont('Times', 14))

    table.setVerticalHeaderLabels(vert_hdrs)
    table.verticalHeader().setFont(QFont('Times', 14))

    for i in range(coloumn_cnt):
        table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignCenter)

    for i in range(row_cnt):
        table.verticalHeaderItem(i).setTextAlignment(Qt.AlignCenter)


def clear_table(self):

    for i in range(self.table.columnCount()):
        for j in range(self.table.rowCount()):
            self.table.item(j, i).setData(Qt.EditRole, 0)
    self.repaint()


def redraw_table(self, new_col_size, new_row_size):

    if new_col_size > 5 or new_row_size > 3 or new_col_size < 2 or new_row_size < 2:
        show_size_warning()
        return

    self.table.setColumnCount(new_col_size)
    self.table.setRowCount(new_row_size)

    form_headers(self.table, new_col_size, new_row_size)

    for i in range(new_col_size):
        for j in range(new_row_size):
            if self.table.item(j, i) is None:
                new_item = create_table_item()
                self.table.setItem(j, i, new_item)

    self.table.resizeColumnsToContents()
    self.repaint()


def read_table_vals(self):
    alpha = "abcdefg"
    model = self.table.model()
    tuple_list = []

    for row in range(model.rowCount()):
        int_list = []
        for column in range(model.columnCount()):
            index = model.index(row, column)

            value = model.data(index)
            if value < 0 or value > model.columnCount():
                show_val_warning(value, row, column)
                return

            int_list.append(value)
        tuple_list.append((alpha[row], int_list))

    
    print(monoid_alg.monoid_table(tuple_list))

    return tuple_list
