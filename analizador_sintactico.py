import sys
INT, FLOAT, ID, COMMA, OPERATOR, EOI, INVALID, KEYWORD, QUERY, IDLIST, CONDLIST, COND, TERM = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13


def typeToString(tp):
    if (tp == INT):
        return "Int"
    elif (tp == FLOAT):
        return "Float"
    elif (tp == ID):
        return "ID"
    elif (tp == COMMA):
        return "Comma"
    elif (tp == OPERATOR):
        return "Operator"
    elif (tp == EOI):
        return "EOI"
    elif (tp == KEYWORD):
        return "Keyword"
    elif (tp == QUERY):
        return "Query"
    elif (tp == IDLIST):
        return "IdList"
    elif (tp == CONDLIST):
        return "CondList"
    elif (tp == COND):
        return "Cond"
    elif (tp == TERM):
        return "Term"
    return "Invalid"


class Token:
    #"A class for representing Tokens"
    # a Token object has two fields: the token's type and its value
    def _init_(self, tokenType, tokenVal):
        self.type = tokenType
        self.val = tokenVal

    def getTokenType(self):
        return self.type

    def getTokenValue(self):
        return self.val

    def _repr_(self):
        if (self.type in [INT, FLOAT, ID, KEYWORD, QUERY, IDLIST, CONDLIST, COND, TERM]):
            return self.val
        elif (self.type == COMMA):
            return ","
        elif (self.type == OPERATOR):
            if (self.val == "="):
                return "="
            if (self.val == ">"):
                return ">"
            if (self.val == "<"):
                return "<"
        elif (self.type == EOI):
            return ""
        else:
            return "invalid"

 # ------------------------------------ LEXER --------------------------------------


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"


class Lexer:

    # stmt is the current statement to perform the lexing;
    # index is the index of the next char in the statement
    def _init_(self, s):
        self.stmt = s
        self.index = 0
        self.nextChar()

    def nextToken(self):
        while True:
            if self.ch.isalpha():  # is a letter
                id = self.consumeChars(LETTERS+DIGITS)
                if id == "SELECT" or id == "FROM" or id == "WHERE" or id == "AND":
                    return Token(KEYWORD, id)
                else:
                    return Token(ID, id)
            elif self.ch.isdigit():
                num = self.consumeChars(DIGITS)
                if self.ch != ".":
                    return Token(INT, num)
                num += self.ch
                self.nextChar()
                if self.ch.isdigit():
                    num += self.consumeChars(DIGITS)
                    return Token(FLOAT, num)
                else:
                    return Token(INVALID, num)
            elif self.ch == ' ':
                self.nextChar()
            elif self.ch == ',':
                self.nextChar()
                return Token(COMMA, "")
            elif self.ch == '=':
                self.nextChar()
                return Token(OPERATOR, "=")
            elif self.ch == '>':
                self.nextChar()
                return Token(OPERATOR, ">")
            elif self.ch == '<':
                self.nextChar()
                return Token(OPERATOR, "<")
            elif self.ch == '$':
                return Token(EOI, "")
            else:
                self.nextChar()
                return Token(INVALID, self.ch)

    def nextChar(self):
        self.ch = self.stmt[self.index]
        self.index = self.index + 1

    def consumeChars(self, charSet):
        r = self.ch
        self.nextChar()
        while (self.ch in charSet):
            r = r + self.ch
            self.nextChar()
        return r

    def checkChar(self, c):
        self.nextChar()
        if (self.ch == c):
            self.nextChar()
            return True
        else:
            return False
 # ------------------------------------ PARSER --------------------------------------


class Parser:
    def _init_(self, s):
        self.lexer = Lexer(s+"$")
        self.token = self.lexer.nextToken()

    def run(self):
        self.query()

    def next(self):
        self.token = self.lexer.nextToken()

    def query(self):
        print("Query")

        if (self.token.getTokenType() == KEYWORD) and (self.token.getTokenValue() == "SELECT"):
            print("\t<Keyword>" + self.token.getTokenValue() + "</Keyword>")
            self.next()
            self.idList()
        else:
            self.error(KEYWORD)

        if (self.token.getTokenType() == KEYWORD) and (self.token.getTokenValue() == "FROM"):
            print("\t<Keyword>" + self.token.getTokenValue() + "</Keyword>")
            self.next()
            self.idList()
        else:
            self.error(KEYWORD)

        if (self.token.getTokenType() == KEYWORD) and (self.token.getTokenValue() == "WHERE"):
            print("\t<Keyword>" + self.token.getTokenValue() + "</Keyword>")
            self.next()
            self.condList()

        if self.token.getTokenType() == EOI:
            print("</Query>")

        if self.token.getTokenType() == INVALID:
            self.error(self.token.getTokenType())
            self.next()

    def idList(self):
        print("\t<IdList>")
        if self.token.getTokenType() == ID:
            print("\t\t<Id>" + self.token.getTokenValue() + "</Id>")
            self.next()
        while self.token.getTokenType() == COMMA:
            print("\t\t<Comma>" + "," + "</Comma>")
            self.next()
            if self.token.getTokenType() == ID:
                print("\t\t<Id>" + self.token.getTokenValue() + "</Id>")
                self.next()
            else:
                self.error(ID)
        print("\t</IdList>")

    def condList(self):
        print("\t<CondList>")
        if self.token.getTokenType() == ID:
            self.cond()
        else:
            self.error(self.token.getTokenType())

        while ((self.token.getTokenType() == KEYWORD) and (self.token.getTokenValue() == "AND")):
            print "\t<Keyword>" + self.token.getTokenValue() + "</Keyword>"
            self.next()
            if self.token.getTokenType() == ID:
                self.cond()
            else:
                self.error(CONDLIST)
        print "\t</CondList>"

    def cond(self):
        print "\t\t<Cond>"
        print "\t\t\t<Id>" + self.token.getTokenValue() + "</Id>"
        self.next()
        if self.token.getTokenType() == OPERATOR:
            print "\t\t\t<Operator>" + self.token.getTokenValue() + "</Operator>"
            self.next()
            self.term()
        else:
            self.error(COND)
        print "\t\t</Cond>"

    def term(self):
        print "\t\t\t<Term>"
        if self.token.getTokenType() == ID:
            print "\t\t\t<Id>" + self.token.getTokenValue() + "</Id>"
            self.next()

        elif self.token.getTokenType() == INT:
            print "\t\t\t<Int>" + self.token.getTokenValue() + "</Int>"
            self.next()

        elif self.token.getTokenType() == FLOAT:
            print "\t\t\t\t<Float>" + self.token.getTokenValue() + "</Float>"
            self.next()

        else:
            self.error(TERM)
        print "\t\t\t</Term>"

    def error(self, tp):
        print "Syntax error: expecting: " + typeToString(tp) \ + "; saw: " + typeToString(self.token.getTokenType())
        sys.exit(1)

 # ------------------------------------ MAIN ----------------------------------------


 # -------- Test 1 -----------
parser = Parser("SELECT C1,C2 FROM T1 WHERE C1=5.23")
parser.run()
# -------- Test 2 -----------
# parser = Parser ("SELECT C1,C2 FROM T1 WHERE C1<5.23 AND C2 = 5")
# parser.run()
# -------- Test 3 -----------
# parser = Parser (" ")
# parser.run()
