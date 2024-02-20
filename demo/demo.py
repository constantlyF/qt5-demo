# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QTabWidget 例子


'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *

from CallFirstMainWin import MainForm


class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)
        self.tab1 = MainWindow()
        self.setTabText(0, "tab1--外部网址")
        self.tab2 = parent
        # self.tab2.show()
        self.setTabText(1, "tab2--MainWin")
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.setWindowTitle("Tab 例子")


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
    demo = TabDemo(parent=MainForm())
    demo.show()
    sys.exit(app.exec_())

# CanvasMainWindow
# CanvasApplication

