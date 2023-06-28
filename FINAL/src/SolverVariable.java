//package mx.ipn.escom.compiladores;

/**
 * SolverVariable
 */
public class SolverVariable {

    private final Nodo nodo;
    public final TablaSimbolos tabla;

    public SolverVariable(Nodo nodo, TablaSimbolos tabla) {
        this.nodo = nodo;
        this.tabla = tabla;
    }

    public Object resolver() {
        return resolver(nodo);
    }

    private Object resolver(Nodo n) {
        // No tiene hijos, es un error
        if (n.getHijos() == null) {
            // Error, identificador faltante
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