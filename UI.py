# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Add(QDialog):
    def __init__(self):
        super(Add, self).__init__()
        self.setWindowTitle(u"新建")
        self.initLayout()
        self.resize(300, 100)
        self.show()

    def initLayout(self):
        self.leftLayout = QGridLayout(self)

        lblTitle = QLabel(u'标题')
        editTitle = QLineEdit()

        lblStart = QLabel(u'开始时间')
        editStart = QLineEdit()

        lblEnd = QLabel(u'结束时间')
        editEnd = QLineEdit()

        self.leftLayout.addWidget(lblTitle, 0, 0)
        self.leftLayout.addWidget(editTitle, 0, 1)

        self.leftLayout.addWidget(lblStart, 1, 0)
        self.leftLayout.addWidget(editStart, 1, 1)

        self.leftLayout.addWidget(lblEnd, 2, 0)
        self.leftLayout.addWidget(editEnd, 2, 1)

        '''self.mainLayout = QGridLayout(self)
        self.mainLayout.setMargin(15)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setColumnStretch(1, 20)
        self.mainLayout.addLayout(self.leftLayout, 0, 0)'''



class Talendar(QWidget):

    def __init__(self):
        super(Talendar, self).__init__()
        self.setWindowTitle("Talendar")

        self.initGrid()
        self.resize(650, 500)
        #self.center()
        #self.current_row = 0
        #self.setGeometry(300, 300, 1000, 400)
        #elf.setWindowTitle('Talendar')
        #self.setWindowIcon(QtGui.QIcon('icon.png'))

    def initDB(self):
        pass

    def initGrid(self):


        self.initLeftGrid()
        self.initCalendarGrid()
        self.initMainGrid()


    def initMainGrid(self):
        self.mainLayout = QGridLayout(self)
        self.mainLayout.setMargin(15)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setColumnStretch(1,20)
        self.mainLayout.addLayout(self.leftLayout, 0, 0)
        self.mainLayout.addLayout(self.calendarLayout, 0, 1)
        #self.mainLayout.addLayout(bottomLayout, 1, 0, 1, 2)
        #self.mainLayout.setSizeConstraint(QLayout.SetFixedSize)
    def newWindow(self):
        addWindow = Add()
        if addWindow.exec_():
            return

    def initLeftGrid(self):
        self.leftLayout = QVBoxLayout()
        #self.leftLayout.setMargin(10)

        btnUpdate = QPushButton(u'同步')
        self.leftLayout.addWidget(btnUpdate)
        btnNew = QPushButton(u'新建')
        self.leftLayout.addWidget(btnNew)

        btnNew.clicked.connect(self.newWindow)
        btnDDL = QPushButton(u'DDL列表')
        self.leftLayout.addWidget(btnDDL)
        btnSetting = QPushButton(u'设置')
        self.leftLayout.addWidget(btnSetting)

        self.leftLayout.addStretch(1)
        #self.leftLayout.setRowStretch(0, 1)
        #self.leftLayout.setRowStretch(1, 1)
        #self.leftLayout.setColumnStretch(0, 1)

    def fillBlank(self, flag, start, end):     #column 1 row 0
        for i in range(start, end):
            self.leftLayout.addWidget(QLabel(''),0, 0)

    def initCalendarGrid(self):
        self.calendarLayout = QGridLayout()
        self.grid = QTableWidget()


        #self.setCentralWidget(self.grid)

        self.grid.setColumnCount(7)
        self.grid.setRowCount(0)
        column_width = [75 for i in range(7)]
        for column in range(7):
            self.grid.setColumnWidth(column, column_width[column])
        headerlabels = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日']
        self.grid.setHorizontalHeaderLabels(headerlabels)
        self.grid.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.grid.setSelectionBehavior(QAbstractItemView.SelectRows)


        self.calendarLayout.addWidget(self.grid)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initUI(self):

        #self.c = Communicate()
        self.c.closeApp.connect(self.close)

        #self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()


    def mousePressEvent(self, event):

        self.c.closeApp.emit()


def main():

    app = QApplication(sys.argv)
    talendar = Talendar()
    talendar.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()