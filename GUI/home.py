import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home(object):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de Signals

        #Área de Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_home()
    window.show()
    sys.exit(app.exec_())