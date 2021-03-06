# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 600)
        MainWindow.setStyleSheet("background-color: rgb(98, 127, 245);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 321, 71))
        self.label.setStyleSheet("color: rgb(245, 237, 86);")
        self.label.setObjectName("label")
        self.tx_ingreso = QtWidgets.QTextEdit(self.centralwidget)
        self.tx_ingreso.setGeometry(QtCore.QRect(10, 140, 481, 191))
        self.tx_ingreso.setStyleSheet("background-color: rgb(128, 153, 255);\n"
"")
        self.tx_ingreso.setObjectName("tx_ingreso")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(520, 140, 251, 31))
        self.label_2.setStyleSheet("color: rgb(168, 162, 50);")
        self.label_2.setObjectName("label_2")
        self.bt_archivo = QtWidgets.QPushButton(self.centralwidget)
        self.bt_archivo.setGeometry(QtCore.QRect(530, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_archivo.setFont(font)
        self.bt_archivo.setStyleSheet("background-color: rgb(245, 180, 110);\n"
"border-radius: 7px;")
        self.bt_archivo.setObjectName("bt_archivo")
        self.bt_limpiar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_limpiar.setGeometry(QtCore.QRect(660, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_limpiar.setFont(font)
        self.bt_limpiar.setStyleSheet("background-color: rgb(198, 0, 0);\n"
"border-radius: 7px;")
        self.bt_limpiar.setObjectName("bt_limpiar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 250, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tx_lexico = QtWidgets.QTextEdit(self.centralwidget)
        self.tx_lexico.setGeometry(QtCore.QRect(20, 390, 351, 181))
        self.tx_lexico.setStyleSheet("background-color: rgb(128, 153, 255);\n"
"")
        self.tx_lexico.setObjectName("tx_lexico")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(390, 390, 20, 191))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 340, 741, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.bt_lexico = QtWidgets.QPushButton(self.centralwidget)
        self.bt_lexico.setGeometry(QtCore.QRect(580, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_lexico.setFont(font)
        self.bt_lexico.setStyleSheet("background-color: rgb(245, 180, 110);\n"
"border-radius: 7px;")
        self.bt_lexico.setObjectName("bt_lexico")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 350, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 360, 131, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 410, 391, 171))
        self.label_5.setObjectName("label_5")
        self.label.raise_()
        self.label_2.raise_()
        self.bt_archivo.raise_()
        self.bt_limpiar.raise_()
        self.line.raise_()
        self.tx_lexico.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.tx_ingreso.raise_()
        self.bt_lexico.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Compilador</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">C??digo fuente</span></p></body></html>"))
        self.bt_archivo.setText(_translate("MainWindow", "Archivo"))
        self.bt_limpiar.setText(_translate("MainWindow", "Borrar"))
        self.bt_lexico.setText(_translate("MainWindow", "Compilar"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Output</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Equipo:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cadena Garcia Maria Fernanda - 2173330048</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Francisco Ramirez Daniel - 2173330010</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Garcia Serrano Jorge Luis - 2173330050</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Rodriguez Hernandez Alejandro - 2173330037</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Olguin Trejo Javier Eduardo - 2173330027</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
