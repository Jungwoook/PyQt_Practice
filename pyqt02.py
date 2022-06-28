import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Push Me!', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.resize(500, 500)
        self.setWindowTitle('Second Practice')
        self.show()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())

# 버튼 이벤트 처리 / 메시지 박스 / 종료 이벤트