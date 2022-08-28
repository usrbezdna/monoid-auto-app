from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import *
from dialog_window import *


def setup_menu(window_obj):
    menuBar = QMenuBar(window_obj)

    info = QAction("О приложении", window_obj)
    info.triggered.connect(get_info)
    menuBar.addAction(info)

    feedBack = QAction("Обратная связь", window_obj)
    feedBack.triggered.connect(get_feedback)
    menuBar.addAction(feedBack)

    window_obj.setMenuBar(menuBar)

    return menuBar


def setup_goback_action(window_obj, dialog_window, menuBar):
    goBack2dialog = QAction("Обратно к выбору режима", window_obj)
    goBack2dialog.triggered.connect(lambda: go_to_dialog(window_obj, dialog_window))
    menuBar.addAction(goBack2dialog)


def get_info():
    msg_box = QMessageBox()

    msg_box.setWindowIcon(QIcon('resources\\choose.png'))

    msg_box.setWindowTitle("Информация о приложении")
    msg_box.setText(
        "Данное приложение предназначано для создания моноида ДКА по таблице переходов"
        ", а также для генерации таблицы Кэли для этого автомата.\n\n"
        "Кроме того, есть также режим "
        "генерации 20-30 вариантов таблиц переходов ДКА из 3-4 вершин для студентов.")

    msg_box.setIconPixmap(QPixmap('resources\\info2.png'))

    msg_box.exec_()

def get_feedback():
    msg_box = QMessageBox()

    msg_box.setWindowIcon(QIcon('resources\\choose.png'))

    msg_box.setWindowTitle("Обратная связь с разработчиками")
    msg_box.setText(
        "Чтобы связаться с разработчиками приложения и сообщить о недочетах "
        "(или высказать предложения) - легче всего написать им в Telegram: @usrBezdna или @andreykaf1")

    msg_box.setIconPixmap(QPixmap('resources\\feedback.png'))

    msg_box.exec_()


def go_to_dialog(window_obj, dialog_window):
    window_obj.hide()
    dialog_window.show()
    # form_window = FormWindow()

    # ch_window = ModeChooseWindow(form_window)
    # ch_window.show()