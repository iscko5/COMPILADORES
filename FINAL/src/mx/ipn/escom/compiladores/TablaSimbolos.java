package mx.ipn.escom.compiladores;

import java.util.HashMap;
import java.util.Map;

public class TablaSimbolos {

    private final Map<String, Object> values = new HashMap<>();
    private final Map<String, TipoToken> types = new HashMap<>();

    public boolean existeIdentificador(String identificador) {
        return values.containsKey(identificador);
    }

    public Object obtenerValue(String identificador) {
        if (values.containsKey(identificador)) {
            return values.get(identificador);
        }
        throw new RuntimeException("Variable no definida '" + identificador + "'.");
    }

    public TipoToken obtenerType(String identificador) {
        if (types.containsKey(identificador)) {
            return types.get(identificador);
        }
        throw new RuntimeException("Variable no definida '" + identificador + "'.");
    }

    public void asignar(String identificador) {
        types.put(identificador, null);
        values.put(identificador, null);
    }

    public void asignar(String identificador, TipoToken tipo, Object valor) {
        types.put(identificador, tipo);
        values.put(identificador, valor);
    }
}