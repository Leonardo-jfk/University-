import io
import pickle
import os.path
import random

class Paciente:
    def __init__(self, hc, nom, fec, cod):
        self.hist_clinica = hc
        self.nombre = nom
        self.fecha = fec
        self.cod_problema = cod


def crear_paciente():
    cant = int(input('Cantidad de pacientes: '))


    FD = 'pacientes.med'


    # tbm = os.path.getsize(FD)
    m = open(FD, 'wb')

    for pac in range(cant):
        hist_clinica = random.randint(1, 1000)
        nombre = random.choice(["aa", "bb", "cc", "dd"])
        fecha = random.randint(1, 100)
        cod_problema = random.randint(1, 100)

        pickle.dump(Paciente(hist_clinica, nombre, fecha, cod_problema), m)


    m.close()

def mostrar_paciente():
    FD = 'pacientes.med'
    file = open(FD, 'rb')
    endOfFile = os.path.getsize(FD)
    while file.tell() < endOfFile:
        print(pickle.load(file))

    file.close()


def display(pac):
    print('Historia clínica:', pac.hist_clinica, end=' ')
    print('Nombre:', pac.nombre, end=' ')
    print('Dias desde su última visita:', pac.fecha, end=' ')
    print('Código de enfermedad:', pac.cod_problema)


def mostrar_mayores():
    FD = 'pacientes.med'

    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        crear_paciente()
        print("kk")
        mostrar_paciente()
        return

    crear_paciente()
    mostrar_paciente()


    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    ac, c = 0, 0
    while m.tell() < tbm:
        pac = pickle.load(m)
        ac += pac.fecha
        c += 1
    p = ac / c

    print('Pacientes con dias de re-visita mayor al promedio de días:')
    # os.path(m, 0, io.SEEK_SET)
    m.seek(0, io.SEEK_SET)
    while m.tell() < tbm:
        pac = pickle.load(m)
        if pac.fecha > p:
            display(pac)

    m.close()
    print("ksfdmkmf")


# script principal...
if __name__ == '__main__':
    mostrar_mayores()