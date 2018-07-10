# Clase 'Voz'
# Define los objetos como voces, les da los atributos:
#   - indice    número de voz (identificador)
#   - especie   Especie del contrapunto que se aplica a esa voz (1, 2, 3, 4 o 5)
#   - clave     Clave en que esta escrita esa voz
#   - nombre    Nombre de la voz ej. 'Cantus Firmus'
#   - compases  Compases pertenecientes a esa voz, información principal para el desarrollo del contrapunto
class Voz:

    def __init__(self, indice, especie, clave, alteraciones, compases, nombre):
        self.indice = indice
        self.especie = especie
        self.clave = clave
        self.alteraciones = alteraciones
        self.compases = compases
        self.nombre = nombre


# Clase 'Nota'
# Define los objetos de tipo nota (notas musicales)
# Les d los atributos:
#   - step      Nombre de la nota ej. 'C'
#   - alter     Alteraciones de la nota ej. 1
#   - octave    Octava de la nota (altura) ej. 4
#   - duration  Duración de la nota en formato de MusicXML ej. 4
#   - type      Tipo de figura ej. 'whole'
#   - dots      Puntillos, si la nota tiene puntillos que alargan su duración o no. ej. 0
class Nota:

    def __init__(self, step, alter, octave, duration, type, dots):
        self.step = step
        self.alter = alter
        self.octave = octave
        self.duration = duration
        self.type = type
        self. dots = dots

    # Devuelve un string con la información del objeto
    # Su finalidad principal es observar en la consola el comportamiento de los objetos durante el proceso
    def toString(self):
        string = (str(self.step) + ", " +
                  str(self.alter) + ", " +
                  str(self.octave) + ", " +
                  str(self.duration) + ", " +
                  str(self.type) + ", " +
                  str(self.dots))

        return string
