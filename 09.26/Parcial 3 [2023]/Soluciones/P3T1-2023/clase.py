class Empleo:
    def __init__(self, cid, des, tip, imp):
        self.identificador = cid
        self.descripcion = des
        self.tipo = tip
        self.importe = imp

    def __str__(self):
        r = ""
        r = "{:<20}".format("Identificador: " + str(self.identificador))
        r += "{:<35}".format(" - Descripción: " + self.descripcion)
        r += "{:<12}".format(" - Tipo: " + str(self.tipo))
        r += "{:<17}".format(" - Importe: " + str(self.importe))
        return r
