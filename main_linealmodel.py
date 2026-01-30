import values_xwyalpha as values
import y_predictiva as yp
import errorvector as evector
import errortotal as errort
import ajuste_transpuesta as ajt
import ajuste_pesos as ajp
import nueva_prediccion as np
import nuevo_vectorerror_errortotal as nvert
import funcion_de_perdida as fdp
import funcion_costo as fc
print("y_hat =", yp.y_hat)
print("error vector", evector.e)
print("ErrorTotal1 =", errort.ErrorTotal1)
print("X^T e =", ajt.grad)
print("nuevos pesos w =", values.w)
print("y_hat2 =", np.y_hat2)
print("error nuevo =", nvert.e2)
print("ErrorTotal2 =", nvert.ErrorTotal2)
print("La Función de Pérdida (MSE) es:", fdp.perdida)