import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QPlainTextEdit, QVBoxLayout, QWidget, \
    QHBoxLayout


def create_tree_structure(parent, data):
    for item_data in data:
        item = QTreeWidgetItem(parent, [item_data[0]])
        if len(item_data) > 1:
            item.setIcon(0, QIcon("./images/IOS.png"))
            create_tree_structure(item, item_data[1])
        else:
            item.setIcon(0, QIcon("./images/bao2.png"))
            # 设置文件内容
            item.setData(0, 1000, item_data[0] + " Content")


def on_item_clicked(item):
    if item.data(0, 1000):
        content_edit.setPlainText(item.data(0, 1000))
    else:
        content_edit.setPlainText(111111)


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
    tree.resize(320, 480)

    # 创建文本编辑部件
    content_edit = QPlainTextEdit()
    content_edit.setReadOnly(True)

    # 将树形部件和文本编辑部件放在一个垂直布局中
    layout = QHBoxLayout()
    layout.addWidget(tree)
    layout.addWidget(content_edit)

    # 创建主窗口并设置布局
    main_window = QWidget()
    main_window.setLayout(layout)

    # 连接树形部件的 itemClicked 信号到槽函数
    tree.itemClicked.connect(on_item_clicked)

    main_window.show()
    sys.exit(app.exec_())
