package mx.ipn.escom.compiladores;

public class Solver {
	public final TablaSimbolos tabla;
	public Boolean error = false;
	public String errorMessage = "";

	public Solver(TablaSimbolos tabla) {
		this.tabla = tabla;
	}

	public Object resolverAritmetico(Nodo n) {
		// No tiene hijos, es un operando
		if (n.getHijos() == null) {
			if (n.getValue().tipo == TipoToken.CADENA) {
				return n.getValue().lexema;
			} else if (n.getValue().tipo == TipoToken.NUMERO) {
				return Double.valueOf(n.getValue().lexema);
			} else if (n.getValue().tipo == TipoToken.TRUE || n.getValue().tipo == TipoToken.FALSE) {
				return resolverBooleano(n);
			} else if (n.getValue().tipo == TipoToken.IDENTIFICADOR) {
				// Checar que esté en la tabla de símbolos
				validateVariable(n, this.tabla);
				if (this.error)
					return null;
				Tuple<TipoToken, Object> res = this.tabla.obtener((String) n.getValue().lexema);

				if (res.x == TipoToken.NUMERO) {
					return res.y;
				} else if (res.x == TipoToken.CADENA) {
					return String.valueOf(res.y);
				} else if (res.x == TipoToken.TRUE || res.x == TipoToken.FALSE) {
					return res.x == TipoToken.TRUE;
				} else {
					this.errorMessage = ("Valor inválido de identificador");
					this.error = true;
					return null;
				}
			} else {
				this.errorMessage = ("Valor inválido");
				this.error = true;
				return null;
			}
		} else if (n.getHijos().size() > 2) {
			this.errorMessage = ("Operador inválido");
			this.error = true;
			return null;
		}

		// Por simplicidad se asume que la lista de hijos del nodo tiene dos elementos
		Nodo izq = n.getHijos().get(0);
		Nodo der = n.getHijos().get(1);

		Object resultadoIzquierdo = resolverAritmetico(izq);
		if (this.error)
			return null;
		Object resultadoDerecho = resolverAritmetico(der);
		if (this.error)
			return null;

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
				case MAYOR:
					return ((Double) resultadoIzquierdo > (Double) resultadoDerecho);
				case MAYOR_IGUAL:
					return ((Double) resultadoIzquierdo >= (Double) resultadoDerecho);
				case MENOR:
					return ((Double) resultadoIzquierdo < (Double) resultadoDerecho);
				case MENOR_IGUAL:
					return ((Double) resultadoIzquierdo <= (Double) resultadoDerecho);
				case IGUAL_A:
					return ((Double) resultadoIzquierdo == (Double) resultadoDerecho);
				default:
					this.errorMessage = ("Operador inválido");
					this.error = true;
					return null;
			}
		} else if (resultadoIzquierdo instanceof String && resultadoDerecho instanceof String) {
			switch (n.getValue().tipo) {
				case SUMA:
					return ((String) resultadoIzquierdo).concat((String) resultadoDerecho);
				case IGUAL_A:
					return (((String) resultadoIzquierdo).equals((String) resultadoDerecho));
				default:
					this.errorMessage = ("Operador inválido");
					this.error = true;
					return null;
			}
		} else if (resultadoIzquierdo instanceof Boolean && resultadoDerecho instanceof Boolean) {
			switch (n.getValue().tipo) {
				case IGUAL_A:
					return ((Boolean) resultadoIzquierdo == (Boolean) resultadoDerecho);
				case AND:
					return ((Boolean) resultadoIzquierdo && (Boolean) resultadoDerecho);
				case OR:
				default:
					this.errorMessage = ("Operador inválido");
					this.error = true;
					return null;
			}
		} else {
			// Error por diferencia de tipos
			this.errorMessage = ("Diferencia de tipos");
			this.error = true;
			return null;
		}
	}

	public Boolean resolverBooleano(Nodo n) {
		if (n.getHijos() != null) {
			this.errorMessage = ("Valor inválido boo");
			this.error = true;
			return null;
		}

		switch (n.getValue().tipo) {
			case TRUE:
				return true;
			case FALSE:
				return false;
			case IDENTIFICADOR:
				validateVariable(n, tabla);
				if (this.error)
					return null;

				Object valor = this.tabla.obtener((String) n.getValue().lexema);
				if (valor.getClass() != Boolean.class) {
					this.errorMessage = ("Booleano inválido");
					this.error = true;
					return null;
				} else {
					return (Boolean) valor;
				}
			default:
				this.errorMessage = ("Booleano inválido");
				this.error = true;
				return null;
		}
	}

	public Object resolverIf(Nodo n) {
		if (n.getHijos() == null) {
			this.errorMessage = ("Condición faltante");
			this.error = true;
			return null;
		}

		// evaluando la condicion
		Object condicion = resolverAritmetico(n.getHijos().get(0));
		if (this.error)
			return null;
		// verificando que la condicion sea booleana
		if (!(condicion instanceof Boolean)) {
			this.errorMessage = ("Booleano inválido");
			this.error = true;
			return null;
		}
		n.getHijos().remove(0);

		// Checar si el ultimo nodo es un else
		if (n.getHijos().get(n.getHijos().size() - 1).getValue().tipo == TipoToken.ELSE) {
			n.getHijos().remove(n.getHijos().size() - 1);
		}

		if ((Boolean) condicion) {
			// Correr lo de adentro del if
			Arbol arbol = new Arbol(n);
			arbol.recorrer();
		} else if (n.getHijos().get(n.getHijos().size() - 1).getValue().tipo == TipoToken.ELSE) {
			Arbol arbol = new Arbol(n.getHijos().get(n.getHijos().size() - 1));
			arbol.recorrer();
		}

		return condicion;
	}

	public Object resolverPrint(Nodo n) {
		if (n.getHijos() == null) {
			this.errorMessage = ("Faltan argumentos");
			this.error = true;
			return null;
		}
		if (n.getHijos().size() > 1) {
			this.errorMessage = ("Valores de print de más");
			this.error = true;
			return null;
		}

		Object imprimir = resolverAritmetico(n.getHijos().get(0));
		if (this.error)
			return null;

		System.out.println(imprimir);
		return null;
	}

	public Object resolverVariable(Nodo n) {
		if (n.getHijos() == null) {
			this.errorMessage = ("Identificador faltante");
			this.error = true;
			return null;
		} else if (n.getHijos().size() > 2) {
			this.errorMessage = ("Valores de más");
			this.error = true;
			return null;
		}

		if (n.getValue().tipo == TipoToken.VAR) {
			// Intentar inicializar variable
			invalidateVariable(n.getHijos().get(0), tabla);
			if (this.error) {
				return null;
			}
			// Agregar hijo 1 como identificador
			this.tabla.asignar(n.getHijos().get(0).getValue().lexema);
		} else if (n.getValue().tipo == TipoToken.SET) {
			// Checar que variable exista
			validateVariable(n.getHijos().get(0), tabla);
			if (this.error)
				return null;
		}

		if (n.getHijos().size() == 2) {
			// Agregar solución de hijo 2 como valor de identificador
			Object res = resolverAritmetico(n.getHijos().get(1));
			if (this.error)
				return null;
			TipoToken tipo = null;

			if (res instanceof Double) {
				tipo = TipoToken.NUMERO;
			} else if (res instanceof String) {
				tipo = TipoToken.CADENA;
			} else if (res instanceof Boolean) {
				tipo = (Boolean) res ? TipoToken.TRUE : TipoToken.FALSE;
			} else {
				this.errorMessage = ("Valor de asignación inválido");
				this.error = true;
				return null;
			}

			this.tabla.asignar(n.getHijos().get(0).getValue().lexema, tipo, res);
			return res;
		}
		return null;
	}

	// Control de variable
	public Boolean validateVariable(Nodo n, TablaSimbolos tabla) {
		if (!tabla.existeIdentificador(n.getValue().lexema)) {
			this.errorMessage = ("Variable no inicializada");
			this.error = true;
			return null;
		} else {
			return true;
		}
	}

	public Boolean invalidateVariable(Nodo n, TablaSimbolos tabla) {
		if (tabla.existeIdentificador(n.getValue().lexema)) {
			this.errorMessage = ("Variable ya existe");
			this.error = true;
			return null;
		} else {
			return true;
		}
	}

}