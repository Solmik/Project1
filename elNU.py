# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elNU.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WElement(object):
    def setupUi(self, WElement):
        WElement.setObjectName("WElement")
        WElement.resize(800, 640)
        WElement.setMinimumSize(QtCore.QSize(800, 640))
        WElement.setMaximumSize(QtCore.QSize(800, 640))
        WElement.setSizeIncrement(QtCore.QSize(0, 0))
        WElement.setBaseSize(QtCore.QSize(10, 10))
        WElement.setStyleSheet("")
        WElement.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(WElement)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 631, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 141, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 250, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leNomer = QtWidgets.QLineEdit(self.centralwidget)
        self.leNomer.setGeometry(QtCore.QRect(240, 60, 291, 32))
        self.leNomer.setObjectName("leNomer")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 431, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.leKolvo = QtWidgets.QLineEdit(self.centralwidget)
        self.leKolvo.setGeometry(QtCore.QRect(240, 240, 131, 32))
        self.leKolvo.setObjectName("leKolvo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 360, 58, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 360, 41, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-color: rgb(0, 0, 0)")
        self.label_5.setObjectName("label_5")
        self.leDVE = QtWidgets.QLineEdit(self.centralwidget)
        self.leDVE.setGeometry(QtCore.QRect(70, 390, 113, 32))
        self.leDVE.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leDVE.setObjectName("leDVE")
        self.leBC = QtWidgets.QLineEdit(self.centralwidget)
        self.leBC.setGeometry(QtCore.QRect(270, 390, 113, 32))
        self.leBC.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leBC.setObjectName("leBC")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 290, 450, 5))
        self.line_2.setStyleSheet("color:rgb(10, 14, 255);\n"
"background-color:rgb(174, 220, 255)\n"
"")
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(160, 510, 450, 5))
        self.line_3.setStyleSheet("color:rgb(10, 14, 255);\n"
"background-color:rgb(174, 220, 255)\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pbZapis = QtWidgets.QPushButton(self.centralwidget)
        self.pbZapis.setGeometry(QtCore.QRect(270, 530, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pbZapis.setFont(font)
        self.pbZapis.setObjectName("pbZapis")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(70, 590, 700, 5))
        self.line_4.setStyleSheet("color:rgb(10, 14, 255);\n"
"background-color:rgb(174, 220, 255)\n"
"")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pbExit = QtWidgets.QPushButton(self.centralwidget)
        self.pbExit.setGeometry(QtCore.QRect(680, 600, 88, 34))
        self.pbExit.setObjectName("pbExit")
        self.leNominal = QtWidgets.QLineEdit(self.centralwidget)
        self.leNominal.setGeometry(QtCore.QRect(240, 180, 291, 32))
        self.leNominal.setText("")
        self.leNominal.setObjectName("leNominal")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 180, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.leName = QtWidgets.QLineEdit(self.centralwidget)
        self.leName.setGeometry(QtCore.QRect(240, 120, 291, 32))
        self.leName.setText("")
        self.leName.setObjectName("leName")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 320, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lePr = QtWidgets.QLineEdit(self.centralwidget)
        self.lePr.setGeometry(QtCore.QRect(510, 390, 231, 32))
        self.lePr.setObjectName("lePr")
        WElement.setCentralWidget(self.centralwidget)

        self.retranslateUi(WElement)
        self.pbExit.clicked.connect(WElement.close)
        self.pbZapis.clicked.connect(WElement.sZapis)
        QtCore.QMetaObject.connectSlotsByName(WElement)
        WElement.setTabOrder(self.leNomer, self.leName)
        WElement.setTabOrder(self.leName, self.leNominal)
        WElement.setTabOrder(self.leNominal, self.leKolvo)
        WElement.setTabOrder(self.leKolvo, self.leDVE)
        WElement.setTabOrder(self.leDVE, self.leBC)
        WElement.setTabOrder(self.leBC, self.lePr)
        WElement.setTabOrder(self.lePr, self.pbZapis)
        WElement.setTabOrder(self.pbZapis, self.pbExit)

    def retranslateUi(self, WElement):
        _translate = QtCore.QCoreApplication.translate
        WElement.setWindowTitle(_translate("WElement", "Заполнение таблицы Элемент"))
        self.label_2.setText(_translate("WElement", "Номер элемента"))
        self.label_3.setText(_translate("WElement", "Количество"))
        self.label_4.setText(_translate("WElement", "Количество элеменов применяемых в приборах"))
        self.label_6.setText(_translate("WElement", "БС"))
        self.label_5.setText(_translate("WElement", "ДВЕ"))
        self.leDVE.setText(_translate("WElement", "0"))
        self.leBC.setText(_translate("WElement", "0"))
        self.pbZapis.setText(_translate("WElement", "Записать в базу данных"))
        self.pbExit.setText(_translate("WElement", "Закрыть"))
        self.label_9.setText(_translate("WElement", "Номинал элемента"))
        self.label_10.setText(_translate("WElement", "Наименование элемента"))
        self.label_7.setText(_translate("WElement", "Примечания"))
