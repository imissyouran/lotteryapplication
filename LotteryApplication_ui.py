# Form implementation generated from reading ui file 'c:\Users\djmin\Downloads\VisStudio\finalproject2\LotteryApplication.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LotteryApplication(object):
    def setupUi(self, LotteryApplication):
        LotteryApplication.setObjectName("LotteryApplication")
        LotteryApplication.resize(240, 225)
        LotteryApplication.setMinimumSize(QtCore.QSize(240, 225))
        LotteryApplication.setMaximumSize(QtCore.QSize(240, 225))
        self.centralwidget = QtWidgets.QWidget(parent=LotteryApplication)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 10, 61, 16))
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 40, 51, 20))
        self.passwordLabel.setObjectName("passwordLabel")
        self.usernameInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(80, 10, 131, 20))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(80, 40, 131, 20))
        self.passwordInput.setObjectName("passwordInput")
        self.numberlabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.numberlabel.setGeometry(QtCore.QRect(20, 70, 47, 16))
        self.numberlabel.setObjectName("numberlabel")
        self.numberInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.numberInput.setGeometry(QtCore.QRect(80, 70, 51, 20))
        self.numberInput.setObjectName("numberInput")
        self.newUserBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.newUserBox.setGeometry(QtCore.QRect(140, 70, 81, 21))
        self.newUserBox.setObjectName("newUserBox")
        self.submitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(60, 100, 121, 23))
        self.submitButton.setObjectName("submitButton")
        self.infoLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(16, 130, 211, 20))
        self.infoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.leaderboardButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.leaderboardButton.setGeometry(QtCore.QRect(80, 160, 75, 23))
        self.leaderboardButton.setObjectName("leaderboardButton")
        LotteryApplication.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LotteryApplication)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setObjectName("menubar")
        LotteryApplication.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LotteryApplication)
        self.statusbar.setObjectName("statusbar")
        LotteryApplication.setStatusBar(self.statusbar)

        self.retranslateUi(LotteryApplication)
        QtCore.QMetaObject.connectSlotsByName(LotteryApplication)

    def retranslateUi(self, LotteryApplication):
        _translate = QtCore.QCoreApplication.translate
        LotteryApplication.setWindowTitle(_translate("LotteryApplication", "Lottery Application"))
        self.usernameLabel.setText(_translate("LotteryApplication", "Username"))
        self.passwordLabel.setText(_translate("LotteryApplication", "Password"))
        self.numberlabel.setText(_translate("LotteryApplication", "Number"))
        self.newUserBox.setText(_translate("LotteryApplication", "New User?"))
        self.submitButton.setText(_translate("LotteryApplication", "SUBMIT NUMBER"))
        self.infoLabel.setText(_translate("LotteryApplication", "Input User Info and Number"))
        self.leaderboardButton.setText(_translate("LotteryApplication", "Leaderboard"))
