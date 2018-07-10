import especies as contrapunto
from threading import Condition, Thread

# arreglo que contiene los hilos que se van a generar
threads = []
# objeto de clase consicion para mantener un control de la ejecucion de los hilos, el hilo 2 depende del hilo 1
condition = Condition()

# funcion para realizar el conrapunto en procesamiento paralelo
# argumento     descripción
#   cf          objeto de clase voz del cantus firmus
#   cp1         objeto de clase voz del contrapunto 1
#   cp2         objeto de clase voz del contrapunto 2
def contrapunto_paralelo(cf, cp1, cp2):

    # Se generan los hilos, uno para cada voz y se inician
    for func in [contrapunto1, contrapunto2]:
        threads.append(Thread(target=func, args=(cf, cp1, cp2)))
        threads[-1].start()

    # espera a que terminen los hilos para volver a la ejecución del hilo principal
    for thread in threads:
        thread.join()

    # print("Se realizo el contrapunto en paralelo")


# funcion que manda llamar el contraputno para la primera voz del contrapunto cp1
def contrapunto1(cf, cp1, cp2):
    # adquiere el condicional que controla la ejecucion de los hilos
    condition.acquire()
    # para cada compas, para cada nota en ese compas, ejecutara la primera especi del contrapunto
    for ncompas in range(len(cf.compases)):
        for nnota in range(len(cf.compases[ncompas])):
            # print("cp1 " + str(ncompas))
            contrapunto.especies(cp1, cf, cp2, ncompas, nnota)
        # una vez que termina de llenar un compas, notifica al condicional que ya cuenta conrecursos (compas) para que
        # el segundo hilo pueda trabajar.
        condition.notify()
    # libera al condicional de control
    condition.release()


# funcion que manda llamar el contraputno para la segunda voz del contrapunto cp2
def contrapunto2(cf, cp1, cp2):
    # adquiere el condicional que controla la ejecucion de los hilos
    condition.acquire()
    # para cada compas, para cada nota en ese compas, ejecutara la primera especi del contrapunto. Revisa si el compas
    # del otro contrapunto esta vacio o no, si no esta vacio continua con el conrapunto, si esta vacio, espera a que el
    # primer hilo notifique que ya hay recursos con que trabajar
    for ncompas in range(len(cf.compases)):
        if cp1.compases[ncompas] != []:
            for nnota in range(len(cf.compases[ncompas])):
                # print(cp2.compases[ncompas])
                contrapunto.especies(cp2, cf, cp1, ncompas, nnota)
                # print("cp2 x")
        else:
            condition.wait()
    # libera al condicional de control
    condition.release()


