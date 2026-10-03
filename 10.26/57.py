import random
import pickle
import os




class Paciente:

    def __init__(self,nombre, numClinica, dateLastVisit, codeEnfermedad):
        self.nombre = nombre
        self.numClinica = numClinica
        self.dateLastVisit = dateLastVisit
        self.codeEnfermedad = codeEnfermedad

    def __str__(self):
        r = "{:<30}". format("nombre del paciente: ",self.nombre)
        r += "{:<30}".format("historia clínica: ", self.numClinica)
        r += "{:<30}".format("fecha de la última: ", self.dateLastVisit)
        r += "{:<30}".format("código de la enfermedad: ", self.codeEnfermedad)

        return r


def add_in_order():
    vector = []
    numPacientes = int(input("cant de pacientes: "))
    nombres = ["Nina", "Quentin", "Hugo", "Simon", "Margaux", "Alice"]

    # this is not in order:
    for paciente in range(numPacientes):

        nombre = random.choice(nombres)
        numClinica = random.randint(100,999)
        dateLastVisit = random.randint(1,365)
        codeEnfermedad = random.randint(0,10)


        vector.append(Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad))
    print("creado! ")
    # this is in order  por historia clínica aka codeEnfermedad :

    primerPaciente = True
    for paciente in range(numPacientes):

        placeFound = False
        nombre = random.choice(nombres)
        numClinica = random.randint(100, 999)
        dateLastVisit = random.randint(1, 365)
        codeEnfermedad = random.randint(0, 10)

        if primerPaciente:
            vector.append(Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad))
            primerPaciente = False

        else:
            while not placeFound:
                izq = 0
                der = len(vector)
                centre = der // 2

                if vector[centre].codeEnfermedad > codeEnfermedad:
                    izq = 0
                    der = centre - 1
                    centre = der // 2

                    if centre == izq:
                        vector[centre:centre] = [Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad)]
                        placeFound = True


                elif vector[centre].codeEnfermedad < codeEnfermedad:
                    izq = centre + 1
                    der = len(vector)
                    centre = der // 2

                    if centre == der:
                        vector[centre:centre] = [Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad)]
                        placeFound = True

                elif vector[centre].codeEnfermedad == codeEnfermedad:
                    vector[centre:centre] = [Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad)]
                    placeFound = True
                else:
                    print("wtf")

    return vector



def mostrar_arreglo(vector):
    for i in range(len(vector)):
        print(vector[i])


def main():
    # vectorName = "pacientesVector"
    response = -1

    print("bienvenido! ")
    while response != 0:
        print()
        print("Choose the action: ")
        print("1. Recargar arreglo de pacientes")
        print("2. Mostrar por última vez en un período de d días ")
        print("3. Determinar si  igual a x.")
        print("4. Mostrar todos los datos del arreglo")
        print("5. Grabe todos los datos del arreglo en un archivo")
        print("6. Mostrar Grabados")
        print("7. crear otro arreglo código de enfermedad sea 8 o 9.")
        print("8. Mostrar el arreglo creado en el punto 7.")
        print()
        response = int(input("Num: "))

        if response == 1:
            pacientesVector =  add_in_order()
            mostrar_arreglo(pacientesVector)


if __name__ == "__main__":
    main()

