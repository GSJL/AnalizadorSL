from tkinter import messagebox
import sys
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
                    self. classname = ""
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
                cad = cad.replace(self.variable[i], self.contenido[i])
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

                                print("[" + self.contenido[self.apuntador] + "]" + "<---" + self.variable[self.apuntador])
                                self.apuntador += 1
                    else:
                        self.error(myClass, "Falta ;")

    def exprecion(self):
        ope = []
        cons = []
        rest = 0
        apu1 = 0
        apu2 = 0
        for i in self.contenido[self.apuntador]:
            if ord(i) > 47 and ord(i) < 58:
                cons.append(i)
            else:
                ope.append(i)
            cons = list(map(int,cons))
        print(cons)
        print(ope)
        if

