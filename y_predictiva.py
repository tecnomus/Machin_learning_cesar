
import values_xwyalpha as values
import numpy as np

#!Esto corresponde a cuanto espero que aprenda realmente el pokémon despues de los combates
x_np = np.array(values.x)
w_np = np.array(values.w)

y_hat = np.dot(x_np,w_np)
#print(y_hat)