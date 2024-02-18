import sys
from PyQt5 import QtWidgets

# 查询类或者对象的所有属性
print(dir(QtWidgets))
# 查看类的说明文档
print(help(QtWidgets))
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("hello qt5")
widget.show()
sys.exit(app.exec_())
