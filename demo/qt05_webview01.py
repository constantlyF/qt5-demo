import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('打开外部网页例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # 加载外部页面
        self.browser.load(QUrl('https://bd.cailian.net/#/login'))

        self.setCentralWidget(self.browser)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setAttribute(Qt.AA_UseDesktopOpenGL)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())