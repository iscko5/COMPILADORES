from enum import Enum
import re


class Reservados(Enum):
    retornar = 'return'
    verdadero = 'true'
    mientras = 'while'
    imprimir = 'print'
    funcion = 'fun'
    ademas = 'else'
    falso = 'false'
    clase = 'class'
    super = 'super'
    este = 'this'
    nulo = 'null'
    para = 'for'
    var = 'var'
    y = 'and'
    si = 'if'
    o = 'or'


class Especiales(Enum):
    comentInicio = '/*'
    menorigual = '<='
    mayorigual = '>='
    comentFin = '*/'
    parentIzq = '('
    parentDer = ')'
    puntocoma = ';'
    llaveIzq = '{'
    llaveDer = '}'
    noigual = '!='
    iguala = '=='
    coment = '//'
    punto = '.'
    menos = '-'
    entre = '/'
    igual = '='
    menor = '<'
    mayor = '>'
    coma = ','
    mas = '+'
    por = '*'
    no = '!'

# AQUI PON LAS CLASES RESTANTES
