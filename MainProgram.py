import sys
import os
from ConfigureWindow import ConfigureWindow
from LoginWindow import LoginScreen
from PyQt5.QtWidgets import QApplication, QSplashScreen, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer


class MainScreen:
    #! Shows the splash screen image
    def showSplashScreen(self):
        self.pix = QPixmap("./splash.jpg")
        self.splash = QSplashScreen(self.pix, Qt.SplashScreen)
        self.splash.show()


def showSetupWindow():
    mainScreen.splash.close()
    configureWindow.show()


def showLoginWindow():
    mainScreen.splash.close()
    login.showLoginScreen()


app = QApplication(sys.argv)
login = LoginScreen()
mainScreen = MainScreen()
mainScreen.showSplashScreen()
configureWindow = ConfigureWindow()

if os.path.exists("./config.json"):
    QTimer.singleShot(3000, showLoginWindow)
else:
    QTimer.singleShot(3000, showSetupWindow)


sys.exit(app.exec_())


"""
! **RUN THIS IN TERMINAL ONLY**
-> source /Users/lakshyaraik/Documents/parking_management_system/env/bin/activate
-> pip3 install PyQt5
-> python3 MainProgram.py
"""
