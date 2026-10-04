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
        r = "{:<30}". format("nombre del paciente: " + self.nombre)
        r += "{:<30}".format("historia clínica: " + str(self.numClinica))
        r += "{:<30}".format("fecha de la última: " + str(self.dateLastVisit))
        r += "{:<30}".format("código de la enfermedad: " + str(self.codeEnfermedad))

        return r


def add_in_order():
    vector = []
    numPacientes = int(input("cant de pacientes: "))
    # vector = [None] * numPacientes
    nombres = ["Nina", "Quentin", "Hugo", "Simon", "Margaux", "Alice"]

    # this is not in order:
    # for paciente in range(numPacientes):
    #
    #     nombre = random.choice(nombres)
    #     numClinica = random.randint(100,999)
    #     dateLastVisit = random.randint(1,365)
    #     codeEnfermedad = random.randint(0,10)
    #
    #
    #     vector.append(Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad))
    # print("creado! ")
    # this is in order  por historia clínica aka codeEnfermedad :

    # primerPaciente = True
    # for paciente in range(numPacientes):
    #
    #     placeFound = False
    #     nombre = random.choice(nombres)
    #     numClinica = random.randint(100, 999)
    #     dateLastVisit = random.randint(1, 365)
    #     codeEnfermedad = random.randint(0, 10)
    #
    #     if primerPaciente:
    #         vector.append(Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad))
    #         primerPaciente = False
    #
    #     else:
    #         izq = 0
    #         der = len(vector)
    #         centre = der // 2
    #         while izq < der:
    #             # izq = 0
    #             # der = len(vector)
    #             # centre = der // 2
    #             centre = (izq + der) // 2
    #
    #             if vector[centre].numClinica > numClinica:
    #                 # izq = 0
    #                 der = centre
    #                 # centre = der // 2
    #                 #
    #                 # if der == izq:
    #                 #     vector[centre:centre] = [Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad)]
    #                 #     placeFound = True
    #
    #
    #             elif vector[centre].numClinica < numClinica:
    #                 izq = centre + 1
    #                 # der = len(vector)
    #                 # centre = der // 2
    #                 #
    #                 # if izq == der:
    #                 #     vector[centre:centre] = [Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad)]
    #                 #     placeFound = True
    #
    #             elif vector[centre].numClinica == numClinica:
    #                 vector[centre:centre] = [Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad)]
    #                 # placeFound = True
    #                 break
    #             else:
    #                 print("wtf")
    #
    #         vector[izq:izq] = [Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad)]
    #
    for paciente in range(numPacientes):
        nombre = random.choice(nombres)
        numClinica = random.randint(100, 999)
        dateLastVisit = random.randint(1, 365)
        codeEnfermedad = random.randint(0, 10)

        izq = 0
        der = len(vector)
        while izq < der:
            centre = (izq + der) // 2
            if vector[centre].numClinica < numClinica:
                izq = centre + 1
            else:
                der = centre

        vector[izq:izq] = [Paciente(nombre, numClinica, dateLastVisit, codeEnfermedad)]
    return vector



def mostrar_arreglo(vector):
    for i in range(len(vector)):
        print(vector[i])



def arreglo_d_dias(pacientesVector):

    vector_d_dias = []
    dia = int(input("dia interesado: "))
    for paciente in range(len(pacientesVector)):
        if pacientesVector[paciente].dateLastVisit >= dia:
            vector_d_dias.append(pacientesVector[paciente])

    return vector_d_dias

def encontrar_paciente(pacientesVector):
    x = int(input("paciente interesado: "))
    for paciente in range(len(pacientesVector)):
        if pacientesVector[paciente].numClinica == x:
            print("paciente: ", pacientesVector[paciente])
            return True
    # else:
    return False

def main():
    pacientesVector, vector_d_dias = None, None
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

        elif response == 2:
            if pacientesVector:
                vector_d_dias = arreglo_d_dias(pacientesVector)
                mostrar_arreglo(vector_d_dias)

        elif response == 3:
            if pacientesVector:
                paciente_encontrado = encontrar_paciente(pacientesVector)


                if not paciente_encontrado:
                    print("dar un mensaje de error")


if __name__ == "__main__":
    main()

