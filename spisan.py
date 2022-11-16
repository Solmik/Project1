# -*- coding: utf-8 -*-
# списание приборов
from PyQt5 import QtWidgets, QtCore
import sqlite3
from PyQt5.QtCore import QTimer
import spisanU

class MWspis(QtWidgets.QMainWindow, spisanU.Ui_MWspis):

    sig_sps = QtCore.pyqtSignal(int)

    def __init__(self):  # для доступа к элементам таблицы в файле zap1

        super().__init__()
        self.setupUi(self)  # для инициализации дизайна

        self.t = QTimer(self)
        self.t.timeout.connect(self.t_out)
        self.sig_sps.connect(self.spisan)

    def t_out(self):
        self.label.setText("")
        self.t.stop()

    def sSpis(self):
        a = 11
        sp = self.lineEdit.text()
        try:
            self.spi = int(sp)

        except:
            self.label.setText(sp+" - Введено не число")
        else:
            if self.spi > 0:
                self.label.setText(sp + " Ввод верен")

                nomer = self.comboBox.currentText()
                if nomer == 'ДВЕ':
                    a = 5

                if nomer == 'БС':
                    a = 6
                self.lineEdit.setText("")
                self.sig_sps.emit(a)
            else:
                self.label.setText(sp + " - Введено отрицательное число")

    def spisan(self, a):
        try:
            conn = sqlite3.connect('elements.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM element")
            row1 = cur.fetchall()
            cur.close()
        except:
            self.label.setText('<font color= "red">Ошибка соединения с БД!</font>')
        else:

            a = int(a)
            rez = False
            row = row1.copy()

            for i in range(len(row)):
                row[i] = list(row[i])
                row[i][4] = row[i][4] - row[i][a] * self.spi
                if row[i][4] < 0:
                    self.label.setText('<font color= "red">Ошибка ввода количества приборов!</font>')
                    rez = False
                    break
                else:
                    rez = True
            print("rez=", rez)

            if rez:
                try:
                    conn = sqlite3.connect('elements.db')
                    cur = conn.cursor()

                    for i in range(len(row)):
                        cur.execute('UPDATE element SET kolwo=? WHERE nomer=?', (row[i][4], row[i][0]))  # обновляем

                    conn.commit()
                    cur.close()
                except:
                    self.label.setText('<font color= "red">Ошибка записи в базу данных</font>')
                else:
                    self.label.setText('<font color= "green">Запись в базу данных прошла успешно</font>')
                    self.t.start(1700)





