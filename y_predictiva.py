import values_xwyalpha as values

# 1. Definimos la "Receta" (Lambda)
# Esta función anónima recibe una fila (un pokémon), junta sus datos con los pesos
# y calcula la suma total.
calcular_prediccion = lambda fila: sum(dato * peso for dato, peso in zip(fila, values.w))

# 2. Aplicamos la receta a todos los datos (Map)
# map(funcion, lista) aplica la lambda a cada elemento de values.X
y_hat = list(map(calcular_prediccion, values.x))

#print("y_hat =", y_hat)
# Resultado esperado: [7.0, 10.0, 13.0]