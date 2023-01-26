from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QApplication,
)
import sys
from DataBaseOperation import DBOperation
from HomeWindow import HomeScreen


class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Login")
        self.resize(300, 100)
        layout = QVBoxLayout()  #! Vertical layout

        label_username = QLabel("Username : ")
        label_username.setStyleSheet("color:#fff;padding:8px 0px;font-size:18px;")
        self.input_username = QLineEdit()
        self.input_username.setStyleSheet("padding:5px;font-size:17px")
        label_password = QLabel("Password : ")
        label_password.setStyleSheet("color:#fff;padding:8px 0px;font-size:18px;")
        self.error_msg = QLabel()
        self.error_msg.setStyleSheet(
            "color:red;padding:8px 0px;font-size:18px;text-align:center"
        )
        self.input_password = QLineEdit()
        self.input_password.setStyleSheet("padding:5px;font-size:17px")

        btn_login = QPushButton("Login")
        btn_login.setStyleSheet(
            "padding:5px;font-size:20px;background:green;color:#fff"
        )
        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_login)
        layout.addWidget(self.error_msg)
        layout.addStretch()
        btn_login.clicked.connect(self.showHome)
        self.setLayout(layout)

    def showLoginScreen(self):
        #! shows the login screen
        self.show()

    def showHome(self):
        #! checks if the input fields are empty, if empty then shows error
        if self.input_username.text() == "":
            self.error_msg.setText("Please Enter Username")
            return

        if self.input_password.text() == "":
            self.error_msg.setText("Please Enter Password")
            return

        dboperation = DBOperation()

        #! Checks if admin username and password are correct; if correct then instantly logs in the user otherwise shows the error message
        result = dboperation.doAdminLogin(
            self.input_username.text(), self.input_password.text()
        )
        if result:
            self.error_msg.setText("Login Successful")
            self.close()
            self.home = HomeScreen()
            self.home.show()
        else:
            self.error_msg.setText("Invalid Login Details")
