import gengar_stats as gs
import yp_gengar as ypg
import errorvector_gengar as ervector
import errortotal_gengar as errort
import ajuste_transpuesta_gengar as ajtg
import ajuste_pesos_gengear as ajpg
import nueva_prediccion_gengar as npg
import new_vec_err_gengar as nvert
import f_perdida_gengar as fdpg
print("y_hat =", ypg.y_hat)
print("error vector", ervector.e)
print("ErrorTotal1 =", errort.ErrorTotal1)
print("X^T e =", ajtg.grad)
print("nuevos pesos w =", gs.w)
print("y_hat2 =", npg.y_hat2)
print("error nuevo =", nvert.e2)
print("ErrorTotal2 =", nvert.ErrorTotal2)
print("La Función de Pérdida (MSE) es:", fdpg.perdida)