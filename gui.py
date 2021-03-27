import sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import numpy

class Label(QtWidgets.QLabel):
    def __init__(self, parent, mainwindowobj, x, y, bx, by):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(y, x, 90, 90))
        mainwindowobj.button_list.update({(x, y): self})

        self.setFont(mainwindowobj.standard_font)
        self.font().setPointSize(150)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setObjectName("label")
        self.setStyleSheet('''#label{border: 12px solid #bbada0;
                                                     background-color: rgba(238, 228, 218, 0.35)}''')

        self.bx = bx
        self.by = by


class Gui(QtWidgets.QMainWindow):
    def setupUI(self):
        super().__init__()
        self.button_list = {}
        # setting standard font
        self.standard_font = QtGui.QFont()
        self.standard_font.setBold(True)
        self.standard_font.setPointSize(36)
        self.standard_font.setWeight(75)
        self.standard_font.setFamily('Comic Sans Ms')

        # setting stacked widget
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.stacked_widget.setCurrentIndex(0)

        self.setFixedSize(278, 236)
        self.home_screen = QtWidgets.QWidget()
        self.home_screen.setObjectName('home_screen')
        self.home_screen.setStyleSheet('''
                                            #home_screen{background-image: url('images/home_screen_background.jpg');
                                            background-repeat: no-repeat;
                                                         }''')
        self.play_button = QtWidgets.QPushButton(self.home_screen)
        self.play_button.setGeometry(QtCore.QRect(52, 61, 151, 91))
        self.play_button.setFont(self.standard_font)
        self.play_button.setText('Play')
        self.play_button.setObjectName('play_button')
        self.play_button.setStyleSheet('''
                        #play_button{background: rgba(255,255,255,30);}
                        ''')
        self.play_button.clicked.connect(self.on_click_play_button)
        self.stacked_widget.addWidget(self.home_screen)

        self.play_screen = QtWidgets.QWidget()
        self.exit_button = QtWidgets.QPushButton(self.play_screen)
        self.exit_button.setGeometry(QtCore.QRect(10, 20, 401, 41))
        self.exit_button.clicked.connect(self.on_click_exit)
        self.exit_button.setFont(self.standard_font)
        self.exit_button.setText('Exit')
        for x in enumerate([90, 190, 290, 390]):
            for y in enumerate([10, 110, 210, 310]):
                label = Label(self.play_screen, self, x[1], y[1], x[0], y[0])

        self.stacked_widget.addWidget(self.play_screen)

        self.stacked_widget.setCurrentIndex(0)


    def on_click_play_button(self):

        self.setFixedSize(410, 490)
        self.refresh_play()
        self.stacked_widget.setCurrentIndex(1)
        self.set_label_according_to_board()

    def on_click_exit(self):
        self.setFixedSize(278, 236)
        self.board = numpy.zeros((4, 4), dtype='int32')
        self.stacked_widget.setCurrentIndex(0)
        self.refresh_play()
        self.generate_random()
        self.generate_random()

    def refresh_play(self):
        for items in self.button_list.values():
            items.setText('')
            items.setObjectName("label")
            items.setStyleSheet('''#label{border: 12px solid #bbada0;
                                    background-color: rgba(238, 228, 218, 0.35)}''')
