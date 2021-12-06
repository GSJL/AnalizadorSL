
class Analizador:
    __constantes = []
    __operadores = []
    __variables = []
    __list_v = []
    __ord = []


    def separateSymbols(self, operacion):
        operacion += " "
        i = 0
        while i < (len(operacion)):
            if operacion[i] == '+' or operacion[i]== '-' or operacion[i]== '*' or operacion[i]== '/' \
                    or operacion[i]== '(' or operacion[i]== ')':
                self.__operadores.append(operacion[i])
                self.__ord.append(1)
            elif ord(operacion[i]) > 47 and ord(operacion[i])< 58:
                res = ""
                while ord(operacion[i]) > 47 and ord(operacion[i])< 58:
                    res+= operacion[i]
                    i+=1
                i-=1
                self.__constantes.append(res)
                self.__ord.append(2)
            elif operacion[i] != " " and operacion[i] != "=":
                self.__variables.append(operacion[i])
                self.__ord.append(3)
            elif operacion[i] == '=':
                res = ""
                i+=1
                if operacion[i] == " ":
                    i+=1
                    res = self.dobCaracter(operacion,i)
                else:
                    res = self.dobCaracter(operacion,i)
                self.__list_v.append(res)
                self.__ord.append(4)
                i+=1
            i+=1


    def dobCaracter(operacion, i):
        res = ""
        while ord(operacion[i]) > 47 and ord(operacion[i])< 58:
            res+= operacion[i]
            i+=1
        i-=1
        return res


    def printTest(self):
        print(self.__constantes)
        print(self.__operadores)
        print(self.__variables)
        print(self.__list_v)
        print('final')


if __name__ == '__main__':
    print("Aqui no xd")