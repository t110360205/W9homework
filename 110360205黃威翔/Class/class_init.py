# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 897)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 961, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 491, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 170, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 240, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 310, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 190, 261, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 260, 261, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(200, 330, 261, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 190, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 330, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 520, 231, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(630, 80, 251, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 39))
        self.menubar.setObjectName("menubar")
        self.menuStudent = QtWidgets.QMenu(parent=self.menubar)
        self.menuStudent.setObjectName("menuStudent")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuStudent.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Student Management Sysrem"))
        self.label_2.setText(_translate("MainWindow", "    Add Student"))
        self.label_3.setText(_translate("MainWindow", "    Name:"))
        self.label_4.setText(_translate("MainWindow", "    Subject:"))
        self.label_5.setText(_translate("MainWindow", "    Score:"))
        self.pushButton.setText(_translate("MainWindow", "Query"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.pushButton_3.setText(_translate("MainWindow", "Send"))
        self.label_6.setText(_translate("MainWindow", "will show information"))
        self.menuStudent.setTitle(_translate("MainWindow", "Student"))
        self.label_6.setWordWrap(True)
        self.textEdit_2.setEnabled(False)
        self.textEdit_3.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())'''
