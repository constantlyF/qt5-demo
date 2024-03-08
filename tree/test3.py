import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.index)

    def columnCount(self, parent=None):
        return len(self._data.columns)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建示例数据
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'Los Angeles', 'Chicago']
        }
        df = pd.DataFrame(data)

        # 创建 Pandas 模型
        model = PandasModel(df)

        # 创建表格视图
        table_view = QTableView()
        table_view.setModel(model)

        self.setCentralWidget(table_view)
        self.setWindowTitle('Pandas in PyQt5')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
