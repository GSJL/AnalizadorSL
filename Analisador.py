
class Analizador:
    __constantes = []
    __operadores = []
    __variables = []
    __stack_cons = []
    __stack_op = []
    __ind_op = 0
    __ind_const = 0

    def separateSymbols(self, operacion):
        operacion += " "
        for i in range(len(operacion)):
            if operacion[i] == '+' or operacion[i]== '-' or operacion[i]== '*' or operacion[i]== '/' \
                    or operacion[i]== '(' or operacion[i]== ')'or operacion[i]== '=':
                self.__operadores.append(operacion[i])
            elif ord(operacion[i]) > 47 and ord(operacion[i])< 58:
                res = ""
                while ord(operacion[i]) > 47 and ord(operacion[i])< 58:
                    res+= operacion[i]
                    i+= 1
                i -= 1
                self.__constantes.append(res)
            elif operacion[i] != " ":
                self.__variables.append(operacion[i])


    def printTest(self):
        print(self.__constantes)
        print(self.__operadores)
        print(self.__variables)
        print('final')


if __name__ == '__main__':
    print("Aqui no xd")