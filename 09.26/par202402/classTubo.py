class Tubo:

    def __init__(self, codigo, diameter, type, weight, ignifugo ):
        self.codigo = codigo
        self.diameter = diameter
        self.type = type
        self.weight = weight
        self.ignifugo = ignifugo



    def __str__(self):
        r = "{:<30}". format("código de producto: " + str(self.codigo))
        r += "{:<30}".format(" - diámetro en pulgadas: " + str(self.diameter))
        r += "{:<30}".format(" - tipo de aplicación: " + str(self.type))
        r += "{:<30}".format(" - cantidad de gramos: " + str(self.weight))
        r += "{:<30}".format(" - es ignífugo o no : " + str(self.ignifugo))

        return r