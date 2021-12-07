import sys
from Analizador import myClass as Lex
from tkinter import Tk
from tkinter.filedialog import askopenfilename
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

        self.home.bt_archivo.clicked.connect(self.ev_archivo)
        self.home.bt_limpiar.clicked.connect(self.ev_limpiar)

        #Desarrollandoresl

    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas
        :return:
        '''
        try:
            Lex.Analizar(Lex, self.tx_ingreso.text())
        except:
            print("compilar")


    def ev_archivo(self):
        '''
        Manejo de subir archivo
        :return:
        '''
       # try:
        Tk().withdraw()
        filename = askopenfilename()
        data = []
        with open(filename, 'r') as f:
            for line in f:
                data.append(line.rstrip())
            if data:
                self.tx_ingreso.setText(data)
                Lex.Analizar(Lex, self.tx_ingreso.Text())
            else:
                print("Archivo no apto")
        """except:
            print("Error")"""

    def ev_limpiar(self):
        '''
        Manejo de limpieza de campos
        :return:
        '''
        try:
            self.home.tx_ingreso.setText('')
            self.home.tx_lexico.setText('')
            self.home.tx_sintactico.setText('')
        except:
            print("limpiar")




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
