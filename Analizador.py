from tkinter import messagebox
import sys

""" EQUIPO 4
Cadena Garcia Maria Fernanda - 2173330048
Francisco Ramirez Daniel - 2173330010
Garcia Serrano Jorge Luis - 2173330050
Rodriguez Hernandez Alejandro - 2173330037
Olguin Trejo Javier Eduardo - 2173330027
"""
class myClass:
    __palabrasReservadas= {1:"class",
                           2:"void",
                           3:"int",
                           4:"string"}

    __estructuras = {1:"if",
                     2:"else",
                     3:"while"}

    __cartEspecial = {1:"(",
                      2:")",
                      3:"{",
                      4:"}"}

    __operaciones  = {1:"*",
                      2:"/",
                      3:"+",
                      4:"-"}

    __operacion = ["*", "/", "+", "-"]
    classname = ""
    code = []
    variable = []
    contenido = []
    apuntador = 0

    def Analizar(self, cad):
        x = cad
        if "Class" in x[0]:
            i = x[0].find("class")
            i = i + 6
            while x[0][i] != "{":
                if i > 60:
                    self.error(myClass, "No se encotro llave de apertura ")
                    self.classname = ""
                    break
                else:
                    self.classname += str(x[0][i])
                i+=1
            print("Class name: " + self.classname)
            self.comp(myClass, x)

        else:
            print("Class name")
            self.error(myClass, "Class name")

    def error(self, err):
        messagebox.showinfo(message=("Error: " + err), title="Error")
        sys.exit()

    def printf(self, cad):
        cad = cad.replace("printf","")
        cad = cad.replace(";","")
        for i in range(len(self.variable)):
            if self.variable[i] in cad:
                cad = cad.replace(self.variable[i], str(self.contenido[i]))
        if "+" in cad or "-" in cad or "*" in cad or "/" in cad:
            cad = eval(cad)
        print(cad)

    def comp(self, x):
        i = 0
        while(x != "}" and i < len(x)):
            if self.classname != "":
                for i in range(len(x)):
                    if i == 0:
                        continue
                    if "=" in x[i] or "printf" and ";" in x[i]:
                        if "printf" in x[i]:
                            self.printf(myClass,x[i])
                            continue
                        else:
                            j = x[i].split("=")
                            j[0] = j[0].replace(" ", "")
                            j[1] = j[1].replace(";", "")
                            j[1] = j[1].replace(" ", "")
                            if j[0] in self.variable:
                                con = self.variable.index(j[0])
                                self.contenido[con] = j[1]
                                print("[" + self.contenido[con] + "]" + "<---" + self.variable[con] + "*")
                            else:
                                self.variable.append(j[0])
                                self.contenido.append(j[1])
                                if "*" in self.contenido[self.apuntador] or "/" in self.contenido[self.apuntador] or "+" in self.contenido[self.apuntador] or "-" in self.contenido[self.apuntador]:
                                    self.exprecion(myClass)

                                print("[" + str(self.contenido[self.apuntador]) + "]" + "<---" + self.variable[self.apuntador])
                                self.apuntador += 1

                    else:
                        if x[i] == "}":
                            sys.exit()
                        self.error(myClass, "Falta ;")
                        sys.exit()


    def exprecion(self):
        x = 0
        res = eval(str(self.contenido[self.apuntador]))
        self.contenido[self.apuntador] = res




