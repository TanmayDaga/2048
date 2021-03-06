# color dict
import sys

from gui import Gui
from logic import Board
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5 import Qt as forevent
from PyQt5.QtCore import Qt
import numpy

bg_color = {
    '':'',
    '2': '#eee4da',
    '4': '#ede0c8',
    '8': '#edc850',
    '16': '#edc53f',
    '32': '#f67c5f',
    '64': '#f65e3b',
    '128': '#edcf72',
    '256': '#edcc61',
    '512': '#f2b179',
    '1024': '#f59563',
    '2048': '#edc22e',
}
color = {
    '':'#776e65',
    '2': '#776e65',
    '4': '#776e65',
    '8': '#f9f6f2',
    '16': '#f9f6f2',
    '32': '#f9f6f2',
    '64': '#f9f6f2',
    '128': '#f9f6f2',
    '256': '#f9f6f2',
    '512': '#776e65',
    '1024': '#f9f6f2',
    '2048': '#f9f6f2',
}


class ExtendedGui(Gui, Board):

    def __init__(self):
        super().__init__()
        self.setupUI()
        # self.generate_random()
        self.set_label_according_to_board()

    def set_label_according_to_board(self):
        for x in range(4):
            for y in range(4):
                if self.board[x][y] != 0:
                    for items in self.button_list.values():
                        if items.bx == x:
                            if items.by == y:
                                items.setText(str(self.board[x][y]))
                                items.update()
                else:
                    for items in self.button_list.values():
                        if items.bx == x:
                            if items.by == y:
                                items.setText('')
        self.set_color()

    def set_color(self):
        for items in self.button_list.values():
            bgColor = bg_color[items.text()]
            Color = color[items.text()]

            items.setStyleSheet(f'''#label{{background-color: {bgColor};
                                            color: {Color}  
                                          }}''')

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        compress_val = None
        if (a0.type() == forevent.QKeyEvent.KeyPress) and (a0.key() == Qt.Key_Down):
            compress_val = self.down_swipe()
            self.set_label_according_to_board()


        elif (a0.type() == forevent.QKeyEvent.KeyPress) and (a0.key() == Qt.Key_Up):
            compress_val = self.up_swipe()
            self.set_label_according_to_board()

        elif (a0.type() == forevent.QKeyEvent.KeyPress) and (a0.key() == Qt.Key_Right):
            compress_val = self.right_swipe()
            self.set_label_according_to_board()

        elif (a0.type() == forevent.QKeyEvent.KeyPress) and (a0.key() == Qt.Key_Left):
            compress_val = self.left_swipe()
            self.set_label_according_to_board()
        if self.check_win_game_over(compress_val) == False:

            loose_box = QtWidgets.QMessageBox()
            loose_box.setText("You lost the game")
            loose_box.setWindowTitle('You loose')
            loose_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            loose_box.buttonClicked.connect(self.on_click_exit)
            loose_box.exec_()
        elif self.check_win_game_over(compress_val) == True:
            win_box = QtWidgets.QMessageBox()
            win_box.setText("You won the game")
            win_box.setWindowTitle("You Won")
            win_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            win_box.buttonClicked.connect(self.on_click_exit)
            win_box.exec_()
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = ExtendedGui()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
