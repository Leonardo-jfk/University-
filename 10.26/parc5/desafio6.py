import os


class Pila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def __str__(self):
        return str(self.items)

def es_opuesto(apertura, cierre):
    opuestos = {'(': ')', '[': ']', '{': '}'}
    return opuestos.get(apertura) == cierre

def procesar_archivo(nombre_archivo):


    import os

def procesar_archivo(nombre_archivo):
    # On vérifie l'existence avant d'essayer d'ouvrir
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                            expresion = linea.strip()
                            if not expresion:
                                continue
                            
                            pila = Pila()
                            cola = Cola()
                            estado = "Ok"
                            
                            # Segunda parte del pseudocódigo: recolectar los símbolos en el orden original
                            for s in expresion:
                                if s in "()[]{}":
                                    cola.enqueue(s)
                            
                            # Primera parte del pseudocódigo: verificar el equilibrio
                            for s in expresion:
                                if s in "([{":
                                    pila.push(s)
                                elif s in ")]}":
                                    if pila.is_empty():
                                        estado = "Sobran cierres"
                                        break
                                    else:
                                        ps = pila.pop()
                                        if not es_opuesto(ps, s):
                                            estado = "Desequilibrio interno"
                                            break
                            
                            # Si el ciclo terminó sin errores pero quedaron aperturas sin cerrar
                            if estado == "Ok" and not pila.is_empty():
                                estado = "Sobran aperturas"
            
                            # Mostrar los resultados requeridos
                            print(f"Estado: {estado}")
                            print(f"Símbolos procesados: {cola}")
                            print("-" * 40)
                
    else:
        # Si le fichier n'existe pas, on affiche l'erreur directement
        print(f"Error: No se encontró el archivo '{nombre_archivo}'. Asegúrese de que esté en la misma carpeta.")

if __name__ == "__main__":
    procesar_archivo("expresiones.txt")