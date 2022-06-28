import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('pushbutton', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('Button Hint.<b>Hello<b/>')
        btn.move(20, 30)

        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('First Practice')

        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())

# 버튼 생성 / 창 크기 변경