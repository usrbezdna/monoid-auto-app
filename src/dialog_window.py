from http.client import FAILED_DEPENDENCY
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, QRegExp
from PyQt5.QtGui import *


class ChoosingButton(QPushButton):

    """
    Represents QPushButton with linked action
    (Closes choose window and opens new one)
    """

    def __init__(self, text, func_close, icon_path):
        super().__init__(text)

        self.clicked.connect(func_close)
        self.setIcon(QtGui.QIcon(icon_path))
        self.setGeometry(200, 150, 100, 40)
        self.setFont(QFont('Times', 14))


class ModeChooseWindow(QMainWindow):

    """
    This window allows user to choose type
    of functionality he is willing to get
    """

    def __init__(self, form_window):
        super().__init__()
        self.form_window = form_window

        self.setMinimumSize(QSize(480, 230))
        self.setWindowTitle("Выбор режима работы")

        self.setWindowIcon(QtGui.QIcon('resources\\choose.png'))

        menu = self.getMenu()

        layout = QVBoxLayout()

        layout.addWidget(
            ChoosingButton(
                " Режим построения моноида ДКА по таблице",
                self.form_on_clicked,
                'resources\\form.png'))
        layout.addWidget(
            ChoosingButton(
                " Режим генерации ДКА из 3-4 вершин",
                self.generate_on_clicked,
                'resources\\generate.jpg'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        widget.show()

    def form_on_clicked(self):
        self.close()
        print("Режим ввода таблицы построения")
        self.form_window.show()

    def generate_on_clicked(self):
        self.close()
        print("Режим генерации ДКА")

    def getMenu(self):
        menuBar = QMenuBar(self)

        info = QAction("О приложении", self)
        info.triggered.connect(self.get_info)
        menuBar.addAction(info)

        feedBack = QAction("Обратная связь", self)
        feedBack.triggered.connect(self.get_feedback)
        menuBar.addAction(feedBack)

        self.setMenuBar(menuBar)

    def get_info(self):
        msg_box = QMessageBox(self)

        msg_box.setWindowTitle("Информация о приложении")
        msg_box.setText(
            "Данное приложение предназначано для создания моноида ДКА по таблице переходов"
            ", а также для генерации таблицы Кэли для этого автомата.\n\n"
            "Кроме того, есть также режим "
            "генерации 20-30 вариантов таблиц переходов ДКА из 3-4 вершин для студентов.")

        msg_box.setIconPixmap(QPixmap('resources\\info2.png'))

        msg_box.exec_()

    def get_feedback(self):
        msg_box = QMessageBox(self)

        msg_box.setWindowTitle("Обратная связь с разработчиками")
        msg_box.setText(
            "Чтобы связаться с разработчиками приложения и сообщить о недочетах "
            "(или высказать предложения) - легче всего написать им в Telegram: @usrBezdna или @andreykaf1")

        msg_box.setIconPixmap(QPixmap('resources\\feedback.png'))

        msg_box.exec_()
