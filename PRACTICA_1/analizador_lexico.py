"""
    ANALIZADOR LEXICO
    
    Alumnos:
        - Sánchez Verdiguel Isaac
        - Morales Víctor
    Materia:
        Compiladores
    
"""

# Diccionarios necesarios

operadores = {'=': 'Operador Igual', '+': 'Operador Suma', '-': 'Operador Resta',
              '/': 'Operador División', '*': 'Operador Multiplicación', '<': 'Operador Menor que', '>': 'Operador Mayor que', '=+': 'Operador Suma Igual'}

operadores_keys = operadores.keys()

tipo_data = {'int': 'Tipo entero', 'float': 'Tipo flotante',
             'char': 'Tipo caracter', 'long': 'Tipo long'}

data_keys = tipo_data.keys()

palabras_clave = {'and': 'and', 'as': 'as', 'assert': 'assert', 'break': 'break', 'class': 'class', 'def': 'function', 'del': 'del',
                  'elif': 'elif', 'else': 'else', 'except': 'exception', 'exec': 'exec', 'finally': 'finally', 'for': 'cicle for', 'from': 'from', 'global': 'global variable', 'if': 'if statement', 'import': 'import',
                  'in': 'in', 'is': 'is', 'lambda': 'function lambda', 'not': 'negation', 'or': 'or', 'pass': 'pass', 'print': 'print', 'raise': 'raise', 'return': 'return', 'try': 'try exception', 'while': 'cicle while', 'with': 'with', 'yield': 'yield'}

clave_keys = palabras_clave.keys()
