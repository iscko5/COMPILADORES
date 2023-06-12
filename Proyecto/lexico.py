from enum import Enum
import re


class Lexico:
    def getTokens(input):
        tokens = []
        # Comentarios
        for search in re.finditer('\/\*\*\/', input, flags=re.DOTALL):
            tokens.append({'index': search.start(),
                          "value": Comentario(search.group(0))})
            input = input.replace(search.group(
                0), ' ' * len(search.group(0)), 1)
        for search in re.finditer('\/\/.*\n', input):
            tokens.append({'index': search.start(),
                          "value": Cadena(search.group(0))})
            input = input.replace(search.group(
                0), ' ' * len(search.group(0)), 1)
        input = input.replace('\n', '')

        # Cadenas
        for search in re.finditer('\".*\"', input):
            tokens.append({'index': search.start(),
                          "value": Cadena(search.group(0))})
            input = input.replace(search.group(
                0), ' ' * len(search.group(0)), 1)

        # Numeros
        for search in re.finditer('\d+(.?\d+)', input):
            tokens.append({'index': search.start(),
                          "value": Numero(search.group(0))})
            input = input.replace(search.group(
                0), ' ' * len(search.group(0)), 1)
            print(tokens)

        # Especiales
        for search in re.finditer('!=|==|<=|>=|\/\/|\/\*|\*\/|\(|\)|{|}|,|\.|;|-|\+|\*|\/|!|=|<|>', input):
            tokens.append({'index': search.start(),
                          "value": Especiales(search.group(0))})
            input = input.replace(search.group(
                0), ' ' * len(search.group(0)), 1)

        # Reservados
        for search in re.finditer('(?:^|\W)(false|return|while|class|print|super|this|true|else|null|for|fun|var|if|and|or)(?:^|\W)', input, flags=re.MULTILINE):
            tokens.append({'index': search.start(),
                          "value": Reservados(search.group(1))})
            input = input.replace(search.group(
                1), ' ' * len(search.group(1)), 1)

        # Identificadores
        for search in re.finditer('\S+', input, flags=re.IGNORECASE):
            tokens.append({'index': search.start(),
                          "value": Identificador(search.group(0))})
            input = input.replace(search.group(
                0), ' ' * len(search.group(0)), 1)

        tokens = sorted(tokens, key=lambda token: token['index'])
        tokens = [token['value'] for token in tokens]

        return tokens


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


class Numero:
    def _init_(self, string) -> None:
        self.value = string

    def _str_(self) -> str:
        return 'Numero.' + self.value


class Cadena:
    def _init_(self, string) -> None:
        self.value = string

    def _str_(self) -> str:
        return 'Cadena.' + self.value


class Comentario:
    def _init_(self, string) -> None:
        self.value = string

    def _str_(self) -> str:
        return 'Comentario.' + self.value


class Identificador:
    def _init_(self, string) -> None:
        self.value = string

    def _str_(self) -> str:
        return 'Identificador.' + self.value
