from __future__ import annotations
from enums import *


class Patterns:
    # PROGRAMA
    """
    def PROGRAM(self):
        print("PROGRAM")
        return [
            {
                'match': self.DECLARATION,
                'required': True,
                'looping': True,
                'error': 'DECLARATION faltante'
            }
        ]
    """

    # Aqui el loooping que no se cómo va
    def PROGRAM(self):
        result = []
        while (self.findToken(self.DECLARATION)):
            result.append(self.tokens[0])
            del self.tokens[0]
        if len(result) == 0:
            raise Exception('DECLARATION faltante')
        return result

    # DECLARACIONES

    """
    def DECLARATION(self):
        print("DECLARATION")
        return [
            {
                'match': self.CLASS_DECL,
                'required': False
            },
            {
                'match': self.FUN_DECL,
                'required': False
            },
            {
                'match': self.VAR_DECL,
                'required': False
            },
            {
                'match': self.STATEMENT,
                'required': False
            },
        ]
    
    """

    def DECLARATION(self):
        result = []
        if (self.findToken(self.CLASS_DECL)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.FUNC_DECL)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.VAR_DECL)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.STATEMENT)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
        def CLASS_DECL(self):
        print("CLASS_DECL")
        return [
            {
                'match': 'class',
                'required': False,
                'error': 'class faltante',
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'id faltante'
                    },
                    {
                        'match': self.CLASS_INHER,
                        'required': True,
                        'error': 'CLASS_INHER faltante'
                    },
                    {
                        'match': '{',
                        'required': True,
                        'error': '{ faltante'
                    },
                    {
                        'match': self.FUNCTIONS,
                        'required': True,
                        'error': 'FUNCTIONS faltante'
                    },
                    {
                        'match': '}',
                        'required': True,
                        'error': '} faltante'
                    }
                ]
            }
        ]

    """

    def CLASS_DECL(self):
        result = []
        if (self.findToken('class')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if(self.findToken(Identificador)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('id faltante')

            if(self.findToken(self.CLASS_INHER)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('CLASS_INHER faltante')

            if(self.findToken('{')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('{ faltante')

            if(self.findToken(self.FUNCTIONS)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FUNCTIONS faltante')

            if(self.findToken('}')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('} faltante')
        return result

    """
    def CLASS_INHER(self):
        print("CLASS_INHER")
        return [
            {
                'match': '<',
                'required': True,
                'error': '< faltante',
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'id faltante'
                    }
                ]
            },
        ]
    """

    def CLASS_INHER(self):
        result = []
        if (self.findToken('<')):
            result.append(self.tokes[0])
            del self.tokes[0]

            if(self.findToken(Identificador)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('Id faltante')
        else:
            raise Exception('< faltante')
        return result

    """
    def FUN_DECL(self):
        print("FUN_DECL")
        return [
            {
                'match': 'fun',
                'required': False,
                'error': 'fun faltante',
                'next': [
                    {
                        'match': self.FUNCTION,
                        'required': True,
                        'error': 'FUNCTION faltante'
                    }
                ]
            }
        ]
    """

    def FUN_DECL(self):
        result = []
        if (self.findToken('fun')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.FUNCTION)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FUNCTION faltante')
        return result

    """
    def VAR_DECL(self):
        print("VAR_DECL")
        return [
            {
                'match': 'var',
                'required': False,
                'error': 'var faltante',
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'Identificador faltante'
                    },
                    {
                        'match': self.VAR_INIT,
                        'required': False,
                        'error': 'VAR_INIT faltante'
                    },
                    {
                        'match': ';',
                        'required': True,
                        'error': '; faltante'
                    }
                ]
            }
        ]
    """

    def VAR_DECL(self):
        result = []
        if (self.findToken('var')):
            result.append(self.tokens[0])
            del self.tokens[0]

            if (self.findToken(Identificador)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('Identificador faltante')

            if (self.findToken(self.VAR_INIT)):
                result.append(self.tokens[0])
                del self.tokens[0]

            if (self.findToken(';')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('; faltante')
        return result

    """
    def VAR_INIT(self):
        print("VAR_INIT")
        return [
            {
                'match': '=',
                'required': False,
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'EXPRESSION faltante 1'
                    }
                ]
            },
        ]
    """

    def VAR_INIT(self):
        result = []
        if (self.findToken('=')):
            result.append(self.tokens[0])
            del self.tokens[0]

            if (self.findToken(self.EXPRESSION)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('EXPRESSION faltante 1')
        return result

    # SENTENCIAS
    """
    def STATEMENT(self):
        print("STATEMENT")
        return [
            {
                'match': self.EXPR_STMT,
                'required': False,
                'error': 'EXPR_STMT faltante'
            },
            {
                'match': self.FOR_STMT,
                'required': False,
                'error': 'FOR_STMT faltante'
            },
            {
                'match': self.IF_STMT,
                'required': False,
                'error': 'IF_STMT faltante'
            },
            {
                'match': self.PRINT_STMT,
                'required': False,
                'error': 'PRINT_STMT faltante'
            },
            {
                'match': self.RETURN_STMT,
                'required': False,
                'error': 'RETURN_STMT faltante'
            },
            {
                'match': self.WHILE_STMT,
                'required': False,
                'error': 'WHILE_STMT faltante'
            },
            {
                'match': self.BLOCK,
                'required': False,
                'error': 'BLOCK faltante'
            },
        ]
    
    """

    def STATEMENT(self):
        result = []
        if (self.findToken(self.EXPR_STMT)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.FOR_STMT)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.IF_STMT)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.PRINT_STMT)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.RETURN_STMT)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.WHILE_STMT)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.BLOCK)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
     def EXPR_STMT(self):
        print("EXPR_STMT")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
                'error': 'EXPRESSION faltante 2',
            }, {
                'match': ';',
                'required': False,
                'error': '; faltante 2'
            }
        ]
    """

    def EXPR_STMT(self):
        result = []
        if (self.findToken(self.EXPRESSION)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(';')):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def FOR_STMT(self):
        print("FOR_STMT")
        return [
            {
                'match': 'for',
                'required': False,
                'error': 'for faltante',
                'next': [
                    {
                        'match': '(',
                        'required': True,
                        'error': '( faltante'
                    },
                    {
                        'match': self.FOR_STMT_1,
                        'required': True,
                        'error': 'FOR_STMT_1 faltante'
                    },
                    {
                        'match': self.FOR_STMT_2,
                        'required': True,
                        'error': 'FOR_STMT_2 faltante'
                    },
                    {
                        'match': self.FOR_STMT_3,
                        'required': False,
                        'error': 'FOR_STMT_3 faltante'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': ') faltante'
                    },
                    {
                        'match': self.STATEMENT,
                        'required': True,
                        'error': 'STATEMENT faltante'
                    },
                ]
            },
        ]
    """

    def FOR_STMT(self):
        result = []
        if (self.findToken('for')):
            result.append(self.tokens[0])
            del self.tokens[0]

            if (self.findToken('(')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('( faltante')

            if (self.findToken(self.FOR_STMT_1)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FOR_STMT_1 faltante')

            if (self.findToken(self.FOR_STMT_2)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FOR_STMT_2 faltante')

            if (self.findToken(self.FOR_STMT_3)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FOR_STMT_3 faltante')

            if (self.findToken(')')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception(') faltante')

            if (self.findToken(self.STATEMENT)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('STATEMENT faltante')
        return result
    """
     def FOR_STMT_1(self):
        print("FOR_STMT_1")
        return [
            {
                'match': self.VAR_DECL,
                'required': False,
                'error': 'VAR_DECL faltante'
            },
            {
                'match': self.EXPR_STMT,
                'required': False,
                'error': 'EXPR_STMT faltante'
            },
            # {
            #     'match': ';',
            #     'required': False,
            #     'error': '; faltante'
            # },
        ]
    """

    def FOR_STMT_1(self):
        result = []
        if (self.findToken(self.VAR_DECL)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.EXPR_STM)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def FOR_STMT_2(self):
        print("FOR_STMT_2")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
                'error': 'EXPRESSION faltante 3'
            },
            {
                'match': ';',
                'required': True,
                'error': '; faltante'
            },
        ]
    """

    def FOR_STMT_2(self):
        result = []
        if (self.findToken(self.EXPRESSION)):
            result.append(self.tokens[0])
            del self.tokens[0]

        if (self.findToken(';')):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('; faltante')
        return result

    """
    def FOR_STMT_3(self):
        print("FOR_STMT_3")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
                'error': 'EXPRESSION faltante 4'
            },
        ]
    """

    def FOR_STMT_3(self):
        result = []
        if (self.findToken(self.EXPRESSION)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def IF_STMT(self):
        print("IF_STMT")
        return [
            {
                'match': 'if',
                'required': False,
                'error': 'if faltante',
                'next': [
                    {
                        'match': '(',
                        'required': True,
                        'error': '( faltante'
                    },
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'EXPRESSION faltante 5'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': ') faltante'
                    },
                    {
                        'match': self.STATEMENT,
                        'required': True,
                        'error': 'STATEMENT faltante'
                    },
                    {
                        'match': self.ELSE_STATEMENT,
                        'required': False,
                        'error': 'ELSE_STATEMENT faltante'
                    },
                ]
            },
        ]
    """

    def IF_STMT(self):
        result = []
        if (self.findToken('if')):
            result.append(self.tokens[0])
            del self.tokens[0]

            if (self.findToken('(')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('( faltante')

            if (self.findToken(self.EXPRESSION)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('EXPRESSION faltante 5')

            if (self.findToken(')')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception(') faltante')

            if (self.findToken(self.STATEMENT)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('STATEMENT faltante')

            if (self.findToken(self.ELSE_STATEMENT)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('ELSE_STATEMENT faltante')

        return result

    """
    def ELSE_STATEMENT(self):
        print("ELSE_STATEMENT")
        return [
            {
                'match': 'else',
                'required': False,
                'next': [
                    {
                        'match': self.STATEMENT,
                        'required': True,
                        'error': 'STATEMENT faltante'
                    },
                ]
            },
        ]
    """

    def ELSE_STATEMENT(self):
        result = []
        if (self.findToken('else')):
            result.append(self.tokens[0])
            del self.tokens[0]

            if (self.findToken(self.STATEMENT)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('STATEMENT faltante')

    """
    def PRINT_STMT(self):
        print("PRINT_STMT")
        return [
            {
                'match': 'print',
                'required': False,
                'error': 'print faltante',
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'EXPRESSION faltante 6'
                    },
                    {
                        'match': ';',
                        'required': True,
                        'error': '; faltante'
                    },
                ]
            },
        ]
    """

    def PRINT_STMT(self):
        result = []
        if (self.findToken('print')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.EXPRESSION)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('EXPRESSION faltante 6')
            if (self.findToken(';')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('; faltante')

    """
    def RETURN_STMT(self):
        print("RETURN_STMT")
        return [
            {
                'match': 'return',
                'required': False,
                'error': 'return faltante',
                'next': [
                    {
                        'match': self.RETURN_EXP_OPC,
                        'required': False,
                        'error': 'RETURN_EXP_OPC faltante'
                    },
                    {
                        'match': ';',
                        'required': True,
                        'error': '; faltante'
                    },
                ]
            },
        ]
    """

    def RETURN_STMT(self):
        result = []
        if (self.findToken('return')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.RETURN_EXP_OPC)):
                result.append(self.tokens[0])
                del self.tokens[0]

            if (self.findToken(';')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('; faltante')
        return result

    """
    def RETURN_EXP_OPC(self):
        print("RETURN_EXP_OPC")
        return [
            {
                'match': self.EXPRESSION,
                'required': False,
            },
        ]
    """

    def RETURN_EXP_OPC(self):
        result = []
        if (self.findToken(self.EXPRESSION)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
     def WHILE_STMT(self):
        print("WHILE_STMT")
        return [
            {
                'match': 'while',
                'required': False,
                'error': 'while faltante',
                'next': [
                    {
                        'match': '(',
                        'required': True,
                        'error': '( faltante'
                    },
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'EXPRESSION faltante 7'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': ') faltante'
                    },
                    {
                        'match': self.STATEMENT,
                        'required': True,
                        'error': 'STATEMENT faltante'
                    },
                ]
            },

        ]
    """

    def WHILE_STMT(self):
        result = []
        if (self.findToken('while')):
            result.append(self.tokens[0])
            del self.tokens[0]

            if (self.findToken('(')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('( faltante')

            if (self.findToken(self.EXPRESSION)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('EXPRESSION faltante 7')

            if (self.findToken(')')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception(') faltante')

            if (self.findToken(self.STATEMENT)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('STATEMENT faltante')

        return result

    """
    def BLOCK(self):
        print("BLOCK")
        return [
            {
                'match': '{',
                'required': False,
                'error': '{ faltante',
                'next': [
                    {
                        'match': self.BLOCK_DECL,
                        'required': True,
                        'error': 'BLOCK_DECL faltante'
                    },
                    {
                        'match': '}',
                        'required': True,
                        'error': '} faltante'
                    },
                ]
            },
        ]
    """

    def BLOCK(self):
        result = []
        if (self.findToken('{')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.BLOCK_DECL)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('BLOCK_DECL faltante')
            if (self.findToken('}')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('} faltante')
        return result

    """
    def BLOCK_DECL(self):
        print("BLOCK_DECL")
        return [
            {
                'match': self.DECLARATION,
                'required': False,
                'looping': True
            },
        ]
    """

    def BLOCK_DECL(self):
        result = []
        while (self.findToken(self.DECLARATION)):
            result.append(self.tokens[0])
            del self.tokens[0]
        # if len(result) == 0:
            #raise Exception('DECLARATION faltante')
        return result

    # EXPRESIONES
    """
    def EXPRESSION(self):
        print("EXPRESSION")
        return [
            {
                'match': self.ASSIGNMENT,
                'required': False,
                'error': 'ASSIGNMENT faltante'
            }
        ]
    """

    def EXPRESSION(self):
        result = []
        if (self.findToken(self.ASSIGNMENT)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def ASSIGNMENT(self):
        print("ASSIGNMENT")
        return [
            {
                'match': self.LOGIC_OR,
                'required': False,
                'error': 'LOGIC_OR faltante'
            },
            {
                'match': self.ASSIGNMENT_OPC,
                'required': False,
                'error': 'ASSIGNMENT_OPC faltante'
            },
        ]
    """

    def ASSIGNMENT(self):
        result = []
        if (self.findToken(self.LOGIC_OR)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.ASSIGNMENT_OPC)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def ASSIGNMENT_OPC(self):
        print("ASSIGNMENT_OPC")
        return [
            {
                'match': '=',
                'required': False,
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'EXPRESSION faltante 8'
                    },
                ]
            },
        ]
    """

    def ASSIGNMENT_OPC(self):
        result = []
        if (self.findToken('=')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.EXPRESSION)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('EXPRESSION faltante 8')

    """
    def LOGIC_OR(self):
        print("LOGIC_OR")
        return [
            {
                'match': self.LOGIC_AND,
                'required': False,
                'error': 'LOGIC_AND faltante'
            }, {
                'match': self.LOGIC_OR_2,
                'required': False,
                'error': 'LOGIC_OR_2 faltante'
            }
        ]
    """

    def LOGIC_OR(self):
        result = []
        if (self.findToken(self.LOGIC_AND)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.LOGIC_OR_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def LOGIC_OR_2(self):
        print("LOGIC_OR_2")
        return [
            {
                'match': 'or',
                'required': False,
                'next': [
                    {
                        'match': self.LOGIC_AND,
                        'required': True,
                        'error': 'LOGIC_AND faltante'
                    },
                    {
                        'match': self.LOGIC_OR_2,
                        'required': True,
                        'error': 'LOGIC_OR_2 faltante'
                    },
                ]
            },
        ]
    """

    def LOGIC_OR_2(self):
        result = []
        if (self.findToken('or')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.LOGIC_AND)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('LOGIC_AND faltante')
            if (self.findToken(self.LOGIC_OR_2)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('LOGIC_OR_2 faltante')
        return result

    """
    def LOGIC_AND(self):
        print("LOGIC_AND")
        return [
            {
                'match': self.EQUALITY,
                'required': False,
                'error': 'EQUALITY faltante',
            }, {
                'match': self.LOGIC_AND_2,
                'required': False,
                'error': 'LOGIC_AND_2 faltante'
            }
        ]
    """

    def LOGIC_AND(self):
        result = []
        if (self.findToken(self.EQUALITY)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.LOGIC_AND_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def LOGIC_AND_2(self):
        print("LOGIC_AND_2")
        return [
            {
                'match': 'and',
                'required': False,
                'next': [
                    {
                        'match': self.EQUALITY,
                        'required': True,
                        'error': 'EQUALITY faltante'
                    },
                    {
                        'match': self.LOGIC_AND_2,
                        'required': True,
                        'error': 'LOGIC_AND_2 faltante'
                    },
                ]
            },
        ]
    """

    def LOGIC_AND_2(self):
        result = []
        if (self.findToken('and')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.EQUALITY)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('EQUALITY faltante')
            if (self.findToken(self.LOGIC_AND_2)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('LOGIC_AND_2 faltante')
        return result

    """
    def EQUALITY(self):
        print("EQUALITY")
        return [
            {
                'match': self.COMPARISON,
                'required': False,
                'error': 'COMPARISON faltante'
            },
            {
                'match': self.EQUALITY_2,
                'required': False,
                'error': 'EQUALITY_2 faltante'
            },
        ]
    """

    def EQUALITY(self):
        result = []
        if (self.findToken(self.COMPARISON)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.EQUALITY_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def EQUALITY_2(self):
        print("EQUALITY_2")
        return [
            {
                'match': '!=',
                'required': False,
                'next': [
                    {
                        'match': self.COMPARISON,
                        'required': True,
                        'error': 'COMPARISON faltante'
                    },
                ]
            },
            {
                'match': '==',
                'required': False,
                'next': [
                    {
                        'match': self.COMPARISON,
                        'required': True,
                        'error': 'COMPARISON faltante'
                    },
                ]
            },
        ]
    """
    # duda

    def EQUALITY_2(self):
        result = []
        if (self.findToken('!=')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.COMPARISON)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('COMPARISON faltante')
        elif (self.findToken('==')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.COMPARISON)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('COMPARISON faltante')
        return result

    """
    def COMPARISON(self):
        print("COMPARISON")
        return [
            {
                'match': self.TERM,
                'required': False,
                'error': 'TERM faltante',
            }, {
                'match': self.COMPARISON_2,
                'required': False,
                'looping': True,
                'error': 'COMPARISON_2 faltante'
            }
        ]
    """
    # duda

    def COMPARISON(self):
        result = []
        if (self.findToken(self.TERM)):
            result.append(self.tokens[0])
            del self.tokens[0]
        while (self.findToken(self.COMPARISON_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    ef COMPARISON_2(self):
        print("COMPARISON_2")
        return [
            {
                'match': '>',
                'required': False,
                'next': [
                    {
                        'match': self.TERM,
                        'required': True,
                        'error': 'TERM faltante'
                    },
                ]
            },
            {
                'match': '>=',
                'required': False,
                'next': [
                    {
                        'match': self.TERM,
                        'required': True,
                        'error': 'TERM faltante'
                    },
                ]
            },
            {
                'match': '<',
                'required': False,
                'next': [
                    {
                        'match': self.TERM,
                        'required': True,
                        'error': 'TERM faltante'
                    },
                ]
            },
            {
                'match': '<=',
                'required': False,
                'next': [
                    {
                        'match': self.TERM,
                        'required': True,
                        'error': 'TERM faltante'
                    },
                ]
            },
        ]
    """

    def COMPARISON_2(self):
        result = []
        if (self.findToken('>')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.TERM)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('TERM faltante')

        elif (self.findToken('>=')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.TERM)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('TERM faltante')

        elif (self.findToken('<')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.TERM)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('TERM faltante')

        elif (self.findToken('<=')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.TERM)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('TERM faltante')
        return result

    """
    def TERM(self):
        print("TERM")
        return [
            {
                'match': self.FACTOR,
                'required': False,
                'error': 'FACTOR faltante',
            }, {
                'match': self.TERM_2,
                'required': False,
                'error': 'TERM_2 faltante',
                'looping': True
            }
        ]
    """

    def TERM(self):
        result = []
        if (self.findToken(self.FACTOR)):
            result.append(self.tokens[0])
            del self.tokens[0]
        while (self.findToken(self.TERM_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
     def TERM_2(self):
        print("TERM_2")
        return [
            {
                'match': '-',
                'required': False,
                'next': [
                    {
                        'match': self.FACTOR,
                        'required': True,
                        'error': 'FACTOR faltante'
                    },
                ]
            },
            {
                'match': '+',
                'required': False,
                'next': [
                    {
                        'match': self.FACTOR,
                        'required': True,
                        'error': 'FACTOR faltante'
                    },
                ]
            },
        ]
    """

    def TERM_2(self):
        result = []
        if (self.findToken('-')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.FACTOR)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FACTOR faltante')
        elif (self.findToken('+')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.FACTOR)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FACTOR faltante')
        return result

    """
    def FACTOR(self):
        print("FACTOR")
        return [
            {
                'match': self.UNARY,
                'required': False,
                'error': 'UNARY faltante'
            },
            {
                'match': self.FACTOR_2,
                'required': False,
                'error': 'FACTOR_2 faltante'
            },
        ]
    """

    def FACTOR(self):
        result = []
        if (self.findToken(self.UNARY)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.FACTOR_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def FACTOR_2(self):
        print("FACTOR_2")
        return [
            {
                'match': '/',
                'required': False,
                'next': [
                    {
                        'match': self.UNARY,
                        'required': True,
                        'error': 'UNARY faltante'
                    },
                    {
                        'match': self.FACTOR_2,
                        'required': True,
                        'error': 'FACTOR_2 faltante'
                    },
                ]
            },
            {
                'match': '*',
                'required': False,
                'next': [
                    {
                        'match': self.UNARY,
                        'required': True,
                        'error': 'UNARY faltante'
                    },
                    {
                        'match': self.FACTOR_2,
                        'required': True,
                        'error': 'FACTOR_2 faltante'
                    },
                ]
            },
        ]
    """

    def FACTOR_2(self):
        result = []
        if (self.findToken('/')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.UNARY)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('UNARY faltante')
            if (self.findToken(self.FACTOR_2)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FACTOR_2 faltante')
        if (self.findToken('*')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.UNARY)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('UNARY faltante')
            if (self.findToken(self.FACTOR_2)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('FACTOR_2 faltante')
        return result

    """
    def UNARY(self):
        print("UNARY")
        return [
            {
                'match': '!',
                'required': False,
                'next': [
                    {
                        'match': self.UNARY,
                        'required': True,
                        'error': 'UNARY faltante'
                    }
                ]
            }, {
                'match': '-',
                'required': False,
                'next': [
                    {
                        'match': self.UNARY,
                        'required': True,
                        'error': 'UNARY faltante'
                    }
                ]
            }, {
                'match': self.CALL,
                'required': False,
                'error': 'CALL faltante'
            },
        ]
    """

    def UNARY(self):
        result = []
        if (self.findToken('!')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.UNARY)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('UNARY faltante')
        elif (self.findToken('-')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.UNARY)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('UNARY faltante')
        elif (self.findToken(self.CALL)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def CALL(self):
        print("CALL")
        return [
            {
                'match': self.PRIMARY,
                'required': False,
                'error': 'PRIMARY faltante'
            },
            {
                'match': self.CALL_2,
                'required': False,
                'error': 'CALL_2 faltante'
            },
        ]
    """

    def CALL(self):
        result = []
        if (self.findToken(self.PRIMARY)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(self.CALL_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def CALL_2(self):
        print("CALL_2")
        return [
            {
                'match': '(',
                'required': False,
                'next': [
                    {
                        'match': self.ARGUMENTS_OPC,
                        'required': True,
                        'error': 'ARGUMENTS_OPC faltante'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': ') faltante'
                    },
                    {
                        'match': self.CALL_2,
                        'required': True,
                        'error': 'CALL_2 faltante'
                    },
                ]
            }, {
                'match': '.',
                'required': False,
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'id faltante'
                    }, {
                        'match': self.CALL_2,
                        'required': True,
                        'error': 'CALL_2 faltante'
                    },
                ]
            }
        ]
    """

    def CALL_2(self):
        result = []
        if (self.findToken('(')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.ARGUMENTS_OPC)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('ARGUMENTS_OPC faltante')
            if (self.findToken(')')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception(') faltante')
            if (self.findToken(self.CALL_2)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('CALL_2 faltante')
        elif (self.findToken('.')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(Identificador)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('id faltante')
            if (self.findToken(self.CALL_2)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('CALL_2 faltante')
        return result

    """
    def PRIMARY(self):
        print("PRIMARY")
        return [
            {
                'match': 'true',
                'required': False,
            },
            {
                'match': 'false',
                'required': False,
            },
            {
                'match': 'null',
                'required': False,
            },
            {
                'match': 'this',
                'required': False,
            },
            {
                'match': Numero,
                'required': False,
            },
            {
                'match': Cadena,
                'required': False,
            },
            {
                'match': Identificador,
                'required': False,
            },
            {
                'match': '(',
                'required': False,
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'EXPRESSION faltante 9'
                    },
                    {
                        'match': ')',
                        'required': True,
                        'error': ') faltante'
                    },
                ]
            },
            {
                'match': 'super',
                'required': False,
                'next': [
                    {
                        'match': '.',
                        'required': True,
                        'error': '. faltante'
                    },
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'id faltante'
                    },
                ]
            },
        ]
    """

    def PRIMARY(self):
        result = []
        if (self.findToken('true')):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken('false')):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken('null')):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken('this')):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(Numero)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(Cadena)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken(Identificador)):
            result.append(self.tokens[0])
            del self.tokens[0]
        elif (self.findToken('(')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.EXPRESSION)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('EXPRESSION faltante 9')
            if (self.findToken(')')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception(') faltante')
        elif (self.findToken('super')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken('.')):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('. faltante')
            if (self.findToken(Identificador)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('id faltante')
        return result
    # OTRAS
    """
    def FUNCTION(self):
        print("FUNCTION")
        return [
            {
                'match': Identificador,
                'required': True,
                'error': 'id faltante'
            },
            {
                'match': '(',
                'required': True,
                'error': '( faltante'
            },
            {
                'match': self.PARAMETER_OPC,
                'required': True,
                'error': 'PARAMETER_OPC faltante'
            },
            {
                'match': ')',
                'required': True,
                'error': ') faltante'
            },
            {
                'match': self.BLOCK,
                'required': True,
                'error': 'BLOCK faltante'
            },
        ]
    """

    def FUNCTION(self):
        result = []
        if (self.findToken(Identificador)):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('id faltante')
        if (self.findToken('(')):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('( faltante')
        if (self.findToken(self.PARAMETER_OPC)):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('PARAMETER_OPC faltante')
        if (self.findToken(')')):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception(') faltante')
        if (self.findToken(self.BLOCK)):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('BLOCK faltante')
        return result
    """
    def FUNCTIONS(self):
        print("FUNCTIONS")
        return [
            {
                'match': self.FUNCTION,
                'required': True,
                'looping': True
            }
        ]
    """

    def FUNCTIONS(self):
        result = []
        while (self.findToken(self.FUNCTION)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def PARAMETER_OPC(self):
        print("PARAMETER_OPC")
        return [
            {
                'match': self.PARAMETERS,
                'required': False,
            },
        ]
    """

    def PARAMETER_OPC(self):
        result = []
        if (self.findToken(self.PARAMETERS)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def PARAMETERS(self):
        print("PARAMETERS")
        return [
            {
                'match': Identificador,
                'required': True,
                'error': 'id faltante'
            },
            {
                'match': self.PARAMETERS_2,
                'required': True,
                'error': 'PARAMETERS_2 faltante'
            },
        ]
    """

    def PARAMETERS(self):
        result = []
        if (self.findToken(Identificador)):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('id faltante')
        if (self.findToken(self.PARAMETERS_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('PARAMETERS_2 faltante')
        return result

    """
    def PARAMETERS_2(self):
        print("PARAMETERS_2")
        return [
            {
                'match': ',',
                'required': False,
                'looping': True,
                'next': [
                    {
                        'match': Identificador,
                        'required': True,
                        'error': 'id faltante'
                    }
                ]
            },
        ]
    """

    def PARAMETERS_2(self):
        result = []
        while (self.findToken(',')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(Identificador)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('id faltante')
        return result

    """
    def ARGUMENTS_OPC(self):
        print("ARGUMENTS_OPC")
        return [
            {
                'match': self.ARGUMENTS,
                'required': False,
            },
        ]
    """

    def ARGUMENTS_OPC(self):
        result = []
        if (self.findToken(self.ARGUMENTS)):
            result.append(self.tokens[0])
            del self.tokens[0]
        return result

    """
    def ARGUMENTS(self):
        print("ARGUMENTS")
        return [
            {
                'match': self.EXPRESSION,
                'required': True,
                'error': 'EXPRESSION faltante 10'
            },
            {
                'match': self.ARGUMENTS_2,
                'required': True,
                'error': 'ARGUMENTS_2 faltante'
            },
        ]
    """

    def ARGUMENTS(self):
        result = []
        if (self.findToken(self.EXPRESSION)):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('EXPRESSION faltante 10')
        if (self.findToken(self.ARGUMENTS_2)):
            result.append(self.tokens[0])
            del self.tokens[0]
        else:
            raise Exception('ARGUMENTS_2 faltante')
        return result
    
"""
    def ARGUMENTS_2(self):
        print("ARGUMENTS_2")
        return [
            {
                'match': ',',
                'required': False,
                'looping': True,
                'next': [
                    {
                        'match': self.EXPRESSION,
                        'required': True,
                        'error': 'EXPRESSION faltante 11'
                    }
                ]
            },
        ]
"""

def ARGUMENTS_2(self):
        result = []
        while (self.findToken(',')):
            result.append(self.tokens[0])
            del self.tokens[0]
            if (self.findToken(self.EXPRESSION)):
                result.append(self.tokens[0])
                del self.tokens[0]
            else:
                raise Exception('EXPRESSION faltante 11')
        return result
