from Constantes import *
from Classes import Nota
import random

# Calcula la distancia en semitonos entre dos notas
def intervalost(nota1, nota2):
    st1 = semitonos[nota1.step]
    if int(nota1.alter) != 0:
        st1 += int(nota1.alter)
    st2 = semitonos[nota2.step]
    if int(nota2.alter) != 0:
        st1 += int(nota2.alter)
    distancia = st2 - st1
    if distancia < 0:
        distancia += 12
    return distancia


# calculo de probabilidades de dirección y tipo de intervalo segun el comportamiento del cantus firmus
# variable      indice en []    descripción
# psubir            0           probabilidad de tomar direccion de ascenso en altura
# pbajar            1           probabilidad de tomar direccion de descenso en altura
# prepetir          2           probabilidad de repetir la misma nota
# pgradoc           3           probabilidad de continuar por intervalo de grado continuo
# psalto            4           probabilidad de continuar por salto
def probabilidades(cfa, cf, saltos):
    psubir = 0.475
    pbajar = 0.475
    prepetir = 0.05
    pgradoc = 0.70
    if saltos == 0:
        psalto = 0.30
    else:
        psalto = 0
    if cf.octave == cfa.octave:
        if indices[cf.step] > indices[cfa.step]:
            psubir -= 0.225
            pbajar += 0.225
            prepetir -= 0.035
        elif indices[cf.step] < indices[cfa.step]:
            psubir += 0.255
            pbajar -= 0.255
            prepetir -= 0.035
        else:
            psubir += 0.05
            pbajar += 0.05
            prepetir = 0
    elif cf.octave > cfa.octave:
        psubir -= 0.25
        pbajar += 0.25
        prepetir -= 0.035
    else:
        psubir += 0.25
        pbajar -= 0.25
        prepetir -= 0.035
    distancia = (7 * int(cf.octave) + (indices[cf.step] + 1)) - (7 * int(cfa.octave) + (indices[cfa.step] + 1))
    if (distancia > 1 or distancia < -1) and saltos != 0:
        psalto -= 0.3
        pgradoc += 0.3
        prepetir -= 0.035
    probs = [psubir, pbajar, prepetir, pgradoc, psalto]
    return probs


# funcion que verifica los saltos para evitar saltos continuos
def saltos(compases):
    if compases != None:
        for i in range(len(compases)):
            for j in range(len(compases[i])):
                if len(compases[i]) <= 1:
                    # try:
                    if intervalost(compases[i][j], compases[i - 1][len(compases[i - 1]) - 1]) > 1 :
                        return 1
                    else:
                        return 0
                    # except
                else:
                    if intervalost(compases[i][j], compases[i][j - 1]) > 1 :
                        return 1
                    else:
                        return 0


# funcion especifica para el final
def final(notaCF,notaAnt,tonalidad):
    dist = indices[notaAnt.step] - indices[tonalidad]
    if  dist >= 4:
        octave = notaAnt.octave + 1
    elif dist <= -4 :
        octave = notaAnt.octave - 1
    elif dist < 4 and dist > 0:
        octave = notaAnt.octave
    elif dist > -4 and dist < 0:
        octave = notaAnt.octve
    nota = Nota(tonalidad, notaCF.alter, octave, notaCF.duration, notaCF.type, notaCF.dots)
    return nota

# función que genera el contraputno para el penultimo compas
def quintogrado(tonalidad, cf, nA):
    tonica = indices[tonalidad]
    quintogrado = tonica + 4
    if quintogrado > 6:
        quintogrado = quintogrado - 7
    tercera = quintogrado + 2
    quinta = quintogrado + 4
    if tercera > 6:
        tercera = tercera - 7
    if quinta > 6:
        quinta = quinta - 7
    notas_lst = [quintogrado, tercera, quinta]
    for i in range(len(notas_lst)):
        notas_lst[i] = Nota(notas[i], 0, '', '', '', '')
    dist_v = [
        intervalost(cf, notas_lst[0]),
        intervalost(cf, notas_lst[1]),
        intervalost(cf, notas_lst[2])
    ]
    dist_v_dict = {
        str(intervalost(cf, notas_lst[0])): notas[quintogrado],
        str(intervalost(cf, notas_lst[1])): notas[tercera],
        str(intervalost(cf, notas_lst[2])): notas[quinta]
    }
    dist_h = [
        intervalost(nA, notas_lst[0]),
        intervalost(nA, notas_lst[1]),
        intervalost(nA, notas_lst[2])
    ]
    dist_h_dict = {
        str(intervalost(nA, notas_lst[0])): notas[quintogrado],
        str(intervalost(nA, notas_lst[1])): notas[tercera],
        str(intervalost(nA, notas_lst[2])): notas[quinta]
    }
    min_v = min(dist_v)
    min_h = min(dist_h)
    min_v = dist_v_dict[str(min_v)]
    min_h = dist_h_dict[str(min_h)]
    if random.random() > 0.75:
        step = min_v
    else:
        step = min_h
    alter = nA.alter
    octave = nA.octave
    duration = cf.duration
    type = cf.type
    dots = cf.dots
    nota = Nota(step, alter, octave, duration, type, dots)
    return nota


# Función para identificar octavas y quintas paralelas y ocultas
def intervalos(compases1, compases2, compases3):
    notas = []
    for compases in [compases1, compases2, compases3]:
        nota_lst = []
        for compas in compases:
            if compas != None:
                for nota in compas:
                    nota_lst.append(nota)
        notas.append(nota_lst)

    for NOTAS1 in notas:
        for NOTAS2 in notas:
            if NOTAS2 != NOTAS1:
                if not paralelos(NOTAS1, NOTAS2):
                    return False

    for COMPASES1 in [compases1, compases2, compases3]:
        for COMPASES2 in [compases1, compases2, compases3]:
            if COMPASES2 != COMPASES1:
                for i in range(len(COMPASES1)):
                    if (i + 1) < len(COMPASES1):
                        for j in range(len(COMPASES1[i])):
                            try:
                                NOTAS1 = [COMPASES1[i][j],COMPASES1[i + 1][j]]
                                NOTAS2 = [COMPASES2[i][j],COMPASES1[i + 1][j]]
                                if not paralelos(NOTAS1, NOTAS2):
                                    return False
                            except IndexError:
                                return True
                            except TypeError:
                                return True

        # if not ocultos():
        #     return False


# funcion para identificar quintas y octavas en dos tiempos distintos, se utiliza para determinar quinats y octavas
# paralelas en la funcion intervalos
def paralelos(v1, v2):
    try:
        i1 = interval(v1[ - 2],v2[ - 2])
        i2 = interval(v1[ - 1], v2[ - 1])
        if (i1 == 8 and  i2 == 8) or (i1 == 5 and i2 == 8):
            return False
        else:
            return True
    except IndexError:
        return True


# funcion para identificar el intervalo entre las notas
def interval(n1, n2):
    if n1.step != 'R' and n2.step != 'R':
        n1 = indices[n1.step] + (((int(n1.octave) - 1) * 8) - 1)
        n2 = indices[n2.step] + (((int(n2.octave) - 1) * 8) - 1)
        nmin = min(n1,n2)
        nmax = max(n1,n2)

        interval = nmax - nmin
        while interval > 7:
            interval -= 7
        interval += 1
        return interval
