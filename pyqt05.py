import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()
        '''

        '''
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)    # 메인 창의 레이아웃을 세로로 만들기

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()
        '''

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]    # (0, 0) (0, 1) (0, 2) ... (4, 2) (4, 3)

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)   # *position (0, 3)을 각각 0, 3으로 변경하여 전달, addWidget에는 3개의 변수가 들어감

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Exam()
    sys.exit(app.exec_())

# 레이아웃
# QHBoxLayout 가로로 배열
# QVBoxLayout 세로로 배열
# Stretch 빈 공간을 채워줌