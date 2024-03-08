import sys

from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QFileIconProvider


class CusQFileIconProvider(QFileIconProvider):

    @staticmethod
    def icon_folder():
        icon_provider = QFileIconProvider()
        return icon_provider.icon(QFileIconProvider.Folder)

    @staticmethod
    def icon_xlsx():
        return CusQFileIconProvider.icon_for_file_type('xlsx')

    @staticmethod
    def icon_for_file_type(file_type) -> QIcon:
        icon_provider = QFileIconProvider()
        file_info = QFileInfo(f'xxx.{file_type}')
        return QIcon(icon_provider.icon(file_info))


app = QApplication(sys.argv)

# 创建一个 QPushButton
button = QPushButton()
# 设置按钮的图标
# button.setIcon(icon_for_file_type("xxx.xlsx"))  # 替换为你想要的文件路径
button.setIcon(CusQFileIconProvider.icon_folder())  # 替换为你想要的文件路径

# 显示按钮
button.show()

sys.exit(app.exec_())
