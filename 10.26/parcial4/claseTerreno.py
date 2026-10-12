class Lote:

    def __init__(self, nombre, numManzana, numLote, orientacion, superficie, monto):
        self.nombre = nombre
        self.numManzana = numManzana
        self.numLote = numLote
        self.orientacion = orientacion
        self.superficie = superficie
        self.monto = monto


    def __str__(self):
        r = "{:<30}".format("propietario: " + self.nombre)
        r += "{:<30}".format("número de manzana: " + str(self.numManzana))
        r += "{:<30}".format("número de lote : " + str(self.numLote))
        r += "{:<30}".format("orient del terreno: " + str(self.change_orientacion()))
        r += "{:<30}".format("superficie: " + str(self.superficie))
        r += "{:<30}".format("monto se vendió: " + str(self.monto))

        return r

    def change_orientacion(self):

        orientacion_code = [1, 2, 3, 4]
        orientacion_name = ["Norte", "Sur", "Este", "Oeste"]

        for side in range(1, 5):
            if self.orientacion == side:
                return orientacion_name[side - 1]



        # if self.orientacion == 1:
        #     return orientacion_name[0]
        # elif self.orientacion == 2:
        #     return orientacion_name[1]





