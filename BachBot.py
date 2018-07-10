import inputProcessing as inputFile
import outputProcessing as outputFile
from Classes import *
import Contrapunto as contrapunto
from ContrapuntoParalelo import contrapunto_paralelo as cont_par
from Constantes import escalasMayores as escalas
import time

# guardar el tiempo de inicio de proceso
# tiempo_inicio = time.time()

# procesar la información de entrada
entrada = inputFile.entrada()

# separar los aspectos clave de la partritura
# Variable      Descripción
#   clave           guarda la información de la clave en un arreglo [signo, linea] ej. ['G', '2']
#   timepo          guarda la información del ritmo (compas) en un arreglo ['pulsos', 'figura'] ej. ['4', '4']
#   armadura        guarda la información de la armadura (tonalidad) en un arreglo [Número de sostenidos o bemoles]
#                   ej. [0],
#                       [1] *para sostenidos,
#                       [-1] *para bemoles
#   tonalidad       guarda la nota tónica, da la tonalidad, para conocer las alteraciones necesarias. ej. 'C'
#   compases        guarda los compases introducidos en en archivo de entrada en un arreglo [compas, compas, compas]
#                       donde cada compas es un arreglo de notas [nota, nota, nota]
#                       donde cada nota es un arreglo de clase nota.
#                       por lo tanto la estructura de compases es [[nota,nota],[nota,nota],[nota,nota]]
#   datos           guarda un arreglo de los datos generales de la partitura de entrada [clave, timepo,armadura]
clave = entrada[0]
tiempo = entrada[1]
armadura = entrada[2]
if int(armadura) < 0:
    tonalidad = escalas[0][abs(int(armadura))]
else:
    tonalidad = escalas[1][abs(int(armadura))]
compases = []
for i in range(3, len(entrada)):
    compases.append(entrada[i])

datos = [clave, tiempo, armadura]

# generar los objetos de las voces (Cantus Firmus [cf], Contrapunto 1[cp1] y Contrapunto 2 [cp2])
cf = Voz(0, 1, clave, armadura, compases, 'Cantus Firmus')
if cf.clave == ['G', '2']:
    cp1 = Voz(1, 2, ['F', '4'], armadura, [], 'Contrapunto 1')
    cp2 = Voz(2, 3, clave, armadura, [], 'Contrapunto 2')
else:
    cp1 = Voz(1, 2, ['G', '2'], armadura, [], 'Contrapunto 1')
    cp2 = Voz(2, 3, ['G', '2'], armadura, [], 'Contrapunto 2')

# Se llenan las voces del contrapunto ( 1 y 2 ) con compases (arreglos) vacios [] para que tenga la misma longitud que
# el cantus firmus (CF)
for compas in cf.compases:
    cp1.compases.append([])
    cp2.compases.append([])

tiempo_inicio = time.time()
# Se corre el contrapunto en paralelo
cont_par(cf, cp1, cp2)

# Se corre el contrapunto de manera lineal
# contrapunto.contrapunto(cp1, cf, cp2)
# contrapunto.contrapunto(cp2, cf, cp1)

tiempo_procesamiento = time.time() - tiempo_inicio

# Se imprime en la consola los objetos nota de cada voz
parts = [cf, cp1, cp2]

for part in parts:
    print(part.nombre)
    print(part.clave)
    for compases in part.compases:
        for note in compases:
            try:
                print(note.toString())
            except AttributeError:
                print("ERROR AL REALIZAR EL CONTRAPUNTO")
    print()

# se genera el archivo de salida
outputFile.salida(cf, cp1, cp2, datos)

# se calcula el timepo de proceso y se imprime en consola

print(tiempo_procesamiento)
