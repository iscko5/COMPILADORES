import sys
from lexico import *
from gramatica import *
import traceback


def readFile(filename):
    lines = []
    with open(filename) as archivo:
        lines = archivo.read()
    return lines


def processInput(input):
    tokens: list = Lexico.getTokens(input)

    for token in tokens:
        print(token.__str__())

    tokens = list(filter(lambda token: not (
        type(token) is Comentario), tokens))

    try:
        gramatica = Gramatica(tokens)
        stack = gramatica.PROGRAM()
    except Exception as error:
        print(traceback.format_exc())
        print(error)
    else:
        # for unit in stack:
        #     print(unit.__str__())
        print("Sentencia válida")


fileName = sys.argv[1] if len(sys.argv) > 1 else ""

if fileName != "":
    print(f"Procesando archivo {fileName}...")
    lines = re.sub(r'\n+', '\n', readFile(fileName))
    processInput(lines)
else:
    while (True):
        line = input("> ")
        processInput(line)
