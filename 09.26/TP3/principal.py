

import os
import ClasePrincipal


def cargar_tratamientos(filename):
    vector = []
    if not os.path.exists(filename):
        return vector

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

            t = ClasePrincipal.Tratamiento(dni, nombre, apellido, icd10, monto_base, complejidad, id_alg)
            vector.append(t)

    archivo.close()
    return vector


def procesar_opcion_1(vector):
    # r1.1: Cantidad de tratamientos cargados
    respuesta1 = len(vector)
    print("r1.1:", respuesta1)

    # r1.2: Apellido del quinto tratamiento de alta complejidad
    contador_a = 0
    respuesta2 = "No hay suficientes tratamientos de alta complejidad."

    for t in vector:
        if t.complejidad == 'A':
            contador_a += 1
            if contador_a == 5:
                # El apellido del paciente del quinto tratamiento
                respuesta2 = t.apellido
                break


    print("r1.2: ", respuesta2)


def procesar_opcion_2(vector):
    if len(vector) == 0:
        return

    # r2.1: Diferencia promedio entre monto final y base
    suma_diferencia = 0
    for trat in vector:
        suma_diferencia += (trat.calcular_monto_final() - trat.monto_base)
    r2_1 = suma_diferencia / len(vector)

    # r2.2 y r2.3: Letra con mayor cantidad de tratamientos (usando arreglos simples sin diccionarios)

    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    conteos_letras = [0] * 26

    for trat in vector:
        letra_paciente = trat.icd10[0].upper()

        for i in range(26):
            if abecedario[i] == letra_paciente:
                conteos_letras[i] += 1
                break

    max_conteo = -1
    letra_mayor = ""

    for i in range(26):
        if conteos_letras[i] > max_conteo:
            max_conteo = conteos_letras[i]
            letra_mayor = abecedario[i]

    r2_2 = letra_mayor
    r2_3 = max_conteo



    # r2.4: DNI del tratamiento de mayor monto final entre los de alta complejidad
    mayor_monto = -1
    dni_mayor = -1

    for trat in vector:
        if trat.complejidad == 'A':
            monto_final = trat.calcular_monto_final()
            if monto_final > mayor_monto:
                mayor_monto = monto_final
                dni_mayor = trat.dni

    # r2_4 = dni_mayor if dni_mayor != -1 else "No hay tratamientos de alta complejidad."
    if dni_mayor != -1:
        r2_4 = dni_mayor
    else:
        r2_4 = "No hay tratamientos de alta complejidad."

    print("r.2.1:", round(r2_1, 2))
    print("r.2.2:", r2_2)
    print("r.2.3:", r2_3)
    print("r.2.4:", r2_4)


def principal():
    vector = []
    opcion = -1

    while opcion != 0:
        opcion = int(input("Ingrese opción: "))

        if opcion == 1:
            vector = cargar_tratamientos("tratamientos.csv")
            # vector = cargar_tratamientos("tratTest.csv")


            procesar_opcion_1(vector)

        if opcion == 2:
            if vector:
                procesar_opcion_2(vector)
            else:
                print("No has creado un arreglo de tratamientos, vaya a la 1ra opcion")

    print("Terminamos el trabajo! ")

if __name__ == "__main__":
    principal()