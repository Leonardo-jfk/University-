class Publicacion:
    def __init__(self, cod, tit, tip, cos):
        self.codigo = cod
        self.titulo = tit
        self.tipo = tip
        self.costo = cos

    def __str__(self):
        r = ""
        r = "{:<18}".format("Código: " + self.codigo)
        r += "{:<40}".format(" - Título: " + self.titulo)
        r += "{:<13}".format(" - Tipo: " + str(self.tipo))
        r += "{:<17}".format(" - Costo: " + str(self.costo))
        return r
