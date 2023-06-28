package mx.ipn.escom.compiladores;

public class Arbol {
    private final Nodo raiz;
    public TablaSimbolos tabla;
    public Boolean error;
    public String errorMessage;

    public Arbol(Nodo raiz) {
        this.raiz = raiz;
    }

    public void recorrer() {
        Solver solver = new Solver(this.tabla);
        for (int i = 0; i < raiz.getHijos().size(); ++i) {
            Nodo n = raiz.getHijos().get(i);
            Token t = n.getValue();

            switch (t.tipo) {
                // Operadores aritméticos
                case SUMA:
                case RESTA:
                case MULTIPLICACION:
                case DIVISION:
                    solver.resolverAritmetico(n);
                    break;
                case VAR:
                case SET:
                    solver.resolverVariable(n);
                    break;
                case IF:
                    solver.resolverIf(n);
                    break;
                case PRINT:
                    solver.resolverPrint(n);
                    break;
                default:
                    i = raiz.getHijos().size() + 1;
            }

            if (solver.error) {
                i = raiz.getHijos().size() + 1;
            }
        }
        this.error = solver.error;
        this.errorMessage = solver.errorMessage;
        this.tabla = solver.tabla;
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
