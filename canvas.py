
import math
class Point:
    pass
    def init(self, cx, cy, desc='p'):
        p = Point()
        p.x = cx
        p.y = cy
        p.descripcion = desc
        return p
    def to_string(p):
        r = str(p.descripcion) + '(' + str(p.x) + ', ' + str(p.y) + ')'
        return r


def distance(p):
# Pitágoras...
    return math.sqrt(pow(p.x, 2) + pow(p.y, 2))
def gradient(p1, p2):
# calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x
    # si los puntos no son colineales verticales,
    # retornar la pendiente...
    if dx != 0:
        return dy / dx
# de otro modo, la pendiente es indefinida...
# ... este retorno debería ser controlado al regresar...`~
    return None