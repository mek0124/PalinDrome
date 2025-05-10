from PySide6 import QtWidgets as qtw
import sys
import os
import importlib.util

# Try different import approaches to handle both development and packaged environments
try:
    # First try the development import path
    from src.main_window import Ui_MainWindow
except ImportError:
    try:
        # Then try the local import path
        from main_window import Ui_MainWindow
    except ImportError:
        # Finally, try to load the module dynamically from the packaged location
        try:
            # Get the directory where the script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Try to find main_window.py in the same directory
            main_window_path = os.path.join(script_dir, "main_window.py")

            if not os.path.exists(main_window_path):
                # If not found, look in the parent directory
                main_window_path = os.path.join(os.path.dirname(script_dir), "main_window.py")

            if os.path.exists(main_window_path):
                # Load the module dynamically
                spec = importlib.util.spec_from_file_location("main_window", main_window_path)
                main_window_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(main_window_module)
                Ui_MainWindow = main_window_module.Ui_MainWindow
            else:
                # If all else fails, copy the UI class directly
                from src.app.main_window import Ui_MainWindow
        except Exception as e:
            print(f"Error importing Ui_MainWindow: {e}")
            raise


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