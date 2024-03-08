import sys

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QTreeView


def create_tree_structure():
    # 创建根节点
    root_item = QStandardItem("Root")

    # 添加文件夹1
    folder1 = QStandardItem("文件夹1")
    folder1_1 = QStandardItem("文件夹1.1")
    file1 = QStandardItem("文件1")
    folder1_2 = QStandardItem("文件夹1.2")
    file2 = QStandardItem("文件2")

    # 添加文件夹1的子项
    folder1.appendRow(folder1_1)
    folder1_1.appendRow(file1)
    folder1.appendRow(folder1_2)
    folder1_2.appendRow(file2)

    # 添加文件夹2
    folder2 = QStandardItem("文件夹2")
    folder2_1 = QStandardItem("文件夹2.1")
    file3 = QStandardItem("文件3")
    file4 = QStandardItem("文件4")

    # 添加文件夹2的子项
    folder2.appendRow(folder2_1)
    folder2_1.appendRow(file3)
    folder2_1.appendRow(file4)

    # 将文件夹1和文件夹2添加到根节点
    root_item.appendRow(folder1)
    root_item.appendRow(folder2)

    return root_item


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建模型
    model = QStandardItemModel()

    # 获取目录结构
    root_item = create_tree_structure()

    # 将根节点设置为模型的根节点
    model.setItem(0, 0, root_item)

    # 创建树形视图
    tree_view = QTreeView()
    tree_view.setModel(model)
    tree_view.setWindowTitle("Custom Tree Structure")
    tree_view.resize(640, 480)
    tree_view.show()

    sys.exit(app.exec_())
