class Ticket:
    def __init__(self, vue, pas, pai, asi, imp):
        self.vuelo = vue
        self.pasajero = pas
        self.pais = pai
        self.asiento = asi
        self.importe = imp

    def __str__(self):
        r = ""
        r = "{:<17}".format("Vuelo: " + self.vuelo)
        r += "{:<20}".format(" - Pasajero: " + str(self.pasajero))
        r += "{:<20}".format(" - País destino: " + str(self.pais))
        r += "{:<17}".format(" - Asiento: " + str(self.asiento))
        r += "{:<17}".format(" - Importe: " + str(self.importe))
        return r
