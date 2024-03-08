import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget
from login import Ui_Login


class MyMainWindow(QWidget, Ui_Login):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
