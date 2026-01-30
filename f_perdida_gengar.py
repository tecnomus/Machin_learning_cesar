import gengar_stats as gs
import y_predictiva as ypg
# y = [50, 100, 40] 

# 1. Definimos la lambda para el Error Cuadrático Individual
# Recibe una tupla (pareja) de valores: (real, prediccion)
calc_error_cuadrado = lambda pareja: (pareja[0] - pareja[1]) ** 2

# 2. Emparejamos los datos reales con los predichos
datos_emparejados = zip(gs.y, ypg.y_hat)

# 3. Aplicamos la resta y el cuadrado a cada pareja
lista_errores = map(calc_error_cuadrado, datos_emparejados)

# 4. Calculamos el promedio (Suma total / Cantidad de elementos)
# Nota: 'list(values.y)' es para asegurar que tenemos el largo correcto
perdida = sum(lista_errores) / len(gs.y)

#print("La Función de Pérdida (MSE) es:", perdida)
# Resultado esperado: 3559.3333333333335...