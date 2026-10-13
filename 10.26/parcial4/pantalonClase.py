class Pantalon:

    def __init__(self, codigo, modelo, largo, cintura, tela, stock):
        self.codigo = codigo
        self.modelo = modelo
        self.largo = largo
        self.cintura = cintura
        self.tela = tela
        self.stock = stock



    def __str__(self):
        r = "{:<30}".format("código de producto: " + str(self.codigo))
        r += "{:<30}".format("nombre del modelo: " + str(self.modelo))
        r += "{:<30}".format("talle de largo: " + str(self.largo))
        r += "{:<30}".format("talle de cintura : " + str(self.cintura))
        r += "{:<30}".format("tipo de tela: " + str(self.changeTipo()))
        r += "{:<30}".format("stock: " + str(self.stock))

        return r

    def changeTipo(self):
        # telaCode = random.randint(1, 3)
        telaNames = ["Jean", "Gabardina", "Denim"]

        for i in range(3):
            if self.tela - 1 == i:
                return telaNames[i]
