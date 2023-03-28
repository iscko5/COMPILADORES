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
              '/': 'Operador División', '*': 'Operador Multiplicación', '<': 'Operador Menor que', '>': 'Operador Mayor que', '+=': 'Operador Suma Igual', "-=": 'Operador resta igual',
              '==': 'Igual Condicional'}

operadores_keys = operadores.keys()

tipo_data = {'int': 'Tipo entero', 'float': 'Tipo flotante',
             'char': 'Tipo caracter', 'long': 'Tipo long'}

data_keys = tipo_data.keys()

palabras_clave = {'and': 'and', 'as': 'as', 'assert': 'assert', 'break': 'break', 'class': 'class', 'def': 'function', 'del': 'del',
                  'elif': 'elif', 'else': 'else', 'except': 'exception', 'exec': 'exec', 'finally': 'finally', 'for': 'cicle for', 'from': 'from', 'global': 'global variable', 'if': 'if statement', 'import': 'import',
                  'in': 'in', 'is': 'is', 'lambda': 'function lambda', 'not': 'negation', 'or': 'or', 'pass': 'pass', 'print': 'print', 'raise': 'raise', 'return': 'return', 'try': 'try exception', 'while': 'cicle while', 'with': 'with', 'yield': 'yield'}

clave_keys = palabras_clave.keys()

simbolos_puntuacion = {':': 'Punto doble',
                       ';': 'Punto y coma', '.': 'Punto', ',': 'Coma', '!': 'Negación'}
simbolos_keys = simbolos_puntuacion.keys()

identifier = {"a": 'id', "b": 'id', "c": 'id', "d": 'id', "e": 'id', "f": 'id', "g": 'id', "h": 'id', "i": 'id', "j": 'id', "k": 'id', "l": 'id', "m": 'id', "n": 'id', "o": 'id',
              "p": 'id', "q": 'id', "r": 'id', "s": 'id', "t": 'id', "u": 'id', "v": 'id', "w": 'id', "x": 'id', "z": 'id', "y": 'id'}
identifier_key = identifier.keys()

digit = {"1": "uno", "2": 'dos', "3": 'tres', "4": 'cuatro', "5": 'cinco', "6": 'seis', "7": 'siete', "8": 'ocho', "9": 'nueve', "0": 'cero', "_": 'guion bajo', "?": '', "/": 'diagonal', "\\": 'comentario',
         "@": 'arroba', "$": 'signo dolar', "&": 'amperson', ")": 'Parentesís derecha', "(": 'Parentesís izquierda', "\"": 'diagonal invertida', "#": 'Signo gato',
         "[": 'Corchete izquierda', "]": 'Corchete derecha', "{": 'Parentesis izquierda', "}": 'Parentesis derecha'}
