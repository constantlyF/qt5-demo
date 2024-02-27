import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QTabWidget, QMainWindow, QApplication


class ZLConfig:
    configs = {
        "工作台": "https://sx.cailian.net/#/",
        "项目": "https://sx.cailian.net/#/TheoryCourse/TeachingClass",
        "大数据库": "https://sx.cailian.net/#/teachingDetail/courseDetail?courseId=2035&classId=257685&subjectId=625&classStatus=1&courseName=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91&className=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91&courseType=3&type=1&isPay=1&courseModel=2&teacherUserId=537758",
        "数据应用": "https://bd.cailian.net/#/dataApplication",
        "人工智能": None,
        "权限管理": "https://bd.cailian.net/#/orgManage",
    }
    # configs = {
    #     "工作台": "https://bd.cailian.net/#/login",
    #     "项目": "https://bd.cailian.net/#/projectManage",
    #     "大数据库": "https://bd.cailian.net/#/IndustryDatabase",
    #     "数据应用": "https://bd.cailian.net/#/dataApplication",
    #     "人工智能": None,
    #     "权限管理": "https://bd.cailian.net/#/orgManage",
    # }
    configs_index: list = list(configs.keys())

    @staticmethod
    def get_index(key):
        return ZLConfig.configs_index.index(key)


class ZLTabWidget(QTabWidget):
    def __init__(self, orangeMainWin):
        super(ZLTabWidget, self).__init__()
        for title, url in ZLConfig.configs.items():
            index = ZLConfig.get_index(title)
            if title == '人工智能':
                self.addTab(orangeMainWin, f'tab_{index}')
            else:
                self.addTab(ZLWebMainWindow(title, url), f'tab_{index}')
            self.setTabText(index, title)
        self.setWindowTitle("中联")





class ZLWebMainWindow(QMainWindow):

    def __init__(self, title, url):
        super(QMainWindow, self).__init__()
        self.setWindowTitle(title)
        self.setGeometry(5, 30, 1355, 730)
        browser.load(QUrl(url))
        self.setCentralWidget(browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = QWebEngineView()
    demo = ZLTabWidget(ZLWebMainWindow('人工智能', 'https://yiyan.baidu.com/'))
    demo.show()
    sys.exit(app.exec_())
