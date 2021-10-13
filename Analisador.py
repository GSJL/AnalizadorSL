
class Analizador:
    __constantes = []
    __operadores = []
    __variables = []
    __stack_c = []
    __stack_o = []
    __ind_op = 0
    __ind_const = 0

    def separateSymbols(self, operacion):
        operacion += " "
        for i in range(len(operacion)):
            if operacion[i] == '+' or operacion[i]== '-' or operacion[i]== '*' or operacion[i]== '/' \
                    or operacion[i]== '(' or operacion[i]== ')'or operacion[i]== '=':
                self.__operadores.append(operacion[i])
            elif ord(operacion[i]) > 47 and ord(operacion[i])< 58:
                self.__constantes.append(operacion[i])
            elif operacion[i] != " ":
                self.__variables.append(operacion[i])



    def printTest(self):
        print(self.__constantes)
        print(self.__operadores)
        print(self.__variables)
        print('final')


if __name__ == '__main__':
    print("Aqui no xd")