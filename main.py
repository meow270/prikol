from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from glavprikol import Ui_MainWindow

import sys
from uiprikol import Ui_Dialog
from ahuelui import Ui_Dialog

class Prilozhenie(QMainWindow):
    def __init__(self):
        super(Prilozhenie, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def open_if_da(self):
        self.new_window = QtWidgets.QDialog()
        self.uiprikol.setupUi(self.new_window)
        self.new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Prilozhenie()
    window.show()
    sys.exit(app.exec())