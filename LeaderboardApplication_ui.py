# Form implementation generated from reading ui file 'c:\Users\djmin\Downloads\VisStudio\finalproject2\LeaderboardApplication.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Leaderboard(object):
    def setupUi(self, Leaderboard):
        Leaderboard.setObjectName("Leaderboard")
        Leaderboard.resize(205, 115)
        Leaderboard.setMinimumSize(QtCore.QSize(205, 115))
        Leaderboard.setMaximumSize(QtCore.QSize(205, 115))
        self.secondPlaceWinner = QtWidgets.QLabel(parent=Leaderboard)
        self.secondPlaceWinner.setGeometry(QtCore.QRect(40, 60, 161, 16))
        self.secondPlaceWinner.setObjectName("secondPlaceWinner")
        self.firstPlaceLabel = QtWidgets.QLabel(parent=Leaderboard)
        self.firstPlaceLabel.setGeometry(QtCore.QRect(20, 40, 21, 16))
        self.firstPlaceLabel.setObjectName("firstPlaceLabel")
        self.secondPlaceLabel = QtWidgets.QLabel(parent=Leaderboard)
        self.secondPlaceLabel.setGeometry(QtCore.QRect(20, 60, 21, 16))
        self.secondPlaceLabel.setObjectName("secondPlaceLabel")
        self.firstPlaceWinner = QtWidgets.QLabel(parent=Leaderboard)
        self.firstPlaceWinner.setGeometry(QtCore.QRect(40, 40, 161, 16))
        self.firstPlaceWinner.setObjectName("firstPlaceWinner")
        self.thirdPlaceLabel = QtWidgets.QLabel(parent=Leaderboard)
        self.thirdPlaceLabel.setGeometry(QtCore.QRect(20, 80, 21, 16))
        self.thirdPlaceLabel.setObjectName("thirdPlaceLabel")
        self.thirdPlaceWinner = QtWidgets.QLabel(parent=Leaderboard)
        self.thirdPlaceWinner.setGeometry(QtCore.QRect(40, 80, 161, 16))
        self.thirdPlaceWinner.setObjectName("thirdPlaceWinner")
        self.leaderboardLabel = QtWidgets.QLabel(parent=Leaderboard)
        self.leaderboardLabel.setGeometry(QtCore.QRect(50, 10, 111, 20))
        self.leaderboardLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.leaderboardLabel.setObjectName("leaderboardLabel")

        self.retranslateUi(Leaderboard)
        QtCore.QMetaObject.connectSlotsByName(Leaderboard)

    def retranslateUi(self, Leaderboard):
        _translate = QtCore.QCoreApplication.translate
        Leaderboard.setWindowTitle(_translate("Leaderboard", "Leaderboard"))
        self.secondPlaceWinner.setText(_translate("Leaderboard", "Second Place"))
        self.firstPlaceLabel.setText(_translate("Leaderboard", "1."))
        self.secondPlaceLabel.setText(_translate("Leaderboard", "2."))
        self.firstPlaceWinner.setText(_translate("Leaderboard", "First Place"))
        self.thirdPlaceLabel.setText(_translate("Leaderboard", "3."))
        self.thirdPlaceWinner.setText(_translate("Leaderboard", "Third Place"))
        self.leaderboardLabel.setText(_translate("Leaderboard", "LEADERBOARD"))
