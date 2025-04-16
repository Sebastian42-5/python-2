from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import time
import webbrowser


class MyWindow(QMainWindow):

    def __init__(self):
        
        super(MyWindow, self).__init__()

        self.setGeometry(200, 200, 300, 300)

        self.setWindowTitle('Tab opener!')

        self.initUI()


    def initUI(self):

        self.label = QtWidgets.QLabel(self)

        self.label.setText('Click here to open tabs needed for homework')

        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)

        self.b1.setText('Click me')

        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('You pressed the button')
        self.set_tabs()


    def set_tabs(self):

        url_lst = ['https://www.youtube.com/watch?v=d9zSKHrE7aQ&ab_channel=asmrzeitgeist', 'https://moodle.dawsoncollege.qc.ca/my/', 'https://dawsoncollege.omnivox.ca/Login/Account/Login?ReturnUrl=%2fintr%2f', 'https://www.youtube.com/']


        for website in url_lst:
            webbrowser.open_new_tab(website)

            time.sleep(0.5)
    


def window():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = MyWindow()
        win.show()
        sys.exit(app.exec())


window()







    
