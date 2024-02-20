import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QTabWidget

class BrowserTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi Tab Browser")

        self.addTab(QWebEngineView(), "Tab 1")  # Add a tab with a QWebEngineView
        self.addTab(QWebEngineView(), "Tab 2")  # Add another tab with a QWebEngineView

        # Load different URLs in each tab
        self.widget(0).setUrl(QUrl("https://sx.cailian.net/"))
        self.widget(1).setUrl(QUrl("https://sx.cailian.net/"))

        self.currentChanged.connect(self.tab_changed)

    def tab_changed(self, index):
        print(index)
        # Load different URLs when the tab is changed
        if index == 0:
            self.widget(0).setUrl(QUrl("https://sx.cailian.net/#/Home"))
        elif index == 1:
            self.widget(1).setUrl(QUrl("https://sx.cailian.net/#/TheoryCourse/TeachingClass"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = BrowserTabWidget()
    browser.show()
    sys.exit(app.exec_())
