import errorvector as er
import values_xwyalpha as val
grad = [0, 0]

for j in range(2):          # columnas
    suma = 0
    for i in range(3):      # filas
        suma = suma + val.x[i][j] * er.e[i]
    grad[j] = suma

#print("X^T e =", grad)
