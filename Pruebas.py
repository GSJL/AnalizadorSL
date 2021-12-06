from Analizador import myClass as Lex
from tkinter import Tk
from tkinter.filedialog import askopenfilename

print("Archivo....")
Tk().withdraw()
filename = askopenfilename()
data = []
with open(filename, 'r') as f:
    for line in f:
        data.append(line.rstrip())
    if data:
        Lex.Analizar(Lex, data)
    else:
        print("Archivo no apto")