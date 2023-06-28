package mx.ipn.escom.compiladores;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Scanner {
    private final String source;

    private final List<Token> tokens = new ArrayList<>();

    private static final Map<String, TipoToken> palabrasReservadas;
    static {
        palabrasReservadas = new HashMap<>();
        palabrasReservadas.put("if", TipoToken.IF);
        palabrasReservadas.put("var", TipoToken.VAR);
        palabrasReservadas.put("print", TipoToken.PRINT);
        palabrasReservadas.put("else", TipoToken.ELSE);
        palabrasReservadas.put("and", TipoToken.AND);
        palabrasReservadas.put("or", TipoToken.OR);
        palabrasReservadas.put("true", TipoToken.TRUE);
        palabrasReservadas.put("false", TipoToken.FALSE);
    }

    Scanner(String source) {
        this.source = source + " ";
    }

    List<Token> scanTokens() {
        int estado = 0;
        char caracter = 0;
        String lexema = "";

        for (int i = 0; i < source.length(); i++) {
            caracter = source.charAt(i);

            switch (estado) {
                case 0:
                    if (caracter == '*') {
                        tokens.add(new Token(TipoToken.MULTIPLICACION, "*"));
                    } else if (caracter == '+') {
                        tokens.add(new Token(TipoToken.SUMA, "+"));
                    } else if (caracter == '-') {
                        tokens.add(new Token(TipoToken.RESTA, "-"));
                    } else if (caracter == '/') {
                        estado = 10;
                    } else if (caracter == '(') {
                        tokens.add(new Token(TipoToken.LPAREN, "("));
                    } else if (caracter == ')') {
                        tokens.add(new Token(TipoToken.RPAREN, ")"));
                    } else if (caracter == '=') {
                        estado = 15;
                    } else if (caracter == '{') {
                        tokens.add(new Token(TipoToken.LBRACE, "{"));
                    } else if (caracter == '}') {
                        tokens.add(new Token(TipoToken.RBRACE, "}"));
                    } else if (caracter == ';') {
                        tokens.add(new Token(TipoToken.SEMICOLON, ";"));
                    } else if (caracter == '"') {
                        estado = 9;
                    } else if (Character.isAlphabetic(caracter)) {
                        estado = 1;
                        lexema = lexema + caracter;
                    } else if (Character.isDigit(caracter)) {
                        estado = 2;
                        lexema = lexema + caracter;
                    } else if (caracter == '>') {
                        estado = 8;
                    } else if (caracter == '<') {
                        estado = 14;
                    }
                    break;

                case 1:
                    if (Character.isAlphabetic(caracter) || Character.isDigit(caracter)) {
                        lexema = lexema + caracter;
                    } else {
                        TipoToken tt = palabrasReservadas.get(lexema);
                        if (tt == null) {
                            tokens.add(new Token(TipoToken.IDENTIFICADOR, lexema));
                        } else {
                            tokens.add(new Token(tt, lexema));
                        }

                        estado = 0;
                        i--;
                        lexema = "";
                    }
                    break;
                case 2:
                    if (Character.isDigit(caracter)) {
                        estado = 2;
                        lexema = lexema + caracter;
                    } else if (caracter == '.') {
                        estado = 3;
                        lexema = lexema + caracter;
                    } else if (caracter == 'E') {
                        estado = 5;
                        lexema = lexema + caracter;
                    } else {
                        tokens.add(new Token(TipoToken.NUMERO, lexema, Double.valueOf(lexema)));
                        estado = 0;
                        lexema = "";
                        i--;
                    }
                    break;
                case 3:
                    if (Character.isDigit(caracter)) {
                        estado = 4;
                        lexema = lexema + caracter;
                    } else {
                        // Lanzar error
                    }
                    break;
                case 4:
                    if (Character.isDigit(caracter)) {
                        estado = 4;
                        lexema = lexema + caracter;
                    } else if (caracter == 'E') {
                        estado = 5;
                        lexema = lexema + caracter;
                    } else {
                        tokens.add(new Token(TipoToken.NUMERO, lexema, Double.valueOf(lexema)));
                        estado = 0;
                        lexema = "";
                        i--;
                    }
                    break;
                case 5:
                    if (caracter == '+' || caracter == '-') {
                        estado = 6;
                        lexema = lexema + caracter;
                    } else if (Character.isDigit(caracter)) {
                        estado = 7;
                        lexema = lexema + caracter;
                    } else {
                        // Lanzar error
                    }
                    break;
                case 6:
                    if (Character.isDigit(caracter)) {
                        estado = 7;
                        lexema = lexema + caracter;
                    } else {
                        // Lanzar error
                    }
                    break;
                case 7:
                    if (Character.isDigit(caracter)) {
                        estado = 7;
                        lexema = lexema + caracter;
                    } else {
                        tokens.add(new Token(TipoToken.NUMERO, lexema, Double.valueOf(lexema)));
                        estado = 0;
                        lexema = "";
                        i--;
                    }
                    break;
                case 8:
                    if (caracter == '=') {
                        tokens.add(new Token(TipoToken.MAYOR_IGUAL, ">=", null));
                    } else {
                        tokens.add(new Token(TipoToken.MAYOR, ">", null));
                        i--;
                    }
                    estado = 0;
                    break;
                case 9:
                    if (caracter == '"') {
                        tokens.add(new Token(TipoToken.CADENA, lexema, null));
                        lexema = "";
                        estado = 0;
                    } else {
                        lexema = lexema + caracter;
                    }
                    break;
                case 10:
                    if (caracter == '/') {
                        estado = 11;
                    } else if (caracter == '*') {
                        estado = 12;
                    } else {
                        tokens.add(new Token(TipoToken.DIVISION, "/"));
                        estado = 0;
                        i--;
                    }
                    break;
                case 11:
                    if (caracter == '\n') {
                        estado = 0;
                    }
                    break;
                case 12:
                    if (caracter == '*') {
                        estado = 13;
                    }
                    break;
                case 13:
                    if (caracter == '/') {
                        estado = 0;
                    } else {
                        estado = 12;
                    }
                    break;
                case 14:
                    if (caracter == '=') {
                        tokens.add(new Token(TipoToken.MENOR_IGUAL, "<=", null));
                    } else {
                        tokens.add(new Token(TipoToken.MENOR, "<", null));
                        i--;
                    }
                    estado = 0;
                    break;
                case 15:
                    if (caracter == '=') {
                        tokens.add(new Token(TipoToken.IGUAL_A, "=="));
                    } else {
                        tokens.add(new Token(TipoToken.IGUAL, "="));
                        i--;
                    }
                    estado = 0;
                    break;
            }
        }
        tokens.add(new Token(TipoToken.EOF, ""));

        return tokens;
    }

}
