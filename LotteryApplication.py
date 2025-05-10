from lotterylogic import *

def main():
    application = QApplication([])
    window = LotteryLogic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()