//package mx.ipn.escom.compiladores;

import java.util.ArrayList;
import java.util.List;

public class Arbol {
    private final Nodo raiz;
    public TablaSimbolos tabla;

    public Arbol(Nodo raiz) {
        this.raiz = raiz;
    }

    public void recorrer() {
        for (Nodo n : raiz.getHijos()) {
            Token t = n.getValue();
            switch (t.tipo) {
                // Operadores aritméticos
                case SUMA:
                case RESTA:
                case MULTIPLICACION:
                case DIVISION:
                    SolverAritmetico solver = new SolverAritmetico(n, this.tabla);
                    Object res = solver.resolver();
                    this.tabla = solver.tabla;
                    System.out.println(res);
                    break;

                case VAR:
                    // Crear una variable. Usar tabla de simbolos
                    // SolverVariable solver = new SolverVariable(n);
                    // Object res = solver.resolver();
                    // System.out.println(res);
                    break;
                case IF:
                    break;

            }
        }
    }

    @Override
    public String toString() {
        String res = "";
        for (Nodo n : raiz.getHijos()) {
            res += n.toString();
        }
        return res;
    }

}
