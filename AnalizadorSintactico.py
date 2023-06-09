# Analizador sintactico
resultados = []
operacion = {}

precedence = (
    ('left', 'SUM', 'RES'),
    ('left','POT', 'MULT', 'DIV'),
    ('right','UMENOS'),
    ('left', 'APARENT', 'CPARENT'),
    ('left', 'ACOR', 'CCOR')
)


#definicion de las producciones
def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''


def p_instrucciones_operar(t):
    'instruccion : OPERAR ACOR expresion CCOR FINAL'
    resultados.append([t[3]])
    operacion[t[1]] = t[3]

    print('El resultado de la expresión es: ' + str(t[3]))

def p_instrucciones_expr(t):
    'instruccion : expresion'
    print(t[1])

def p_expresion_binaria(t):
    '''expresion : expresion SUM expresion
                  | expresion RES expresion
                  | expresion MULT expresion
                  | expresion DIV expresion
                  | expresion POT expresion'''


    try:
        if t[2] == '+'  : t[0] = t[1] + t[3]
        elif t[2] == '-': t[0] = t[1] - t[3]
        elif t[2] == '*': t[0] = t[1] * t[3]
        elif t[2] == '/': t[0] = t[1] / t[3]
        elif t[2] == '^': t[0] = pow(t[1] , t[3])
    except ZeroDivisionError:
        error = "Error, División por cero"
        print(error)

#-[Exp] = -Exp
def p_expresion_unaria(t):
    'expresion : RES expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : APARENT expresion CPARENT'
    t[0] = t[2]


def p_expresion_number(t):
    '''expresion    : NUMERO
                    | DECIMAL'''
    t[0] = t[1]

def p_error(t):
    operacion["OPERAR"] = 0

    print("Error sintáctico en '%s'" % t.value)