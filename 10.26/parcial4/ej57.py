import io
import pickle
import os.path
import random

class Votante:
    def __init__(self, dn, nom, ed, sex):
        self.dni = dn
        self.nombre = nom
        self.edad = ed
        self.sexo = sex


def __str__(self):

    sx = 'Hombre'
    if self.sexo == 'm':
        sx = 'Mujer'
        r = ''
        r += '{:<20}'.format('DNI: ' + str(self.dni))
        r += '{:<30}'.format('Nombre: ' + self.nombre)
        r += '{:<20}'.format('Edad: ' + str(self.edad))
        r += '{:<20}'.format('Sexo: ' + sx)
    return r

def cargar_archivo(nameOfFile):
    arregloVotantes = []
    cant = int(input("cuantas votantes: "))
    nombres = ["quentin", "nina", "simon", "rafael", "margaux", "alice"]
    apellidos = ["eon", "françois", "Sancozy", "Di Maria", "Lu pain"]

    for persona in range(cant):
        dni = random.randint(1000_000,999_999_9)
        nombre = random.choice(nombres) + " " + random.choice(apellidos)
        edad = random.randint(16,100)
        sexo = random.choice(["m", "v"])

        arregloVotantes.append(Votante(dni, nombre, edad, sexo))


    file = open(nameOfFile, 'wb')
    pickle.dump(arregloVotantes, file)
    file.close()

def mostrar_archivo(nameOfFile):
    file = open(str(nameOfFile), 'rb')
    endOfFile = os.path.getsize(nameOfFile)
    pointer = int(file.seek(nameOfFile))

    while pointer < endOfFile:

        print(pickle.load(file))
        pointer = int(file.seek(nameOfFile))

    file.close()


def main():
    # global FD1, FD2
    nameOfFile = 'votantes.vot'
    FD2 = 'mayores.vot'
    op = -1
    while op != 0:
        print('Padrón electoral')
        print(' 1. Registrar votantes en el padrón')
        print(' 2. Listado de votantes')
        print(' 3. Buscar un votante por dni')
        print(' 4. Cantidad de varones y mujeres')
        print(' 5. Crear archivo con votantes mayores a 70 años')
        print(' 6. Mostrar el archivo de votantes mayores a 70 años')
        print(' 0. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()
        if op == 1:
            # pass
            cargar_archivo(nameOfFile)
        elif op == 2:
            pass
            mostrar_archivo(nameOfFile)
        elif op == 3:
            pass
            # buscar_votante()
        elif op == 4:
            pass
            # cantidad_por_sexo()
        elif op == 5:
            pass
            # crear_segundo_archivo()
        elif op == 6:
            pass
            # mostrar_archivo(FD2)
        elif op == 7:
            pass

    print("ciao")
# script principal...
if __name__ == '__main__':
    main()