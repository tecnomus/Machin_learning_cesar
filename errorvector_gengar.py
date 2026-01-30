import gengar_stats as gs
import yp_gengar as yp

e = []

for i in range(3):
    e.append(gs.y[i] - yp.y_hat[i])

#print("error e =", e)
