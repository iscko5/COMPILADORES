//package mx.ipn.escom.compiladores;

public class SolverAritmetico {

    private final Nodo nodo;
    public final TablaSimbolos tabla;

    public SolverAritmetico(Nodo nodo, TablaSimbolos tabla) {
        this.nodo = nodo;
        this.tabla = tabla;
    }

    public Object resolver() {
        return resolver(nodo);
    }

    private Object resolver(Nodo n) {
        // No tiene hijos, es un operando
        if (n.getHijos() == null) {
            if (n.getValue().tipo == TipoToken.NUMERO || n.getValue().tipo == TipoToken.CADENA) {
                return n.getValue().literal;
            } else if (n.getValue().tipo == TipoToken.IDENTIFICADOR) {
                // Ver la tabla de símbolos
                if (!this.tabla.existeIdentificador(n.getValue().literal.toString())) {
                    // Error por identificador no inicializado
                }
            }
        }

        // Por simplicidad se asume que la lista de hijos del nodo tiene dos elementos
        Nodo izq = n.getHijos().get(0);
        Nodo der = n.getHijos().get(1);

        Object resultadoIzquierdo = resolver(izq);
        Object resultadoDerecho = resolver(der);

        if (resultadoIzquierdo instanceof Double && resultadoDerecho instanceof Double) {
            switch (n.getValue().tipo) {
                case SUMA:
                    return ((Double) resultadoIzquierdo + (Double) resultadoDerecho);
                case RESTA:
                    return ((Double) resultadoIzquierdo - (Double) resultadoDerecho);
                case MULTIPLICACION:
                    return ((Double) resultadoIzquierdo * (Double) resultadoDerecho);
                case DIVISION:
                    return ((Double) resultadoIzquierdo / (Double) resultadoDerecho);
            }
        } else if (resultadoIzquierdo instanceof String && resultadoDerecho instanceof String) {
            if (n.getValue().tipo == TipoToken.SUMA) {
                // Ejecutar la concatenación
            }
        } else {
            // Error por diferencia de tipos
        }

        return null;
    }
}
