from Classes import Nota
from Constantes import *
import random
import funciones as func


# Me dio mucha flojera comentar toda la funcion
# basicamente es donde se hacen los calculos necesarios para elegir la nota a colocar en el contrapunto
# hay condicionales para saber que compas es pues el primero el penultimo y el ultimo son compases especiales,
# revisa si la nota que se pone es consonancia o disonancia en referencia con las demas voces y si puede ser disinancia
# o consonancia dependiendo del timepo del compas en el que se encuentra.
# Evita que existan tritonos en cualquiera de los casos posibles
# def primera_especie(cp, cf, cf2, ncompas, nnota):
#
#     notacf = cf.compases[ncompas][nnota]
#     # if cf2.compases[ncompas] != []:
#     #     notacf2 = cf2.compases[ncompas][nnota]
#     # else:
#     #     notacf2 = None
#
#     # primer compas
#     if ncompas == 0:
#         notacp = Nota('', '', '', '', '', '')
#         if cp.clave != ['F', '4'] and random.random() > 0.5:
#             notacp.step = indices[notacf.step] + 4
#             if notacp.step > 6:
#                 notacp.step -= 7
#             notacp.step = notas[notacp.step]
#         else:
#             notacp.step = notacf.step
#         notacp.alter = notacf.alter
#
#         if cp.clave == ['F', '4']:
#             notacp.octave = int(notacf.octave) - 1
#         elif indices[notacf.step] < indices[notacp.step]:
#             notacp.octave = notacf.octave
#         else:
#             notacp.octave = int(notacf.octave) + 1
#
#         notacp.duration = notacf.duration
#         notacp.type = notacf.type
#         notacp.dots = notacf.dots
#
#         cp.compases[ncompas].append(notacp)
#
#     # penultimo compas
#     elif ncompas == len(cf.compases) - 2:
#
#         if int(cf.alteraciones) < 0:
#             tonalidad = escalasMayores[0][abs(int(cf.alteraciones))]
#         else:
#             tonalidad = escalasMayores[1][abs(int(cf.alteraciones))]
#
#         notacf = cf.compases[ncompas][nnota]
#         nota_ant = cp.compases[ncompas - 1][len(cp.compases[ncompas - 1]) - 1]
#         notacp = func.quintogrado(tonalidad, notacf, nota_ant)
#
#         cp.compases[ncompas].append(notacp)
#
#     # ultimo compas
#     elif ncompas == len(cf.compases) - 1:
#         if int(cf.alteraciones) < 0:
#             tonalidad = escalasMayores[0][abs(int(cf.alteraciones))]
#         else:
#             tonalidad = escalasMayores[1][abs(int(cf.alteraciones))]
#
#         nota_ant = cp.compases[ncompas - 1][len(cp.compases[ncompas - 1]) - 1]
#         notacf = cf.compases[ncompas][nnota]
#         notacp = func.final(notacf, nota_ant, tonalidad)
#
#         if cp.clave != ['F', '4'] and random.random() < 0.33:
#             notacp.step = indices[notacf.step] + 2
#             if notacp.step > 7:
#                 notacp.step -= 7
#             notacp.step = notas[notacp.step]
#         elif cp.clave != ['F', '4'] and random.random() < 0.33:
#             notacp.step = indices[notacf.step] + 4
#             if notacp.step > 7:
#                 notacp.step -= 7
#             notacp.step = notas[notacp.step]
#         else:
#             notacp.step = tonalidad
#
#         cp.compases[ncompas].append(notacp)
#
#     # resto de los compases
#     else:
#         salto = 0
#         notacp = Nota('', '', '', '', '', '')
#         notacf = cf.compases[ncompas][nnota]
#         notacfant = cf.compases[ncompas - 1][len(cp.compases[ncompas - 1]) - 1]
#         nota_ant = cp.compases[ncompas - 1][len(cp.compases[ncompas - 1]) - 1]
#         prob = func.probabilidades(notacfant, notacf, salto)
#         while True:
#             rand_dist = random.random()
#             rand_dir = random.random()
#             if rand_dir > prob[2]:
#                 if rand_dir > prob[1] + prob[2]:
#                     if rand_dist <= prob[4]:
#                         while True:
#                             step = random.randint(2, 5)
#                             step += indices[nota_ant.step]
#                             while step > 6:
#                                 step -= 7
#                             if func.intervalost(nota_ant, Nota(notas[step], 0,
#                                                                int(nota_ant.octave), '', '', '')) != 6:
#                                 break
#                     else:
#                         step = 1
#                 else:
#                     if rand_dist <= prob[4]:
#                         step = random.randint(2, 5)
#                         step = step * -1
#                     else:
#                         step = -1
#             else:
#                 step = 0
#             step += indices[nota_ant.step]
#             octave = int(nota_ant.octave)
#             if step > 6:
#                 step -= 7
#                 octave += 1
#             elif step < 0:
#                 step += 7
#                 octave -= 1
#             notacp.step = notas[step]
#             notacp.alter = 0
#             notacp.octave = octave
#             notacp.duration = notacf.duration
#             notacp.type = notacf.type
#             notacp.dots = notacf.dots
#             if nnota != 0:
#                 if func.intervalost(notacp, notacf) != 6:
#                     compas_temp = []
#                     for k in range(len(cp.compases[ncompas])):
#                         compas_temp.append(cp.compases[ncompas][k])
#                     if func.intervalos([cf.compases[ncompas - 1], cf.compases[ncompas]],
#                                        [cf2.compases[ncompas - 1], cf2.compases[ncompas]],
#                                        [cp.compases[ncompas - 1], compas_temp.append(notacp)]):
#                         cp.compases[ncompas].append(notacp)
#                         break
#                     if func.paralelos([nota_ant, notacp], [notacfant, notacf]):
#                         cp.compases[ncompas].append(notacp)
#                         break
#             else:
#                 if func.intervalost(notacp, notacf) in consonancias:
#                     compas_temp = []
#                     for k in range(len(cp.compases[ncompas])):
#                         compas_temp.append(cp.compases[ncompas][k])
#                     if func.intervalos([cf.compases[ncompas - 1], cf.compases[ncompas]],
#                                        [cf2.compases[ncompas - 1], cf2.compases[ncompas]],
#                                        [cp.compases[ncompas - 1], compas_temp.append(notacp)]):
#                         cp.compases[ncompas].append(notacp)
#                         break
#                     if func.paralelos([nota_ant, notacp], [notacfant, notacf]):
#                         cp.compases[ncompas].append(notacp)
#                         break


