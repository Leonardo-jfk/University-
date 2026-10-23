import os
import clase

def cargar_tratamientos(filename):
    v = []

    archivo = open(filename, "rt")
    primer_linea = True

    for linea in archivo:
        if primer_linea:
            primer_linea = False
            continue

        linea = linea.strip()
        if linea == "":
            continue

        campos = linea.split(',')
        if len(campos) == 7:
            dni = campos[0].strip()
            nombre = campos[1].strip()
            apellido = campos[2].strip()
            icd10 = campos[3].strip()
            monto_base = campos[4].strip()
            complejidad = campos[5].strip()
            id_alg = campos[6].strip()

            t = clase.Tratamiento(dni, nombre, apellido, icd10, monto_base, complejidad, id_alg)
            v.append(t)

    archivo.close()
    return v


def cargar_afiliados(filename):
    v = []
    archivo = open(filename, "rt")
    primer_linea = True

    for linea in archivo:
        if primer_linea:
            primer_linea = False
            continue

        linea = linea.strip()
        if linea == "":
            continue
        campos = linea.split(',')
        if len(campos) == 4:
            dni = campos[0].strip()
            os = campos[1].strip()
            nivel = campos[2].strip()
            max = campos[3].strip()

            t = clase.afiliados(dni, os, nivel, max)
            m = pos = len(v)
            izq, der = 0, m - 1
            while izq <= der:
                c = (izq + der) // 2
                if t.dni == v[c].dni:
                    pos = c
                    break
                elif t.dni < v[c].dni:
                    der = c - 1
                else:
                    izq = c + 1
            if izq > der:
                pos = izq
            v[pos:pos] = [t]

    archivo.close()
    return v
def principal():
    vector = []
    opcion = -1

    while opcion != 0:
        opcion = int(input("Ingrese opción: "))

        if opcion == 1:
            v = cargar_tratamientos("tratamientos.csv")
            # vector = cargar_tratamientos("tratTest.csv")

        elif opcion == 2:
            v_afiliados = cargar_afiliados("coberturas.csv")

    print("Terminamos el trabajo! ")

if __name__ == "__main__":
    principal()