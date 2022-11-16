# -*- coding: utf-8 -*-
# Создание нового элемента в БД
from PyQt5 import QtWidgets, QtCore
import sqlite3
from PyQt5.QtCore import QTimer
import elNU

class El_Window(QtWidgets.QMainWindow, elNU.Ui_WElement):
    sig_zap = QtCore.pyqtSignal(int)

    def __init__(self):  # для доступа к элементам таблицы в файле zap1

        super().__init__()
        self.setupUi(self)  # для инициализации дизайна

        self.t = QTimer(self)
        self.t.timeout.connect(self.t_out)

        self.sig_zap.connect(self.zapBD)

# Обработка сигнала о записи данных, запись в таблицу element
    def zapBD(self, a):
        try:
           # self.labMesto.setText(self.mesto)
            conn = sqlite3.connect('elements.db')
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS element(nomer INTEGER PRIMARY KEY AUTOINCREMENT , 
            invnomer TXT, name TXT, nominal TXT, kolwo INT, dve INT, bs INT, primech TXT);""")
            conn.commit()
            self.u = (self.nomer, self.name, self.nominal, self.kolwo, self.dve, self.bs, self.primech)
            cur.execute("INSERT INTO element( invnomer, name, nominal, kolwo, dve, bs, primech) VALUES(?, ?, ?, ?, ?, ?, ?);", self.u)
            conn.commit()
            cur.close()
        except:
            self.label.setText('<font color= "red">Ошибка записи в базу данных!</font>')
        else:
            self.label.setText('<font color= "green">Запись в базу данных прошла успешно!</font>')

# Ввод и проверка набора данных
    def sZapis(self):
        self.nomer = self.leNomer.text()
        self.name = self.leName.text()
        self.nominal = self.leNominal.text()
        self.kolwo = self.leKolvo.text()
        self.dve = self.leDVE.text()
        self.bs = self.leBC.text()
        self.primech = self.lePr.text()

        if(self.nomer and self.name and self.kolwo and self.dve and self.bs):
            if(self.nomer.isdigit() and self.kolwo.isdigit()):
                a = 11
                s3 = '0'
                self.sig_zap.emit(a)
                self.leNomer.clear()
                self.leName.clear()
                self.leNominal.clear()
                self.leKolvo.clear()
                self.leDVE.setText(str(s3))
                self.leBC.setText(str(s3))
                self.lePr.clear()

                self.t.start(2000)
            else:
                self.label.setText('<font color= "red">Ошибка набора данных!</font>')
        else:
            self.label.setText('<font color= "red">Ошибка набора данных!</font>')

    def t_out(self):
        self.label.setText("")
        self.t.stop()
