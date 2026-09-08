class Juicio:

    def __init__(self, codeExp, descripcion, type, nomClient, monto):
        self.codeExp = codeExp
        self.descripcion = descripcion
        self.type = type
        self.nomClient = nomClient
        self.monto = monto

    def __str__(self):

        r = '{:<30}' .format("código de expediente: " + str(self.codeExp))
        r += '{:<30}' .format("carátula del juicio: " + self.descripcion)
        r += '{:<30}' .format("tipo de juicio: " + str(self.type))
        r += '{:<30}' .format("nombre: " + self.nomClient)
        r += '{:<30}' .format("monto a cobrar: " + str(self.monto))
        return r
