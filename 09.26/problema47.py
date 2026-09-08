# Problema 47.) Se desea almacenar en un arreglo la información de los n estudiantes que se
# registraron para participar de un curso de programación. Por cada estudiante se tiene su
# número de legajo, su nombre y su promedio en la carrera que cursa. Participarán del curso
# los estudiantes cuyo promedio sea mayor o igual a x, siendo x un valor cargado por teclado.
# Muestre los datos de los estudiantes que participarán del curso, pero ordenados de menor a
# mayor por número de legajo.

import random

class Estudiante:
    def __init__(self, nombre, legajo, promedio):
        self.nombre = nombre
        self.legajo = legajo
        self.promedio = promedio

    def __str__(self):
        # return "Nombre: " + self.nombre + " - legajo: " + str(self.legajo) + " - promedio: " + str(self.promedio)
        # return 'Legajo: ' + str(self.legajo) + ' - Nombre: ' + self.nombre + ' - Promedio: ' + str(self.promedio)
        r = '{:^30}' .format("Nombre: " + self.nombre)
        r += '{:^30}' .format("Legajo: " + str(self.legajo))
        r += '{:^30}' .format("Promedio: " + str(self.promedio))
        return r



def ordenar(estudiantes):
    num = len(estudiantes)
    for i in range(num - 1):
        for j in range(i + 1, num):
            if estudiantes[i].legajo > estudiantes[j].legajo:
                estudiantes[i], estudiantes[j] = estudiantes[j], estudiantes[i]


def checkMin(estudiantes):
    num = len(estudiantes)
    x = int(input("min promedio: "))
    estudiantesAprobados = list()

    for i in range(num):
        if estudiantes[i].promedio > x:
            # estudiantes.append(estudiantesAprobados)
            estudiantesAprobados.append(estudiantes[i])
    # print(estudiantesAprobados)

    for i in range(len(estudiantesAprobados) - 1):
        for j in range(i + 1, len(estudiantesAprobados)):
            if estudiantesAprobados[i].legajo > estudiantesAprobados[j].legajo:
                estudiantesAprobados[i], estudiantesAprobados[j] = estudiantesAprobados[j], estudiantesAprobados[i]

    return estudiantesAprobados

def main():
    x = int(input("Ingrese la cantidad de estudiantes: "))
    estudiantes = x * [None]
    nombres = [ "alice", "bob", "charlie", "david", "alex", "hugo" ]
    # legajos = [ random.randint(1000, 10000) for i in range(x) ]
    # promedios = [ float(random.randint(1, 10)) for i in range(x) ]
    promedio = 0.0
    legajo = 0


    start = -1
    while start != 0:
        print("Opciones:")
        print("0. salir")
        print("1. mostrar estudiantes ")
        print("2. crear arreglo")
        print("3. ordenar")
        print("4. check who go")

        # a, b = 2, 44
        # cad = 'La suma de {0} + {1} es {2}'.format(a, b, a + b)
        # print(cad)
        # cad1 = '{:<5}'.format("gggggggggggggggg")
        # print(cad1)
        #
        start = int(input("Ingrese la deseada: "))
        if start == 1:
            for i in range(x):
                print(estudiantes[i])
        if start == 2:
            for i in range(len(estudiantes)):
                nombre = random.choice(nombres)
                legajo = random.randint(1000, 10000)
                promedio = random.randint(1, 10)
                estudiantes[i] = Estudiante(nombre, legajo, promedio)
                print(estudiantes[i])

        if start == 3:
            ordenar(estudiantes)

        if start == 4:
            if estudiantes != x * [None]:
                estudiantesAprobados = checkMin(estudiantes)
                for i in range(len(estudiantesAprobados)):
                    print(estudiantesAprobados[i])
            else:
                print("No hay estudiantes, go to option 2")




if __name__ == "__main__":
    main()




