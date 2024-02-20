import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTabWidget, QMainWindow, QApplication


class ZLConfig:
    home_url = "https://sx.cailian.net/#/"
    configs = {
        "工作台": "https://sx.cailian.net/#/TheoryCourse/TeachingClass",
        "项目": "https://sx.cailian.net/#/TheoryCourse/CourseLibrary",
        "大数据库": "https://eduresourcesx.cailian.net/#/subjectSet/subject?timestamp=1708342816114",
        "数据应用": "https://sx.cailian.net/#/TheoryCourse/Evaluation",
        "人工智能": None,
        "权限管理": "https://sx.cailian.net/#/n-educa/teacher",
    }
    configs_kes: list = list(configs.keys())

    @staticmethod
    def get_index(key):
        return ZLConfig.configs_kes.index(key)

    @staticmethod
    def get_value(index):
        return ZLConfig.configs[ZLConfig.configs_kes[index]]


class ZLTabWidget(QTabWidget):
    def __init__(self):
        super(ZLTabWidget, self).__init__()
        for title in ZLConfig.configs.keys():
            index = self.addTab(QWebEngineView(), title)
            self.widget(index).setUrl(QUrl(ZLConfig.home_url))
        self.setWindowTitle("中联")
        self.currentChanged.connect(self.tab_changed)

    def tab_changed(self, index):
        url = ZLConfig.get_value(index)
        print(f'url->{url};index->{index}')
        self.widget(index).setUrl(QUrl(url))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ZLTabWidget()
    demo.show()
    sys.exit(app.exec_())
