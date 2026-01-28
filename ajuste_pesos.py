import values_xwyalpha as val
import ajuste_transpuesta as ajt
for j in range(2):
    val.w[j] = val.w[j] + val.alpha * ajt.grad[j]

#print("nuevos pesos w =", val.w)
