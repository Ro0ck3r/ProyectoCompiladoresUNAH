from AnalizarLexico import *
import ply.lex as lex;
import re
import codecs
import os
import sys

def test():
    test = 'C:/Users/t4v0-PC/Downloads/prueba1.txt'

    fp = codecs.open(test, "r", "utf-8")
    cadena = fp.read()
    fp.close()

    analizador = lex.lex()
    analizador.input(cadena)


    while True:
        token = analizador.token()
        if not token: break
        print(token)
