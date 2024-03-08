import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QStackedWidget


class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)

        layout = QVBoxLayout()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        print("Handling login...")  # 添加调试输出
        # 这里可以添加验证逻辑
        # 比如检查用户名和密码是否匹配
        # 如果验证通过，则切换到主页面
        # main_widget.setCurrentIndex(1)  # 切换到主页面
        stacked_widget.setCurrentWidget(main_widget)  # 切换到主页面


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        layout = QVBoxLayout()
        self.label = QLabel("Welcome to Main Page")
        layout.addWidget(self.label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    login_widget = LoginWidget()
    main_widget = MainWindow()

    stacked_widget.addWidget(login_widget)
    stacked_widget.addWidget(main_widget)

    stacked_widget.setWindowTitle("Login Example")
    stacked_widget.show()

    sys.exit(app.exec_())
