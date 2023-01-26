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
    #! Closes the splash screen and shows the setup window
    mainScreen.splash.close()
    configureWindow.show()


def showLoginWindow():
    #! Closes the splash screen and shows the login window
    mainScreen.splash.close()
    login.showLoginScreen()


#! Running the application
app = QApplication(sys.argv)
login = LoginScreen()
mainScreen = MainScreen()
mainScreen.showSplashScreen()
configureWindow = ConfigureWindow()


#! Checking if config.json files exists
if os.path.exists("./config.json"):
    QTimer.singleShot(3000, showLoginWindow)
else:
    QTimer.singleShot(3000, showSetupWindow)

#! If user presses close button on the window, it will terminate the program and close the window
sys.exit(app.exec_())


"""
! **RUN THIS IN TERMINAL ONLY**
-> source /Users/lakshyaraik/Documents/parking_management_system/env/bin/activate
-> pip3 install PyQt5
-> python3 MainProgram.py
"""
