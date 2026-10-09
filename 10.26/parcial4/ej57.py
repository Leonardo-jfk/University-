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

    file = open(nameOfFile, 'wb')

    for persona in range(cant):
        dni = random.randint(1000_000,999_999_9)
        # dni = random.choice([555, 444, 333])
        nombre = random.choice(nombres) + " " + random.choice(apellidos)
        edad = random.randint(16,100)
        sexo = random.choice(["m", "v"])
        duplicate = False

        # arregloVotantes.append(Votante(dni, nombre, edad, sexo))

        for i in range(len(arregloVotantes)):
            if arregloVotantes[i].dni == dni:
                duplicate = True

        arregloVotantes.append(Votante(dni, nombre, edad, sexo))


        if not duplicate:
            pickle.dump(Votante(dni, nombre, edad, sexo), file)


    # file = open(nameOfFile, 'wb')
    # pickle.dump(arregloVotantes, file)
    file.close()

def mostrar_archivo(nameOfFile):
    file = open(nameOfFile, 'rb')
    endOfFile = os.path.getsize(nameOfFile)
    pointer = file.tell()

    while file.tell() < endOfFile:

        print(pickle.load(file))
        # pointer = file.tell()

    file.close()


def trouver_votantes(nameOfFile):
    file = open(nameOfFile, 'rb')
    endOfFile = os.path.getsize(nameOfFile)
    x = int(input("ID a trouver: "))

    while file.tell() < endOfFile:
        votante = pickle.load(file)

        if votante.dni == x:
            print(votante)
            return


    print("personne etait trouve")
    print()

    file.close()

def cantidad_por_sexo(nameOfFile):

    file = open(nameOfFile, 'rb')
    endOfFile = os.path.getsize(nameOfFile)
    cant_mujeres, cant_hommes = 0, 0

    while file.tell() < endOfFile:
        votante = pickle.load(file)

        if votante.sexo == "m":
            cant_mujeres += 1

        else:
            cant_hommes += 1

    print("cantidad de mujeres: ", cant_mujeres)
    print("cantidad de hommes: ", cant_hommes)

    print()

    file.close()


def crear_segundo_archivo(nameOfFile, nameOfFile2):
    file1 = open(nameOfFile, 'rb')
    endOfFile = os.path.getsize(nameOfFile)
    file2 = open(nameOfFile2, 'wb')

    endOfFile = os.path.getsize(nameOfFile)

    while file1.tell() < endOfFile:
        votante = pickle.load(file1)
        if votante.edad > 70:
            pickle.dump(votante, file2)



    file1.close()
    file2.close()

def main():
    # global FD1, FD2
    nameOfFile = 'votantes.vot'
    nameOfFile2 = 'votantes2.vot'
    archivoFait, archivo2Fait = False, False
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
            cargar_archivo(nameOfFile)
            archivoFait = True
        if archivoFait:
            if op == 2:
                mostrar_archivo(nameOfFile)
            elif op == 3:
                trouver_votantes(nameOfFile)
            elif op == 4:
                cantidad_por_sexo(nameOfFile)
            elif op == 5:
                crear_segundo_archivo(nameOfFile, nameOfFile2)
                archivo2Fait = True
            elif op == 6:

                if archivo2Fait:
                    mostrar_archivo(nameOfFile2)
                else:
                    print("nous manqueons le point 5")

        else:
            print("la premiere option! ")



    print("ciao")
# script principal...
if __name__ == '__main__':
    main()