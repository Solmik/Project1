# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glavU1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MW(object):
    def setupUi(self, MW):
        MW.setObjectName("MW")
        MW.resize(1280, 768)
        MW.setMinimumSize(QtCore.QSize(1280, 768))
        MW.setMaximumSize(QtCore.QSize(1280, 768))
        self.centralwidget = QtWidgets.QWidget(MW)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 1241, 521))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.pBExit = QtWidgets.QPushButton(self.centralwidget)
        self.pBExit.setGeometry(QtCore.QRect(1170, 700, 88, 34))
        self.pBExit.setObjectName("pBExit")
        self.lE1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lE1.setGeometry(QtCore.QRect(810, 580, 91, 32))
        self.lE1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE1.setObjectName("lE1")
        self.pBN = QtWidgets.QPushButton(self.centralwidget)
        self.pBN.setGeometry(QtCore.QRect(450, 660, 88, 34))
        self.pBN.setObjectName("pBN")
        self.pBImD = QtWidgets.QPushButton(self.centralwidget)
        self.pBImD.setGeometry(QtCore.QRect(30, 670, 61, 31))
        self.pBImD.setObjectName("pBImD")
        self.lE2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lE2.setGeometry(QtCore.QRect(810, 620, 91, 32))
        self.lE2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lE2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE2.setObjectName("lE2")
        self.lE3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lE3.setGeometry(QtCore.QRect(450, 620, 91, 32))
        self.lE3.setAccessibleDescription("")
        self.lE3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lE3.setInputMask("")
        self.lE3.setText("")
        self.lE3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE3.setObjectName("lE3")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(780, 590, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l1.sizePolicy().hasHeightForWidth())
        self.l1.setSizePolicy(sizePolicy)
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(780, 630, 21, 18))
        self.l2.setObjectName("l2")
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(150, 10, 1091, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l5.setFont(font)
        self.l5.setText("")
        self.l5.setAlignment(QtCore.Qt.AlignCenter)
        self.l5.setObjectName("l5")
        self.textBr1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBr1.setGeometry(QtCore.QRect(220, 570, 341, 141))
        self.textBr1.setObjectName("textBr1")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 580, 71, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.zBfile = QtWidgets.QPushButton(self.centralwidget)
        self.zBfile.setGeometry(QtCore.QRect(1160, 630, 91, 34))
        self.zBfile.setObjectName("zBfile")
        self.pBImB = QtWidgets.QPushButton(self.centralwidget)
        self.pBImB.setGeometry(QtCore.QRect(110, 670, 51, 31))
        self.pBImB.setObjectName("pBImB")
        self.textBr1_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBr1_2.setGeometry(QtCore.QRect(580, 570, 341, 141))
        self.textBr1_2.setObjectName("textBr1_2")
        self.textBr1_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBr1_3.setGeometry(QtCore.QRect(20, 570, 181, 141))
        self.textBr1_3.setObjectName("textBr1_3")
        self.pBA = QtWidgets.QPushButton(self.centralwidget)
        self.pBA.setGeometry(QtCore.QRect(810, 660, 88, 34))
        self.pBA.setObjectName("pBA")
        self.textBr1_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBr1_4.setGeometry(QtCore.QRect(940, 570, 321, 111))
        self.textBr1_4.setObjectName("textBr1_4")
        self.lE3_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lE3_2.setGeometry(QtCore.QRect(1110, 590, 141, 32))
        self.lE3_2.setText("")
        self.lE3_2.setPlaceholderText("")
        self.lE3_2.setObjectName("lE3_2")
        self.textBr1_4.raise_()
        self.textBr1_3.raise_()
        self.tableWidget.raise_()
        self.pBExit.raise_()
        self.l5.raise_()
        self.textBr1.raise_()
        self.comboBox.raise_()
        self.zBfile.raise_()
        self.pBImB.raise_()
        self.textBr1_2.raise_()
        self.pBImD.raise_()
        self.lE3.raise_()
        self.pBN.raise_()
        self.lE1.raise_()
        self.l1.raise_()
        self.lE2.raise_()
        self.l2.raise_()
        self.pBA.raise_()
        self.lE3_2.raise_()
        MW.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MW.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MW)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MW)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MW)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MW)
        self.action_4.setObjectName("action_4")
        self.action_7 = QtWidgets.QAction(MW)
        self.action_7.setObjectName("action_7")
        self.action_5 = QtWidgets.QAction(MW)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MW)
        self.action_6.setObjectName("action_6")
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_7)
        self.menu_2.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MW)
        self.action_7.triggered.connect(MW.close)
        self.action_4.triggered.connect(MW.snowElt)
        self.pBExit.clicked.connect(MW.close)
        self.pBN.clicked.connect(MW.srscN)
        self.pBImD.clicked.connect(MW.srscImD)
        self.pBImB.clicked.connect(MW.srscImB)
        self.zBfile.clicked.connect(MW.sZfile)
        self.pBA.clicked.connect(MW.spBA)
        self.action_5.triggered.connect(MW.sSpis)
        QtCore.QMetaObject.connectSlotsByName(MW)
        MW.setTabOrder(self.lE1, self.lE2)
        MW.setTabOrder(self.lE2, self.lE3)
        MW.setTabOrder(self.lE3, self.pBN)
        MW.setTabOrder(self.pBN, self.pBImD)
        MW.setTabOrder(self.pBImD, self.pBExit)
        MW.setTabOrder(self.pBExit, self.tableWidget)
        MW.setTabOrder(self.tableWidget, self.textBr1)

    def retranslateUi(self, MW):
        _translate = QtCore.QCoreApplication.translate
        MW.setWindowTitle(_translate("MW", "Учет элементов"))
        self.pBExit.setText(_translate("MW", "Закрыть"))
        self.lE1.setText(_translate("MW", "0"))
        self.pBN.setText(_translate("MW", "Расчитать"))
        self.pBImD.setText(_translate("MW", "ДВЕ"))
        self.lE2.setText(_translate("MW", "0"))
        self.lE3.setPlaceholderText(_translate("MW", "Количество"))
        self.l1.setText(_translate("MW", "ДВЕ"))
        self.l2.setText(_translate("MW", "БС"))
        self.textBr1.setHtml(_translate("MW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Задайте тип и количество</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">приборов, программа расчитает</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">количество приборов другого</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> типа которые можно</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> изготовить  из оставшихся</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> элементов</p></body></html>"))
        self.comboBox.setItemText(0, _translate("MW", "  ДВЕ"))
        self.comboBox.setItemText(1, _translate("MW", "  БС"))
        self.zBfile.setText(_translate("MW", "записать"))
        self.pBImB.setText(_translate("MW", " БС"))
        self.textBr1_2.setHtml(_translate("MW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Расчитать количество</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> элементов необходимое</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> для изготовления</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">заданного количества </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">приборов.</p></body></html>"))
        self.textBr1_3.setHtml(_translate("MW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Расчитать сколько</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> возможно  изготовить.</p></body></html>"))
        self.pBA.setText(_translate("MW", "Расчитать"))
        self.textBr1_4.setHtml(_translate("MW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Записать выведенную</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">таблицу в EXEL файл</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">с предложенным именем</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(можно изменить).</p></body></html>"))
        self.menu.setTitle(_translate("MW", "Добавить"))
        self.menu_2.setTitle(_translate("MW", "Списать"))
        self.action.setText(_translate("MW", "Изменить количество элементов"))
        self.action_2.setText(_translate("MW", "Редактировать БД"))
        self.action_3.setText(_translate("MW", "Списать устройства"))
        self.action_4.setText(_translate("MW", "Создать новый злемент"))
        self.action_7.setText(_translate("MW", "Закрыть программу"))
        self.action_5.setText(_translate("MW", "Списать приборы"))
        self.action_6.setText(_translate("MW", "Списать БС"))
