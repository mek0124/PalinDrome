from PySide6 import QtWidgets as qtw
from ui.main_window import Ui_MainWindow

import sys
import os
import importlib.util


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Define color palette
        self.colors = {
            'primary': '#fe558c',    # (254,85,140)
            'secondary': '#ff6b9b',  # (255,107,155)
            'tertiary': '#fe90ad',   # (254,144,173)
            'light': '#fda9c1',      # (253,169,193)
            'lightest': '#fec1d3',   # (254,193,211)
        }

        self.setupUi(self)
        self.setWindowTitle("Palindrome Checker")

        # Apply gradient background using the color palette
        self.setStyleSheet(f"""
            QMainWindow {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 {self.colors['tertiary']},
                    stop:0.5 {self.colors['secondary']},
                    stop:1 {self.colors['primary']});
            }}
            QGroupBox {{
                border: 2px solid {self.colors['primary']};
                border-radius: 8px;
                margin-top: 1ex;
                background-color: rgba(255, 255, 255, 180);
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 5px;
                color: {self.colors['primary']};
            }}
            QPushButton {{
                background-color: {self.colors['primary']};
                color: white;
                border-radius: 4px;
                padding: 6px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.colors['secondary']};
            }}
            QLineEdit {{
                border: 1px solid {self.colors['tertiary']};
                border-radius: 4px;
                padding: 4px;
            }}
            QLabel {{
                color: {self.colors['primary']};
                font-weight: bold;
            }}
        """)

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
            self.le_ResultLabel.setStyleSheet(f"color: red; font-weight: bold; font-size: 16px;")
        else:
            self.le_ResultLabel.setText("True")
            self.le_ResultLabel.setStyleSheet(f"color: green; font-weight: bold; font-size: 16px;")


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())