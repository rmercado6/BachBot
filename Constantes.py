# Diccionario de Semitonos
# Contiene los semitonos de cada nota tomando do 'C' como referencia
semitonos = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11
}

# Diccionario para identificar los intervalos
# Provee una numercaión de las notas para realizar el calculo de los intervalos
indices = {
    "C": 0,
    "D": 1,
    "E": 2,
    "F": 3,
    "G": 4,
    "A": 5,
    "B": 6
}

# Arreglo de notas
# usado para identificar las notas a través de un indice númerico, complemento del diccionariod e intervalos
notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
notas_semitonos = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Disonancias en semitonos      1,2,5,6,10,11
# Consonancias en semitonos     0,3,4,7,8,9,12
consonancias = [0,3,4,7,8,9,12]
disonancias = [1,2,5,6,10,11]

# se utiliza para definiar la tonalidad de un sistema
escalasMayoresSostenidos = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
escalasMayoresBemoles = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
escalasMayores = [escalasMayoresBemoles, escalasMayoresSostenidos]

# constantes de duración de notas
duration_constant = {
    'whole': 64,
    'half': 32,
    'quarter': 16,
    'eighth': 8,
    '16th': 4,
    '32nd': 2,
    '64th': 1
}

type_names = [
    'whole',
    'half',
    'quarter',
    'eighth',
    '16th',
    '32nd',
    '64th'
]

type_constant = {
    'whole': 0,
    'half': 1,
    'quarter': 2,
    'eighth': 3,
    '16th': 4,
    '32nd': 5,
    '64th': 6
}
