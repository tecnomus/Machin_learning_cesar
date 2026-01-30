import gengar_stats as val
import ajuste_transpuesta_gengar as ajtg
for j in range(2):
    val.w[j] = val.w[j] + val.alpha * ajtg.grad[j]

#print("nuevos pesos w =", val.w)
