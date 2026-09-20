class Alumno:
    def __init__(self, leg, nom, pro):
        self.legajo = leg
        self.nombre = nom
        self.promedio = pro

    def __str__(self):
        return "Legajo: " + str(self.legajo) + \
               " Nombre: " + self.nombre + \
               " Promedio: " + str(self.promedio)

def prueba():
    a1 = Alumno(10, 'Juan', 9)
    print(a1)

if __name__ == '__main__':
    prueba()