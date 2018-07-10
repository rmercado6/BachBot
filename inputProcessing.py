import xml.etree.ElementTree as etree
from Classes import Nota
def entrada():
    # importar el xml como un árbol
    tree = etree.parse('xml/ejemplo.xml')
    root = tree.getroot()

    # ubicar la primera voz que encuentre en el xml (part = voz ['instrumento'])
    part = root.find('part')

    # generar la lista con todos los compases
    measures = part.findall('measure')

    # encontrar los atributos 'cualidades' de la voz, siempre se incluyen en el primer compas 'measures[0]'
    attributes = measures[0].find('attributes')

    # encontrar la tonalidad (armadura) a través de las alteraciones (cículo de quintas)
    key = attributes.find('key').find('fifths').text

    # signo de tiempo
    time = []
    time.append(attributes.find('time').find('beats').text)
    time.append(attributes.find('time').find('beat-type').text)

    # clave
    clef = []
    clef.append(attributes.find('clef').find('sign').text)
    clef.append(attributes.find('clef').find('line').text)

    # generación de arreglo de vox (sistema)
    # cf = [] *es el arreglo del 'cantus firmus' la voz base que se da como entrada al programa
    # indice descripción    variable
    #   0       Clave       clef
    #   1       Compás      time
    #   2       Armadura    key
    # 3-fin     compases    measures(lista) || measure(individual)
    #                       *los compases se dividen en listas de notas donde se incluyen sus cualidades(nota, indice, duración y tipo)

    cf = [clef, time, key]

    # separación de notas y silencios por compás
    # variable   descripción
    # measures      lista de todos los compases en el xml
    # measure       compás individual que pertenece a la lista 'measures'
    # notes         lista de notas dentro de un compás 'measure'
    # note          nota individual dentro de la lista 'notes'
    # compas        lista de notas de un mismo compas procesadas con formato para agregar a cf
    # nota          lista de las características de una nota:
    #                   posición    descripción         ejemplo     casos de silencio
    #                       0           nota                G           'R'
    #                       1           alteración          -1          -
    #                       2           indice              4           0
    #                       3           duración            8           int
    #                       4           tipo de figura    'whole'       str
    #                       5           puntillos           1           int
    for measure in measures:
        notes = measure.findall('note')
        compas = []
        for note in notes:
            if note.find('pitch') :
                lstnota = [note.find('pitch').find('step').text,
                           None,
                           note.find('pitch').find('octave').text,]
            else:
                lstnota = ['R',
                        0]
            lstnota.append(note.find('duration').text)
            lstnota.append(note.find('type').text)
            dots = note.findall('dot')
            puntillos = len(dots)
            lstnota.append(puntillos)
            try :
                lstnota[1] = note.find('pitch').find('alter').text
            except:
                lstnota[1] = 0
            nota = Nota(lstnota[0], lstnota[1], lstnota[2], lstnota[3], lstnota[4], lstnota[5])
            compas.append(nota)
        cf.append(compas)

    return(cf)
