class Ticket:

    def __init__(self, codigo, pasajero, paisDestino, numeroAsiento, importe):
        self.codigo = codigo
        self.pasajero = pasajero
        self.paisDestino = paisDestino
        self.numeroAsiento = numeroAsiento
        self.importe = importe

    def __str__(self):
        r = '{:^30}' .format("el código del vuelo: " + str(self.codigo))
        r += '{:^30}' .format("identificación del pasajero: " + str(self.pasajero))
        r += '{:^30}' .format(" país de destino: " + str(self.paisDestino))
        r += '{:^30}' .format("numero de asiento: " + str(self.numeroAsiento))
        r += '{:30}' .format("importe pagado: " + str(self.importe) )

        return r
