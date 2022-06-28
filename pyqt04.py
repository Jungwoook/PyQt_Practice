import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage('Hello')

        menu = self.menuBar()               # 메뉴바 생성
        menu_file = menu.addMenu('File')    # 그룹 생성
        menu_edit = menu.addMenu('Edit')    # 그룹 생성
        menu_view = menu.addMenu('View')    # 그룹 생성

        file_exit = QAction('Exit', self)   # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('Exit')

        new_txt = QAction('New Text File', self)   # 메뉴 객체 생성
        new_txt.setShortcut('Ctrl+T')
        new_txt.setStatusTip('New Text File')

        new_py = QAction('New Python File', self)   # 메뉴 객체 생성
        new_py.setShortcut('Ctrl+P')
        new_py.setStatusTip('New Python File')

        view_stat = QAction('Status Bar', self, checkable=True)
        view_stat.setChecked(True)

        file_exit.triggered.connect(QCoreApplication.instance().quit)
        view_stat.triggered.connect(self.tglStat)

        file_new = QMenu('New', self)   # 메뉴 객체 생성

        file_new.addAction(new_txt)
        file_new.addAction(new_py)

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)      # 메뉴 등록

        menu_view.addAction(view_stat)

        self.resize(450,400)
        self.show()

    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, QContentMenuEvent):
        cm = QMenu(self)

        quit = cm.addAction('Quit')

        action = cm.exec_(self.mapToGlobal(QContentMenuEvent.pos()))
        if action == quit:
            qApp.quit()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())

# 체크메뉴, 컨텍스트메뉴