import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem


def create_tree_structure(parent, data):
    for item_data in data:
        item = QTreeWidgetItem(parent, [item_data[0]])
        if len(item_data) > 1:
            item.setIcon(0, QIcon("./images/IOS.png"))
            create_tree_structure(item, item_data[1])
        else:
            item.setIcon(0, QIcon("./images/bao2.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建树形部件
    tree = QTreeWidget()
    tree.setHeaderLabels(["数据源"])

    # 添加数据
    data = [
        ("文件夹1", [
            ("文件夹1.1", [
                ("文件1",),
            ]),
            ("文件夹1.2", [
                ("文件2",),
            ]),
        ]),
        ("文件夹2", [
            ("文件夹2.1", [
                ("文件3",),
                ("文件4",),
            ]),
        ]),
    ]

    # 创建目录结构
    create_tree_structure(tree, data)

    tree.setWindowTitle("Custom Tree Structure")
    tree.resize(640, 480)
    tree.show()

    sys.exit(app.exec_())
