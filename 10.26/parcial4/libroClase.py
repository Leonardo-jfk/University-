class Libro:

    def __init__(self, ISBN, titulo, autor, idioma, precio):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.idioma = idioma
        self.precio = precio



    def __str__(self):
        r = "{:<30}".format("número ISBN: " + str(self.ISBN))
        r += "{:<30}".format("título: " + str(self.titulo))
        r += "{:<30}".format("autor: " + str(self.autor))
        r += "{:<30}".format(" idioma : " + str(self.austauchen()))
        r += "{:<30}".format("precio de venta: " + str(self.precio))

        return r

    def austauchen(self):

        idiomaText = ["Español", "Inglés", "Portugués", "Francés", "Italiano"]
        # idiomaCode = random.randint(1, 5)
        for lengua in range(5):
            if self.idioma - 1 == lengua:
                return idiomaText[lengua]