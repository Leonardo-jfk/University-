class Servicio:
    def __init__(self, vue, pas, pai, imp):
        self.codigo = vue
        self.nombre = pas
        self.tipo = pai
        self.importe = imp

    def __str__(self):
        r = ""
        r = "{:<15}".format("Código: " + str(self.codigo))
        r += "{:<40}".format(" - Cliente: " + self.nombre)
        r += "{:<25}".format(" - Tipo de servicio: " + str(self.tipo))
        r += "{:<17}".format(" - Importe: " + str(self.importe))
        return r
