import values_xwyalpha as values
import y_predictiva as yp
# y_hat = [7.0, 10.0, 13.0] 

# 1. Definimos la lambda para el Error Cuadrático Individual
# Recibe una tupla (pareja) de valores: (real, prediccion)
calc_error_cuadrado = lambda pareja: (pareja[0] - pareja[1]) ** 2

# 2. Emparejamos los datos reales con los predichos
datos_emparejados = zip(values.y, yp.y_hat)

# 3. Aplicamos la resta y el cuadrado a cada pareja
lista_errores = map(calc_error_cuadrado, datos_emparejados)

# 4. Calculamos el promedio (Suma total / Cantidad de elementos)
# Nota: 'list(values.y)' es para asegurar que tenemos el largo correcto
costo = sum(lista_errores) / len(values.y)

#print("La Función de Pérdida (MSE) es:", costo)
# Resultado esperado: 74.666...