from Classes import Nota
from Constantes import *
import random
import funciones as func
import especies as especies


# Funcion para hacer el contrapunto, se utiliza para la realizacion del contrapunto en procesamiento lineal
def contrapunto(cp, cf, cf2):
    for ncompas in range(len(cf.compases)):
        for nnota in range(len(cf.compases[ncompas])):
            # if cp.especie == 1:
            #     especies.primera_especie(cp, cf, cf2, ncompas, nnota)
            # else:
            especies.especies(cp, cf, cf2, ncompas, nnota)
