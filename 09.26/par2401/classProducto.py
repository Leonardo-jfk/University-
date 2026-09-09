class Producto:

    def __init__(self, codigo, description, calories, type, price ):
        self.codigo = codigo
        self.description = description
        self.calories = calories
        self.type = type
        self.price = price


    def __str__(self):
        r = '{:<30}'. format( "código de prod: " + str(self.codigo))
        r += '{:<30}'. format(" - descripción del prod: " + str(self.description))
        r += '{:<30}'.format(" - cant de calorías: " + str(self.calories))
        r += '{:<30}'.format(" - tipo de producto: " + str(self.type))
        r += '{:<30}'.format(" - price del producto: " + str(self.price))

        return r