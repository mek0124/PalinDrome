from PySide6 import QtWidgets as qtw
from src.main_window import Ui_MainWindow
import sys


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("Palindrome Checker")
        self.setStyleSheet("background: linear-gradient(145deg, rgb(254,144,173), rgb(254,85,140), rgb(254,85,140));")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.pb_Cancel.clicked.connect(self.close)
        self.pb_Check.clicked.connect(self.check_palindrome)

    def check_palindrome(self):
        orig_word = self.le_WordToCheck.text()
        backwards = orig_word[::-1]

        self.is_error = True if backwards != orig_word else False

        self.le_OriginalWord.setText(orig_word)
        self.le_WordBackwards.setText(backwards)

        self.le_OriginalWord.setEnabled(False)
        self.le_WordBackwards.setEnabled(False)

        if self.is_error:
            self.le_ResultLabel.setText("False")
            self.le_ResultLabel.setStyleSheet("color: red;")
        else:
            self.le_ResultLabel.setText("True")
            self.le_ResultLabel.setStyleSheet("color: green;")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())    