import sys


def salida(cf, cp1, cp2, datos):
    parts = [cf, cp1, cp2]

    # variable donde se guardara el string de salida (xml completo)
    xml = ''

    # Abrir archivo template (encabezado del xml)
    try:
        archivo = open('xml/template.xml', "r")
        templateln = archivo.readlines()
        archivo.close()

    except IOError:
        print("Mensaje de error")
        sys.exit(1)

    # Guardar el encabezado (template.xml) en la variable xml
    for line in templateln:
        xml += line

    # generar el resto del xml
    # *variable 'lines' tiene las lineas que se van generando para después guardarlas en xml
    # ---Agregar la lista de partes 'voces' o 'instrumentos'---
    lines = "\n\t<part-list>\n"

    id = ["CF", "CP1", "CP2"]

    for i in range(len(parts)):
        lines += "\t\t<score-part id='" + id[i] + "'>\n" \
                 "\t\t\t<part-name>" + parts[i].nombre + "</part-name>\n" \
                 "\t\t\t<part-abbreviation>" + id[i] + "</part-abbreviation>\n" \
                 "\t\t\t<midi-instrument id='" + id[i] + "'>\n"\
                 "\t\t\t\t<midi-channel>" + str(i + 1) + "</midi-channel>\n"\
                 "\t\t\t\t<midi-bank>" + str(i + 1) + "</midi-bank>\n" \
                 "\t\t\t\t<midi-program>" + str(i + 1) + "</midi-program>\n" \
                 "\t\t\t\t<pan>0</pan>\n" \
                 "\t\t\t</midi-instrument>\n" \
                 "\t\t</score-part>\n"
                 # "\t\t\t<score-instrument id='P1-" + id[i] + "'>\n" \
                 # "\t\t\t\t<instrument-name>Piano</instrument-name>\n" \
                 # "\t\t\t\t</score-instrument>\n" \
                 # "\t\t\t<midi-device id='P1-" + id[i] + "' port='1'></midi-device>\n" \
                 # "\t\t\t<midi-instrument id='P1-" + id[i] + "'>\n" \
                 # "\t\t\t\t<midi-channel>1</midi-channel>\n" \
                 # "\t\t\t\t<midi-program>1</midi-program>\n" \
                 # "\t\t\t\t<volume>78.7402</volume>\n" \
                 # "\t\t\t\t<pan>0</pan>\n" \
                 # "\t\t\t\t</midi-instrument>\n" \
                 # "\t\t\t</score-part>\n"

    lines += "\t</part-list>\n"

    # xml += lines

    for z in range(len(parts)):
        # generación de los compases y las notas y silencios
        for i in range(len(parts[z].compases)):
            # print(i)
            # llenar la información del compás (clave, compás, armadura) en el primer compás
            if i == 0:
                lines += "\t<part id='" + id[z] + "'>\n" \
                         "\t\t<measure number='" + str(i) + "'>\n" \
                         "\t\t\t<attributes>\n" \
                         "\t\t\t\t<divisions>" + str(len(parts[z].compases)) + "</divisions>\n" \
                         "\t\t\t\t<key>\n" \
                         "\t\t\t\t\t<fifths>" + str(datos[2]) + "</fifths>\n" \
                         "\t\t\t\t\t<mode>major</mode>\n" \
                         "\t\t\t\t</key>\n" \
                         "\t\t\t\t<time>\n" \
                         "\t\t\t\t\t<beats>" + str(datos[1][0]) + "</beats>\n" \
                         "\t\t\t\t\t<beat-type>" + str(datos[1][1]) + "</beat-type>\n" \
                         "\t\t\t\t</time>\n" \
                         "\t\t\t\t<clef>\n" \
                         "\t\t\t\t\t<sign>" + str(parts[z].clave[0]) + "</sign>\n" \
                         "\t\t\t\t\t<line>" + str(parts[z].clave[1]) + "</line>\n" \
                         "\t\t\t\t</clef>\n" \
                         "\t\t\t\t</attributes>\n" \
                         "\t\t\t<direction directive='yes' placement = 'above'>\n" \
                         "\t\t\t\t<direction-type>\n" \
                         "\t\t\t\t\t<metronome default-y='40' parentheses='yes'>\n" \
                         "\t\t\t\t\t\t<beat-unit>quarter</beat-unit>\n" \
                         "\t\t\t\t\t\t<per-minute>120</per-minute>\n" \
                         "\t\t\t\t\t</metronome>\n" \
                         "\t\t\t\t</direction-type>\n" \
                         "\t\t\t\t<sound tempo='120'/>\n" \
                         "\t\t\t</direction>\n"

            else:
                lines += "\t\t<measure number='" + str(i) + "'>\n" \
                         "\t\t\t<attributes>\n" \
                         "\t\t\t\t<clef>\n" \
                         "\t\t\t\t\t<sign>" + str(parts[z].clave[0]) + "</sign>\n" \
                         "\t\t\t\t\t<line>" + str(parts[z].clave[1]) + "</line>\n" \
                         "\t\t\t\t</clef>\n" \
                         "\t\t\t</attributes>\n"

            for j in range(len(parts[z].compases[i])):
                # print(parts[k].compases[i][j].toString())
                if parts[z].compases[i][j].step != 'R':
                    lines += "\t\t\t<note>\n" \
                             "\t\t\t\t<pitch>\n" \
                             "\t\t\t\t\t<step>" + str(parts[z].compases[i][j].step) + "</step>\n" \
                             "\t\t\t\t\t<alter>" + str(parts[z].compases[i][j].alter) + "</alter>\n"\
                             "\t\t\t\t\t<octave>" + str(parts[z].compases[i][j].octave) + "</octave>\n" \
                             "\t\t\t\t</pitch>\n" \
                             "\t\t\t\t<duration>" + str(parts[z].compases[i][j].duration) + "</duration>\n" \
                             "\t\t\t\t<voice>1</voice>\n" \
                             "\t\t\t\t<type>" + str(parts[z].compases[i][j].type) + "</type>\n"
                    if parts[z].compases[i][j].dots == 0:
                        lines += "\t\t\t</note>\n"
                    else:
                        for k in range(parts[z].compases[i][j].dots):
                            lines += "\t\t\t\t<dot/>\n"
                        lines += "\t\t\t</note>\n"
                else:
                    lines += "\t\t\t<note>\n" \
                             "\t\t\t\t<rest/>\n" \
                             "\t\t\t\t<duration>" + str(parts[z].compases[i][j].duration) + "</duration>\n" \
                             "\t\t\t\t<voice>1</voice>\n" \
                             "\t\t\t\t<type>" + str(parts[z].compases[i][j].type) + "</type>\n"
                    if parts[z].compases[i][j].dots == 0:
                        lines += "\t\t\t\t</note>\n"
                    else:
                        for each in range(parts[z].compases[i][j].dots):
                            lines += "\t\t\t\t<dot/>\n"
                        lines += "\t\t\t\t</note>\n"
            if i != len(parts[z].compases) - 1:
                lines += "\t\t</measure>\n"
            else:
                lines += "\t\t\t<barline location='right'>\n" \
                         "\t\t\t\t<bar-style>light-heavy</bar-style>\n" \
                         "\t\t\t\t</barline>\n" \
                         "\t\t\t</measure>\n" \
                         "\t\t</part>\n" \

    lines += "\t</score-partwise>\n"

    # completar el xml a imprimir en el archivo
    xml += lines

    # Abrir el archivo de salida y escribir el xml
    try:
        archivo = open('xml/output.xml', "w")
        archivo.write(xml)
        archivo.close()

    except IOError:
        print("Mensaje de error")
        sys.exit(1)
