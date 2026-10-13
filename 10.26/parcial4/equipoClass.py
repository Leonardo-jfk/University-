class Equipo:

    def __init__(self, numero, nombre, edad, nivel, precio):
        self.numero = numero
        self.nombre = nombre
        self.edad = edad
        self.nivel = nivel
        self.precio = precio



    def __str__(self):

        niveles = ["Bajo", "Intermedio", "Avanzado"]
        r = "{:<30}".format(" número de inscripción: " + str(self.numero))
        r += "{:<30}".format("nombre: " + str(self.nombre))
        r += "{:<30}".format("edad  de  sus  jugadores : " + str(self.edad))
        r += "{:<20}".format(" nivel  de  juego : " + str(self.nivel))
        r += "{:<10}".format(" (" + str(niveles[self.nivel]) + " ) ")
        r += "{:<30}".format("monto que pagaron: " + str(self.precio))

        return r