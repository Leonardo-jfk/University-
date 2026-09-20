class Servicio:
    def __init__(self, codigo, cliente, tipo, importe):
        self.codigo = codigo
        self.cliente = cliente
        self.tipo = tipo
        self.importe = importe

    def __str__(self):
        res = "Código: " + str(self.codigo) + " Cliente: " + \
               str(self.cliente) + " Tipo: " + str(self.tipo) + \
               " Importe: " + str(self.importe)
        return res