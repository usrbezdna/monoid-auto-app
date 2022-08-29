from custom_warn import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, QRegExp, Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui


def create_input_table(coloumn_cnt : int, row_cnt : int):

    table = QTableWidget()

    table.setColumnCount(coloumn_cnt)
    table.setRowCount(row_cnt)

    form_input_headers(table, coloumn_cnt, row_cnt)

    for i in range(coloumn_cnt):
        for j in range(row_cnt):
            new_item = create_table_item(0, QtGui.QColor(75, 180, 75))
            table.setItem(j, i, new_item)

    table.resizeColumnsToContents()
    return table


def create_table_item(value : int, color : QtGui.QColor):

    item = QTableWidgetItem()
    item.setData(Qt.EditRole, value)

    item.setBackground(color)
    item.setTextAlignment(Qt.AlignCenter)

    return item

def fill_monoid_table(table : QTableWidget, monoid_data : list[tuple[str, list[int]]]):
    
    table.setColumnCount(len(monoid_data[0][1]))
    table.setRowCount(len(monoid_data))

    form_monoid_headers(table, monoid_data)
    table.resizeColumnsToContents()

    for i, tuple_ in enumerate(monoid_data):
        for j, int_val in enumerate(tuple_[1]):
            new_item = create_table_item(int_val, QtGui.QColor(85, 195, 250))
            table.setItem(i, j, new_item)

def fill_cayley_table(table : QTableWidget, cayley_data : list[list[str]], monoid_data : list[tuple[str, list[int]]]):
    
   table.setColumnCount(len(monoid_data))
   table.setRowCount(len(monoid_data))

   form_cayley_headers(table, monoid_data)
   table.resizeColumnsToContents()

   for i, list_1 in enumerate(cayley_data):
        for j, el in enumerate(list_1):
            new_item = create_table_item(el, QtGui.QColor(250, 140, 60))
            table.setItem(i, j, new_item)


def form_input_headers(table, coloumn_cnt, row_cnt):

    hor_hdrs = [str(i + 1) for i in range(coloumn_cnt)]
    vert_hdrs = [
        el for i, el in enumerate(
            list("abcdefg")[
                0:row_cnt]) if i < row_cnt]

    setup_headers_style(table, hor_hdrs, vert_hdrs)

def form_monoid_headers(table, monoid_data):

    hor_hdrs = [str(i + 1) for i in range(len(monoid_data[0][1]))]
    vert_hdrs = [tuple_[0] for tuple_ in monoid_data]

    setup_headers_style(table, hor_hdrs, vert_hdrs)


def form_cayley_headers(table, monoid_data):
    hor_hdrs = vert_hdrs = [tuple_[0] for tuple_ in monoid_data]

    setup_headers_style(table, hor_hdrs, vert_hdrs)


def setup_headers_style(table, hor_hdrs, vert_hdrs):

    table.setHorizontalHeaderLabels(hor_hdrs)
    table.horizontalHeader().setFont(QFont('Times', 14))

    table.setVerticalHeaderLabels(vert_hdrs)
    table.verticalHeader().setFont(QFont('Times', 14))

    for i in range(table.columnCount()):
        table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignCenter)

    for i in range(table.rowCount()):
        table.verticalHeaderItem(i).setTextAlignment(Qt.AlignCenter)



def clear_table(self):
    for i in range(self.table.columnCount()):
        for j in range(self.table.rowCount()):
            self.table.item(j, i).setData(Qt.EditRole, 0)
    self.repaint()


def redraw_input_table(self, new_col_size, new_row_size):
    if new_col_size > 5 or new_row_size > 3 or new_col_size < 2 or new_row_size < 2:
        show_size_warning()
        return

    self.table.setColumnCount(new_col_size)
    self.table.setRowCount(new_row_size)

    form_input_headers(self.table, new_col_size, new_row_size)

    for i in range(new_col_size):
        for j in range(new_row_size):
            if self.table.item(j, i) is None:
                new_item = create_table_item(0, QtGui.QColor(75, 180, 75))
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

    return tuple_list
