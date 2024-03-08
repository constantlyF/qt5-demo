import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

url = QUrl(
    "https://bduat.cailian.net/#/login?dG9rZW49YjhjN2Y3N2EtNjE4ZS00OTY2LTgyNDYtMDBmMDhhNzllYmIyJnR5cGU9a2hkJnVybD1JbmR1c3RyeURhdGFiYXNl")

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl, QVariant
from PyQt5.QtWebChannel import QWebChannel

def on_java_script_window_object_cleared():
    result = page.runJavaScript("window.sessionStorage;")
    print("Session Storage Data:", result)

app = QApplication(sys.argv)

view = QWebEngineView()
page = QWebEnginePage()

# 连接 javaScriptWindowObjectCleared 信号，以便在JavaScript对象准备就绪时执行相关操作
page.javaScriptWindowObjectCleared.connect(on_java_script_window_object_cleared)

view.setPage(page)
view.load(url)
view.show()

sys.exit(app.exec_())
