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
                  'in': 'in', 'is': 'is', 'lambda': 'function lambda', 'not': 'negation', 'or': 'or', 'pass': 'pass', 'print': 'print', 'raise': 'raise', 'return': 'return', 'try': 'try exception', 'while': 'cicle while', 'with': 'with', 'yield': 'yield',
                  'open': 'openfile'}

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
digitos_keys = digit.keys()


def analyse():

    print("-----------------ANALIZADOR LEXICO-----------------")

    file = open("words.py")
    words = file.read()

    count_lineas = 0
    words_split = words.split('\n')

    new_words = ''

    for linea in words_split:
        count_lineas = count_lineas + 1

        print("Linea #", count_lineas, "\n", linea)

        tokens = linea.split(' ')
        print("Los tokes son", tokens)
        print("Linea #", count_lineas, "propiedades: \n")

        for token in tokens:
            if token in operadores_keys:
                print(token, "->", operadores[token])
            if token in data_keys:
                print(token, "->", tipo_data[token])
            if token in simbolos_keys:
                print(token, "->", simbolos_puntuacion[token])
            if token in identifier_key:
                print(token, "Identifier is", identifier[token])
            try:
                if token[0] in ("'", '"') and token[-1] in ("'", '"'):
                    print(token, "es una cadena de texto")
            except IndexError:
                continue
            for i in range(len(token)):
                new_words += token[i]


def analyze_token(token):
    for i in range(len(token)):
        new_words += token[i]


def main():
    analyse()


if __name__ == "__main__":
    main()
