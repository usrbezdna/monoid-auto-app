from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QPixmap


def show_size_warning():
    msg_box = QMessageBox()

    msg_box.setWindowIcon(QIcon('resources\\choose.png'))

    msg_box.setWindowTitle("Предупреждение")
    msg_box.setText(
        "Вы не можете иметь таблицу с размерами больше чем 5x3"
        " или меньше, чем 2x2, так как это нецелесообразно. ")

    msg_box.setIconPixmap(QPixmap('resources\\warning.png'))

    msg_box.exec_()


def show_val_warning(value, row, column):
    msg_box = QMessageBox()

    msg_box.setWindowIcon(QIcon('resources\\choose.png'))

    msg_box.setWindowTitle("Ошибка в заполнении таблицы")
    msg_box.setText(
        "Элементы в таблице переходов ДКА должны быть строго положительными, "
        "при этом их значение не должно превышать максимальную вершину! "
        f"\n\n Элемент {value} в позиции ({column+1}, {row+1}) это нарушает.")

    msg_box.setIconPixmap(QPixmap('resources\\warning.png'))

    msg_box.exec_()
