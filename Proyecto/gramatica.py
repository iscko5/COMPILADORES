from __future__ import annotations
from lexico import *
import inspect
from inspect import getframeinfo, stack


class Gramatica:
    def __init__(self, tokens):
        self.tokens = tokens
        self.results = []

    def addNextToken(self):
        if len(self.tokens) > 0:
            self.results.append(self.tokens[0])
            del self.tokens[0]

    # Funcion para detectar tokens
    def findToken(self, term):
        if len(self.tokens) == 0:
            return False

        if type(term) is str:
            return self.tokens[0].value == term
        elif inspect.isclass(term):
            return type(self.tokens[0]) is term
        elif callable(term):
            prev = len(self.results)
            term()
            after = len(self.results)
            return after > prev
        else:
            raise Exception('Falta Término inválido')

    # PROGRAMA
    def PROGRAM(self):
        ran = False
        while self.findToken(self.DECLARATION):
            pass
            ran = True
        if not ran:
            raise Exception('Falta DECLARATION')

        return self.results

    # DECLARACIONES

    def DECLARATION(self):

        if (self.findToken(self.CLASS_DECL)):
            pass
        elif (self.findToken(self.FUNC_DECL)):
            pass
        elif (self.findToken(self.VAR_DECL)):
            pass
        elif (self.findToken(self.STATEMENT)):
            pass

    def CLASS_DECL(self):
        if (self.findToken('class')):
            self.addNextToken()
            if(self.findToken(Identificador)):
                self.addNextToken()
            else:
                raise Exception('Falta id')

            if(self.findToken(self.CLASS_INHER)):
                pass

            if(self.findToken('{')):
                self.addNextToken()
            else:
                raise Exception('Falta {')

            if(self.findToken(self.FUNCTIONS)):
                pass

            if(self.findToken('}')):
                self.addNextToken()
            else:
                raise Exception('Falta }')

    def CLASS_INHER(self):
        if (self.findToken('<')):
            self.addNextToken()

            if(self.findToken(Identificador)):
                self.addNextToken()
            else:
                raise Exception('Falta Id')

    def FUNC_DECL(self):
        if (self.findToken('fun')):
            self.addNextToken()
            if (self.findToken(self.FUNCTION)):
                pass
            else:
                raise Exception('Falta FUNCTION')

    def VAR_DECL(self):
        if (self.findToken('var')):
            self.addNextToken()

            if (self.findToken(Identificador)):
                self.addNextToken()
            else:
                raise Exception('Falta Identificador')

            if (self.findToken(self.VAR_INIT)):
                pass

            if (self.findToken(';')):
                self.addNextToken()
            else:
                raise Exception('Falta ;')

    def VAR_INIT(self):
        if (self.findToken('=')):
            self.addNextToken()

            if (self.findToken(self.EXPRESSION)):
                pass
            else:
                raise Exception('Falta EXPRESSION')

    # SENTENCIAS

    def STATEMENT(self):
        if (self.findToken(self.EXPR_STMT)):
            pass
        elif (self.findToken(self.FOR_STMT)):
            pass
        elif (self.findToken(self.IF_STMT)):
            pass
        elif (self.findToken(self.PRINT_STMT)):
            pass
        elif (self.findToken(self.RETURN_STMT)):
            pass
        elif (self.findToken(self.WHILE_STMT)):
            pass
        elif (self.findToken(self.BLOCK)):
            pass

    def EXPR_STMT(self):
        if (self.findToken(self.EXPRESSION)):
            pass
        elif (self.findToken(';')):
            self.addNextToken()

    def FOR_STMT(self):
        if (self.findToken('for')):
            self.addNextToken()

            if (self.findToken('(')):
                self.addNextToken()
            else:
                raise Exception('Falta (')

            if (self.findToken(self.FOR_STMT_1)):
                pass
            else:
                raise Exception('Falta FOR_STMT_1')

            if (self.findToken(self.FOR_STMT_2)):
                pass
            else:
                raise Exception('Falta FOR_STMT_2')

            if (self.findToken(self.FOR_STMT_3)):
                pass

            if (self.findToken(')')):
                self.addNextToken()
            else:
                raise Exception('Falta )')

            if (self.findToken(self.STATEMENT)):
                pass
            else:
                raise Exception('Falta STATEMENT')

    def FOR_STMT_1(self):
        if (self.findToken(self.VAR_DECL)):
            pass
        elif (self.findToken(self.EXPRESSION)):
            pass

    def FOR_STMT_2(self):
        if (self.findToken(self.EXPRESSION)):
            pass

        if (self.findToken(';')):
            self.addNextToken()
        else:
            raise Exception('Falta ;')

    def FOR_STMT_3(self):
        if (self.findToken(self.EXPRESSION)):
            pass

    def IF_STMT(self):
        if (self.findToken('if')):
            self.addNextToken()

            if (self.findToken('(')):
                self.addNextToken()
            else:
                raise Exception('Falta (')

            if (self.findToken(self.EXPRESSION)):
                pass
            else:
                raise Exception('Falta EXPRESSION')

            if (self.findToken(')')):
                self.addNextToken()
            else:
                raise Exception('Falta )')

            if (self.findToken(self.STATEMENT)):
                pass
            else:
                raise Exception('Falta STATEMENT')

            if (self.findToken(self.ELSE_STATEMENT)):
                pass

    def ELSE_STATEMENT(self):
        if (self.findToken('else')):
            self.addNextToken()

            if (self.findToken(self.STATEMENT)):
                pass
            else:
                raise Exception('Falta STATEMENT')

    def PRINT_STMT(self):
        if (self.findToken('print')):
            self.addNextToken()
            if (self.findToken(self.EXPRESSION)):
                pass
            else:
                raise Exception('Falta EXPRESSION')
            if (self.findToken(';')):
                self.addNextToken()
            else:
                raise Exception('Falta ;')

    def RETURN_STMT(self):
        if (self.findToken('return')):
            self.addNextToken()
            if (self.findToken(self.RETURN_EXP_OPC)):
                pass

            if (self.findToken(';')):
                self.addNextToken()
            else:
                raise Exception('Falta ;')

    def RETURN_EXP_OPC(self):
        if (self.findToken(self.EXPRESSION)):
            pass

    def WHILE_STMT(self):
        if (self.findToken('while')):
            self.addNextToken()

            if (self.findToken('(')):
                self.addNextToken()
            else:
                raise Exception('Falta (')

            if (self.findToken(self.EXPRESSION)):
                pass
            else:
                raise Exception('Falta EXPRESSION')

            if (self.findToken(')')):
                self.addNextToken()
            else:
                raise Exception('Falta )')

            if (self.findToken(self.STATEMENT)):
                pass
            else:
                raise Exception('Falta STATEMENT')

    def BLOCK(self):
        if (self.findToken('{')):
            self.addNextToken()
            if (self.findToken(self.BLOCK_DECL)):
                pass
            else:
                raise Exception('Falta BLOCK_DECL')
            if (self.findToken('}')):
                self.addNextToken()
            else:
                raise Exception('Falta }')

    def BLOCK_DECL(self):
        while (self.findToken(self.DECLARATION)):
            pass

    def EXPRESSION(self):
        if (self.findToken(self.ASSIGNMENT)):
            pass

    def ASSIGNMENT(self):
        if (self.findToken(self.LOGIC_OR)):
            pass
        elif (self.findToken(self.ASSIGNMENT_OPC)):
            pass

    def ASSIGNMENT_OPC(self):
        if (self.findToken('=')):
            self.addNextToken()
            if (self.findToken(self.EXPRESSION)):
                pass
            else:
                raise Exception('Falta EXPRESSION')

    def LOGIC_OR(self):
        if (self.findToken(self.LOGIC_AND)):
            pass
        elif (self.findToken(self.LOGIC_OR_2)):
            pass

    def LOGIC_OR_2(self):
        if (self.findToken('or')):
            self.addNextToken()
            if (self.findToken(self.LOGIC_AND)):
                pass
            else:
                raise Exception('Falta LOGIC_AND')
            if (self.findToken(self.LOGIC_OR_2)):
                pass
            else:
                raise Exception('Falta LOGIC_OR_2')

    def LOGIC_AND(self):
        if (self.findToken(self.EQUALITY)):
            pass
        elif (self.findToken(self.LOGIC_AND_2)):
            pass

    def LOGIC_AND_2(self):
        if (self.findToken('and')):
            self.addNextToken()
            if (self.findToken(self.EQUALITY)):
                pass
            else:
                raise Exception('Falta EQUALITY')
            if (self.findToken(self.LOGIC_AND_2)):
                pass
            else:
                raise Exception('Falta LOGIC_AND_2')

    def EQUALITY(self):
        if (self.findToken(self.COMPARISON)):
            pass
        elif (self.findToken(self.EQUALITY_2)):
            pass

    def EQUALITY_2(self):
        if (self.findToken('!=')):
            self.addNextToken()
            if (self.findToken(self.COMPARISON)):
                pass
            else:
                raise Exception('Falta COMPARISON')
        elif (self.findToken('==')):
            self.addNextToken()
            if (self.findToken(self.COMPARISON)):
                pass
            else:
                raise Exception('Falta COMPARISON')

    def COMPARISON(self):
        if (self.findToken(self.TERM)):
            pass
        while (self.findToken(self.COMPARISON_2)):
            pass

    def COMPARISON_2(self):
        if (self.findToken('>')):
            self.addNextToken()
            if (self.findToken(self.TERM)):
                pass
            else:
                raise Exception('Falta TERM')

        elif (self.findToken('>=')):
            self.addNextToken()
            if (self.findToken(self.TERM)):
                pass
            else:
                raise Exception('Falta TERM')

        elif (self.findToken('<')):
            self.addNextToken()
            if (self.findToken(self.TERM)):
                pass
            else:
                raise Exception('Falta TERM')

        elif (self.findToken('<=')):
            self.addNextToken()
            if (self.findToken(self.TERM)):
                pass
            else:
                raise Exception('Falta TERM')

    def TERM(self):
        if (self.findToken(self.FACTOR)):
            pass
        while (self.findToken(self.TERM_2)):
            pass

    def TERM_2(self):
        if (self.findToken('-')):
            self.addNextToken()
            if (self.findToken(self.FACTOR)):
                pass
            else:
                raise Exception('Falta FACTOR')
        elif (self.findToken('+')):
            self.addNextToken()
            if (self.findToken(self.FACTOR)):
                pass
            else:
                raise Exception('Falta FACTOR')

    def FACTOR(self):
        if (self.findToken(self.UNARY)):
            pass
        elif (self.findToken(self.FACTOR_2)):
            pass

    def FACTOR_2(self):
        if (self.findToken('/')):
            self.addNextToken()
            if (self.findToken(self.UNARY)):
                pass
            else:
                raise Exception('Falta UNARY')
            if (self.findToken(self.FACTOR_2)):
                pass
            else:
                raise Exception('Falta FACTOR_2')
        if (self.findToken('*')):
            self.addNextToken()
            if (self.findToken(self.UNARY)):
                pass
            else:
                raise Exception('Falta UNARY')
            if (self.findToken(self.FACTOR_2)):
                pass
            else:
                raise Exception('Falta FACTOR_2')

    def UNARY(self):
        if (self.findToken('!')):
            self.addNextToken()
            if (self.findToken(self.UNARY)):
                pass
            else:
                raise Exception('Falta UNARY')
        elif (self.findToken('-')):
            self.addNextToken()
            if (self.findToken(self.UNARY)):
                pass
            else:
                raise Exception('Falta UNARY')
        elif (self.findToken(self.CALL)):
            pass

    def CALL(self):
        if (self.findToken(self.PRIMARY)):
            pass
        elif (self.findToken(self.CALL_2)):
            pass

    def CALL_2(self):
        if (self.findToken('(')):
            self.addNextToken()
            if (self.findToken(self.ARGUMENTS_OPC)):
                pass
            if (self.findToken(')')):
                self.addNextToken()
            else:
                raise Exception('Falta )')
            if (self.findToken(self.CALL_2)):
                pass
        elif (self.findToken('.')):
            self.addNextToken()
            if (self.findToken(Identificador)):
                self.addNextToken()
            if (self.findToken(self.CALL_2)):
                pass

    def PRIMARY(self):
        if (self.findToken('true')):
            self.addNextToken()
        elif (self.findToken('false')):
            self.addNextToken()
        elif (self.findToken('null')):
            self.addNextToken()
        elif (self.findToken('this')):
            self.addNextToken()
        elif (self.findToken(Numero)):
            self.addNextToken()
        elif (self.findToken(Cadena)):
            self.addNextToken()
        elif (self.findToken(Identificador)):
            self.addNextToken()
        elif (self.findToken('(')):
            self.addNextToken()
            if (self.findToken(self.EXPRESSION)):
                pass
            if (self.findToken(')')):
                self.addNextToken()
            else:
                raise Exception('Falta )')
        elif (self.findToken('super')):
            self.addNextToken()
            if (self.findToken('.')):
                self.addNextToken()
            else:
                raise Exception('Falta .')
            if (self.findToken(Identificador)):
                self.addNextToken()
            else:
                raise Exception('Falta id')

    # OTRAS

    def FUNCTION(self):
        if (self.findToken(Identificador)):
            self.addNextToken()
            if (self.findToken('(')):
                self.addNextToken()
            else:
                raise Exception('Falta (')
            if (self.findToken(self.PARAMETER_OPC)):
                pass
            if (self.findToken(')')):
                self.addNextToken()
            else:
                raise Exception('Falta )')
            if (self.findToken(self.BLOCK)):
                pass
            else:
                raise Exception('Falta BLOCK')

    def FUNCTIONS(self):
        while (self.findToken(self.FUNCTION)):
            pass

    def PARAMETER_OPC(self):
        if (self.findToken(self.PARAMETERS)):
            pass

    def PARAMETERS(self):
        if (self.findToken(Identificador)):
            self.addNextToken()
            if (self.findToken(self.PARAMETERS_2)):
                pass
            else:
                raise Exception('Falta PARAMETERS_2')

    def PARAMETERS_2(self):
        while (self.findToken(',')):
            self.addNextToken()
            if (self.findToken(Identificador)):
                self.addNextToken()
            else:
                raise Exception('Falta id')

    def ARGUMENTS_OPC(self):
        if (self.findToken(self.ARGUMENTS)):
            pass

    def ARGUMENTS(self):
        if (self.findToken(self.EXPRESSION)):
            pass
            if (self.findToken(self.ARGUMENTS_2)):
                pass

    def ARGUMENTS_2(self):
        while (self.findToken(',')):
            self.addNextToken()
            if (self.findToken(self.EXPRESSION)):
                pass
            else:
                raise Exception('Falta EXPRESSION')
