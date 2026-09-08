class Servicio:

    def __init__(self, codeIdent, name, typeOfServicio, importe):
        self.codeIdent = codeIdent
        self.name = name
        self.typeOfServicio = typeOfServicio
        self.importe = importe

    def __str__(self):

        r = '{:^30}' .format("código identificatorio: " + str(self.codeIdent))
        r += '{:^30}'.format("nombre del cliente: " + self.name)
        r += '{:^30}'.format("tipo de servicio: " + str(self.typeOfServicio))
        r += '{:^30}'.format(" importe a pagar: " + str(self.importe))

        return r

