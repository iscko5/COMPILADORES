## COMPILADORES

El repositorio aquí muestra el proyecto del Compiladores.

Si se hace copia, modifique la identación de las líneas de código.

## Identación

Modifique este tipo de líneas:

```python
  tokens.append({'index': search.start(),
                          "value": Comentario(search.group(0))})
```

Por algo así:

```python
  tokens.append({'index': search.start(), "value": Comentario(search.group(0))})
```
