import sys

from PyQt5.QtWidgets import *
from GUI.home import  *
class Main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        # Instaciamos nuestra ventanas widget home
        self.home = Ui_home()
        self.home.setupUi(self)
        # Eventos
        self.home.bt_lexico.clicked.connect(self.ev_lexico)
        self.home.bt_sintactico.clicked.connect(self.ev_sintactico)

        self.home.bt_archivo.clicked.connect(self.ev_archivo)
        self.home.bt_limpiar.clicked.connect(self.ev_limpiar)

        #Desarrollandores
        #Desarrollando por Maryon Torres y Michael Abril

    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas
        :return:
        '''
        pass


    def ev_sintactico(self):
        '''
        Manejo de analisis gramatico
        :return:
        '''
        # print("sintactico")
        pass

    def ev_archivo(self):
        '''
        Manejo de subir archivo
        :return:
        '''
        dlg = QFileDialog()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read().strip()
                if data:
                    self.home.tx_ingreso.setText(data+"\n")

    def ev_limpiar(self):
        '''
        Manejo de limpieza de campos
        :return:
        '''
        self.home.tx_ingreso.setText('')
        self.home.tx_lexico.setText('')
        self.home.tx_sintactico.setText('')




def iniciar():
    # Instaciamos nuestro app por defecto esto no cambia
    app = QApplication(sys.argv)

    # Instaciomos nuestro ventana
    ventana = Main()
    #Se establece un tamaño
    ventana.setFixedSize(800,600)
    # Mostramos nuestra app
    ventana.show()

    #Controlamos el cierre de la app
    sys.exit(app.exec_())


if __name__ == '__main__':
    iniciar()
