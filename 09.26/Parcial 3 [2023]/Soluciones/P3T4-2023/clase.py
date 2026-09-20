class Juicio:
    def __init__(self, exp, car, tip, nom, imp):
        self.expediente = exp
        self.caratula = car
        self.tipo = tip
        self.cliente = nom
        self.importe = imp

    def __str__(self):
        r = ""
        r = "{:<20}".format("Expediente: " + str(self.expediente))
        r += "{:<35}".format(" - Carátula: " + self.caratula)
        r += "{:<25}".format(" - Tipo de juicio: " + str(self.tipo))
        r += "{:<40}".format(" - Cliente: " + self.cliente)
        r += "{:<17}".format(" - Importe: " + str(self.importe))
        return r