def especies(cp, cf, cf2, ncompas, nnota):
    notacf = cf.compases[ncompas][nnota]
    # if cf2.compases[ncompas] != []:
    #     notacf2 = cf2.compases[ncompas][nnota]
    # else:
    #     notacf2 = None

    nnotas_especie = 1
    if cp.especie == 2:
        nnotas_especie = 2
        type_incr = 1
    elif cp.especie == 3:
        nnotas_especie = 4
        type_incr = 2
    # primer compas
    for nnotacp in range(nnotas_especie):
        if ncompas == 0 and nnotacp != 0:
            notacp = Nota('', '', '', '', '', '')
            if cp.clave != ['F', '4'] and random.random() > 0.5:
                notacp.step = indices[notacf.step] + 4
                if notacp.step > 6:
                    notacp.step -= 7
                notacp.step = notas[notacp.step]
            else:
                notacp.step = notacf.step
            notacp.alter = notacf.alter

            if cp.clave == ['F', '4']:
                notacp.octave = int(notacf.octave) - 1
            elif indices[notacf.step] < indices[notacp.step]:
                notacp.octave = notacf.octave
            else:
                notacp.octave = int(notacf.octave) + 1

            type2 = type_constant[notacf.type] + type_incr
            type2 = type_names[type2]
            duration = duration_constant[type2]
            notacp.type = type2
            notacp.duration = duration
            notacp.dots = notacf.dots

            # notacp.duration = notacf.duration
            # notacp.type = notacf.type
            # notacp.dots = notacf.dots

            cp.compases[ncompas].append(notacp)
        elif ncompas == 0 and nnota == 0 :
            notacp = Nota('R', None, 0, None, None, None)

            type2 = type_constant[notacf.type] + type_incr
            type2 = type_names[type2]
            duration = duration_constant[type2]
            notacp.type = type2
            notacp.duration = duration
            notacp.dots = notacf.dots

            cp.compases[ncompas].append(notacp)

        # penultimo compas
        elif ncompas == len(cf.compases) - 2:

            if int(cf.alteraciones) < 0:
                tonalidad = escalasMayores[0][abs(int(cf.alteraciones))]
            else:
                tonalidad = escalasMayores[1][abs(int(cf.alteraciones))]

            notacf = cf.compases[ncompas][nnota]
            nota_ant = cp.compases[ncompas - 1][len(cp.compases[ncompas - 1]) - 1]
            notacp = func.quintogrado(tonalidad, notacf, nota_ant)

            type2 = type_constant[notacf.type] + type_incr
            type2 = type_names[type2]
            duration = duration_constant[type2]
            notacp.type = type2
            notacp.duration = duration
            notacp.dots = notacf.dots

            cp.compases[ncompas].append(notacp)

        # ultimo compas
        elif ncompas == len(cf.compases) - 1:
            if (nnotacp == 0):
                if int(cf.alteraciones) < 0:
                    tonalidad = escalasMayores[0][abs(int(cf.alteraciones))]
                else:
                    tonalidad = escalasMayores[1][abs(int(cf.alteraciones))]

                nota_ant = cp.compases[ncompas - 1][len(cp.compases[ncompas - 1]) - 1]
                notacf = cf.compases[ncompas][nnota]
                notacp = func.final(notacf, nota_ant, tonalidad)

                if cp.clave != ['F', '4'] and random.random() < 0.33:
                    notacp.step = indices[notacf.step] + 2
                    if notacp.step > 7:
                        notacp.step -= 7
                    notacp.step = notas[notacp.step]
                elif cp.clave != ['F', '4'] and random.random() < 0.33:
                    notacp.step = indices[notacf.step] + 4
                    if notacp.step > 7:
                        notacp.step -= 7
                    notacp.step = notas[notacp.step]
                else:
                    notacp.step = tonalidad

                cp.compases[ncompas].append(notacp)

        # resto de los compases
        else:
            salto = 0
            notacp = Nota('', '', '', '', '', '')
            notacf = cf.compases[ncompas][nnota]

            if nnota == 0:
                notacfant = cf.compases[ncompas - 1][len(cf.compases[ncompas - 1]) - 1]
                # notacfant = cf.compases[ncompas - 1][len(cp.compases[ncompas - 1]) - 1]
                if nnotacp == 0:
                    nota_ant = cp.compases[ncompas - 1][len(cp.compases[ncompas - 1]) - 1]
            else:
                notacfant = cf.compases[ncompas][nnota]
                nota_ant = cp.compases[ncompas][nnotacp - 1]

            prob = func.probabilidades(notacfant, notacf, salto)
            while True:
                rand_dist = random.random()
                rand_dir = random.random()
                if rand_dir > prob[2]:
                    if rand_dir > prob[1] + prob[2]:
                        if rand_dist <= prob[4]:
                            while True:
                                step = random.randint(2, 5)
                                step += indices[nota_ant.step]
                                while step > 6:
                                    step -= 7
                                if func.intervalost(nota_ant, Nota(notas[step], 0,
                                                                   int(nota_ant.octave), '', '', '')) != 6:
                                    break
                        else:
                            step = 1
                    else:
                        if rand_dist <= prob[4]:
                            step = random.randint(2, 5)
                            step = step * -1
                        else:
                            step = -1
                else:
                    step = 0
                step += indices[nota_ant.step]
                octave = int(nota_ant.octave)
                if step > 6:
                    step -= 7
                    octave += 1
                elif step < 0:
                    step += 7
                    octave -= 1
                notacp.step = notas[step]
                notacp.alter = 0
                notacp.octave = octave

                type2 = type_constant[notacf.type] + type_incr
                type2 = type_names[type2]
                duration = duration_constant[type2]
                notacp.type = type2
                notacp.duration = duration
                notacp.dots = notacf.dots
                # notacp.duration = notacf.duration
                # notacp.type = notacf.type
                # notacp.dots = notacf.dots
                if nnota != 0:
                    if func.intervalost(notacp, notacf) != 6:
                        compas_temp = []
                        for k in range(len(cp.compases[ncompas])):
                            compas_temp.append(cp.compases[ncompas][k])
                        if func.intervalos([cf.compases[ncompas - 1], cf.compases[ncompas]],
                                           [cf2.compases[ncompas - 1], cf2.compases[ncompas]],
                                           [cp.compases[ncompas - 1], compas_temp.append(notacp)]):
                            cp.compases[ncompas].append(notacp)
                            break
                        if func.paralelos([nota_ant, notacp], [notacfant, notacf]):
                            cp.compases[ncompas].append(notacp)
                            break
                else:
                    if func.intervalost(notacp, notacf) in consonancias:
                        compas_temp = []
                        for k in range(len(cp.compases[ncompas])):
                            compas_temp.append(cp.compases[ncompas][k])
                        if func.intervalos([cf.compases[ncompas - 1], cf.compases[ncompas]],
                                           [cf2.compases[ncompas - 1], cf2.compases[ncompas]],
                                           [cp.compases[ncompas - 1], compas_temp.append(notacp)]):
                            cp.compases[ncompas].append(notacp)
                            break
                        if func.paralelos([nota_ant, notacp], [notacfant, notacf]):
                            cp.compases[ncompas].append(notacp)
                            break