# self.pushButton.setShortcut(_translate("MainWindow", "enter")) #设置快捷键
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QKeyEvent

from PyQt5.QtWidgets import QMessageBox
from login import Ui_login_MainWindow
from open_camera_main import *
from PyQt5.QtCore import Qt


class login_window(QtWidgets.QMainWindow, Ui_login_MainWindow):
    def __init__(self):
        super(login_window, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        self.init()
        self.admin = "帅哥"
        self.Password = "000"

    def init(self):
        self.pushButton.clicked.connect(self.login_button)  # 连接槽

    def login_button(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
            return None

        # if  self.password == self.lineEdit.text():
        if (self.lineEdit.text() == self.Password) and self.lineEdit_2.text() == self.admin:
            # Ui_Main = Open_Camera()  # 生成主窗口的实例
            # 1打开新窗口
            Ui_Main.show()
            # 2关闭本窗口
            self.close()
        else:
            QMessageBox.critical(self, '错误', '密码错误！')
            self.lineEdit.clear()
            return None


if __name__ == '__main__':
    from PyQt5 import QtCore

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应分辨率

    app = QtWidgets.QApplication(sys.argv)
    window = login_window()
    Ui_Main = Open_Camera()  # 生成主窗口的实例
    window.show()

    sys.exit(app.exec_())
