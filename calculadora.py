import ply.lex as lex
import ply.yacc as yacc
import codecs

from GenOutput import Generador
from AdminFiles import Administrador

# importando nuestro analizador lexico
from AnalizarLexico import *

# Construcción del analizador lexico
lexer = lex.lex()

# Importando nuestro analizador sintactico
from AnalizadorSintactico import *

parser = yacc.yacc()


class Calculadora:
    def __init__(self, expresion):
        self.expresion = expresion

    def calcular(self):
        parser.parse(self.expresion)
