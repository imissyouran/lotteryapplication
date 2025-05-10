from PyQt6.QtWidgets import *
from LotteryApplication_ui import *
from LeaderboardApplication_ui import *
import csv
import random

class LotteryLogic(QMainWindow, Ui_LotteryApplication):
    def __init__(self) -> None:
        '''
        Method to setup the UI and button inputs
        '''
        super().__init__()
        self.setupUi(self)

        self.submitButton.clicked.connect(lambda : self.submit())
        self.leaderboardButton.clicked.connect(lambda : self.leaderboard())

    def submit(self) -> None:
        '''
        Method runs when submit button is pressed
        Checks for user info, whether a new user is being registered, and any potential duplicates or errors
        '''
        user = self.usernameInput.text()
        user = user.strip()
        password = self.passwordInput.text()
        password = password.strip()
        number = self.numberInput.text()
        number = number.strip()
        counter = 0

        if self.newUserBox.isChecked():
            # New User Register
            try:
                with open('users.csv', 'r', newline='') as users_file:
                    reader = csv.reader(users_file)
                    for line in reader:
                        if line[0].strip() == user:
                            # If an already registered user tries to register, give error
                            self.infoLabel.setText('User Already Registered')
                            self.infoLabel.setStyleSheet('color: red;')
                            counter = 1
                    if counter == 0:
                        with open('users.csv', 'a', newline='') as users_file:
                            content = csv.writer(users_file)
                            if len(number) <= 3 and number.isnumeric():
                                winningNum = random.randint(1, 999)
                                if number == winningNum:
                                    # User win text, appends their name/password/wins to users.csv
                                    self.infoLabel.setText(f'Congrats {user}, your number wins!')
                                    content.writerow([user, password, 1])
                                else:
                                    # User lose text, appends their name/password/wins to users.csv
                                    self.infoLabel.setText(f'The winner is: {winningNum}, Better luck next time!')
                                    content.writerow([user, password, 0])
                            else:
                                self.infoLabel.setText('Please enter a number from 1-999')
                                self.infoLabel.setStyleSheet('color: red;')
            except FileNotFoundError:
                with open('users.csv', 'a', newline='') as users_file:
                        content = csv.writer(users_file)
                        content.writerow(['Username', 'Password', 'Wins'])
                        if len(number) <= 3 and number.isnumeric():
                            winningNum = random.randint(1, 999)
                            if number == winningNum:
                                    # User win text, appends their name/password/wins to users.csv
                                    self.infoLabel.setText(f'Congrats {user}, your number wins!')
                                    content.writerow([user, password, 1])
                            else:
                                    # User lose text, appends their name/password/wins to users.csv
                                    self.infoLabel.setText(f'The winner is: {winningNum}, Better luck next time!')
                                    content.writerow([user, password, 0])
                        else:
                            self.infoLabel.setText('Please enter a number from 1-999')
                            self.infoLabel.setStyleSheet('color: red;')
                            content.writerow([user, password, 0])
        else:
            uFile = open('users.csv', 'r')
            # Registered User Login
            reader = csv.reader(uFile)
            for line in reader:
                if line[0].strip() == user and line[1].strip() == password:
                    if len(number) <= 3 and number.isnumeric():
                        winningNum = random.randint(1, 999)
                        winningNum = str(winningNum)
                        if number == winningNum:
                            # Used geeksforgeeks to help me with the code in this block here.
                            uFile.close
                            self.infoLabel.setText(f'Congrats {user}, your number wins!')
                            self.infoLabel.setStyleSheet('color: black;')
                            uFile = open('users.csv', 'r')
                            dt = csv.DictReader(uFile)
                            up_dt = []
                            for r in dt:
                                if r['Username'] == user:
                                    wins = int(r['Wins'])
                                    wins = wins + 1
                                    row = {'Username': r['Username'],
                                        'Password': r['Password'],
                                        'Wins': wins}
                                    up_dt.append(row)
                                else:
                                    row = {'Username': r['Username'],
                                        'Password': r['Password'],
                                        'Wins': r['Wins']}
                                    up_dt.append(row)
                            uFile.close
                            uFile = open('users.csv', 'w', newline='')
                            headers = ['Username', 'Password', 'Wins']
                            data = csv.DictWriter(uFile, delimiter=',', fieldnames=headers)
                            data.writerow(dict((heads, heads) for heads in headers))
                            data.writerows(up_dt)
                            uFile.close
                        else:
                            self.infoLabel.setText(f'The winner is: {winningNum}, Better luck next time!')
                            self.infoLabel.setStyleSheet('color: black;')
                    else:
                        self.infoLabel.setText('Please enter a number from 1-999')
                        self.infoLabel.setStyleSheet('color: red;')
                else:
                    self.infoLabel.setText('Incorrect Username or Password')
                    self.infoLabel.setStyleSheet('color: red;')
        # Clear all of the user inputs after pressing submit
        self.usernameInput.clear()
        self.passwordInput.clear()
        self.numberInput.clear()
        self.newUserBox.setChecked(False)

    def leaderboard(self) -> None:
        '''
        Method to bring up and show the leaderboard window
        '''
        if self.lbWindow is None:
            # If leaderboard != open, open it.
            self.lbWindow = Leaderboard()
            self.lbWindow.show()
        else:
            # Closes leaderboard window
            self.lbWindow = None

class Leaderboard(QWidget, Ui_Leaderboard):
    def __init__(self) -> None:
        '''
        Method to setup the leaderboard UI
        '''
        super().__init__()
        self.setupUi(self)

        self.leaderboardWinners()

    def leaderboardWinners(self) -> None:
        '''
        Method to display the top 3 winners on the leaderboard

        !!!DOES NOT UPDATE BY ITSELF ONLY WHEN NEW INSTANCE MADE!!!
        '''
        with open('users.csv', 'r') as users_file:
            # Open file in read mode, and find top 3 winners to display on leaderboard
            reader = csv.reader(users_file)
            lbUsers = []
            wins = []
            for line in reader:
                # TODO: Add logic for sorting top 3 winners
                pass