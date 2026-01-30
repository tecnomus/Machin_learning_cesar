import nueva_prediccion_gengar as npg
import gengar_stats as gs
e2 = []

for i in range(3):
    e2.append(gs.y[i] - npg.y_hat2[i])

ErrorTotal2 = 0
for i in range(3):
    ErrorTotal2 = ErrorTotal2 + e2[i] * e2[i]

#print("error nuevo =", e2)
#print("ErrorTotal2 =", ErrorTotal2)
