from Analisador import Analizador as Lex

numero = input("Ingrese su operacion: ")

Lex.separateSymbols(Lex, numero)
Lex.printTest(Lex)