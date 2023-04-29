import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

import ply.lex as lex
import ply.yacc as yacc
import codecs
from GenOutput import Generador
from AdminFiles import Administrador
from TestAnalizadorLexico import *

# importando la clase analizador lexico
from AnalizarLexico import *
#Construcción del analizador lexico
lexer = lex.lex()

# Importando nuestro analizador sintactico
from AnalizadorSintactico import *
parser = yacc.yacc()

class dialogo(QMainWindow):
    def __init__(self):
        super(dialogo, self).__init__()
        uic.loadUi("Inyector.ui", self)
        self.setWindowTitle("Proyecto Compiladores -- Grupo#6 -- Seccion 0900 ")
        self.open_file.clicked.connect(self.apertura)

    def apertura(self):
        self.abrir_dialogo()
    #LOCALIZANDO EL ARCHIVO
    def abrir_dialogo(self):
        filename = QFileDialog.getOpenFileName()[0]
        # print(filename)
        self.text_path.clear()
        self.text_path.append(filename)
        #ABRIENDO EL ARCHIVO SELECCIONADO
        with open(filename, 'r') as file:
            self.text_read.append(f"Las expresiones encontradas en el archivo cargado son: ".center(60,"*"))
            lineas = file.readlines()
            for linea in lineas:
                linea = linea.rstrip()
                self.text_read.append(linea)

        if (filename):
            adminArchivos = Administrador(filename)
            contenido = adminArchivos.obtenerContenido()
            parser.parse(contenido)
            self.dibujarTabla(contenido)


    def dibujarTabla(self, cadena = None):
        if not cadena: cadena = self.cadena
        g = Generador(lexer, cadena, resultados)
        contenido = g.dibujarTabla()
        #contenido.rstrip()
        self.text_read.append(contenido)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlog = dialogo()
    dlog.show()
    sys.exit(app.exec())

