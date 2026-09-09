class Publicacion:

    def __init__(self, codigo, titulo, tipo, costo ):
        self.codigo = codigo
        self.titulo = titulo
        self.tipo = tipo
        self.costo = costo


    def __str__(self):
        r = '{:<30}'. format("código de ide: " + self.codigo)
        r += '{:<30}'. format(" - título de pub: " + self.titulo)
        r += '{:30}'. format(" - tipo pub: " + str(self.tipo))
        r += '{:<30}'. format(" - costo de prod: " + str(self.costo))
        return r