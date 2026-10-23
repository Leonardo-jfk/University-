import os
import ClassLeo


def cargar_afiliados(nombre_archivo):
    v = []
    if not os.path.exists(nombre_archivo):
        return v

    archivo = open(nombre_archivo, "rt")
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
            afi = ClassLeo.Afiliado(campos[0].strip(), campos[1].strip(),
                                 campos[2].strip(), campos[3].strip())
            insertar_ordenado(v, afi)

    archivo.close()
    return v


def insertar_ordenado(v, afi):
    # Búsqueda binaria de la posición de inserción (vector ordenado por DNI)
    izq, der = 0, len(v) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if afi.dni == v[c].dni:
            pos = c
            break
        elif afi.dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [afi]


def buscar_afiliado(v, dni):
    # Búsqueda binaria por DNI: retorna el afiliado o None si no está
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if dni == v[c].dni:
            return v[c]
        elif dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1
    return None


def cargar_tratamientos(nombre_archivo):
    v = []
    if not os.path.exists(nombre_archivo):
        return v

    archivo = open(nombre_archivo, "rt")
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
            t = ClassLeo.Tratamiento(campos[0].strip(), campos[1].strip(), campos[2].strip(),
                                  campos[3].strip(), campos[4].strip(), campos[5].strip(),
                                  campos[6].strip())
            v.append(t)

    archivo.close()
    return v


def mostrar_resultados(afiliados, tratamientos):
    total_cubierto = 0.0
    total_no_cubierto = 0.0
    cant_topes = 0
    cant_sin_obra_social = 0

    # Acumulador de monto cubierto por obra social (códigos 1 a 20)
    cubierto_por_os = [0.0] * 21

    mayor_no_cubierto = -1
    dni_mayor_no_cubierto = -1

    for t in tratamientos:
        afi = buscar_afiliado(afiliados, t.dni)
        monto_final, cubierto, no_cubierto, tope = t.calcular_cobertura(afi)

        total_cubierto += cubierto
        total_no_cubierto += no_cubierto

        if tope:
            cant_topes += 1

        if afi is None:
            cant_sin_obra_social += 1
        else:
            cubierto_por_os[afi.obra_social] += cubierto

        if no_cubierto > mayor_no_cubierto:
            mayor_no_cubierto = no_cubierto
            dni_mayor_no_cubierto = t.dni

    # Obra social con mayor monto cubierto (empate: menor código)
    cod_mayor = -1
    mayor_cubierto = -1
    for cod in range(1, 21):
        if cubierto_por_os[cod] > mayor_cubierto:
            mayor_cubierto = cubierto_por_os[cod]
            cod_mayor = cod

    print("r3.1:", round(total_cubierto, 2))
    print("r3.2:", round(total_no_cubierto, 2))
    print("r3.3:", cant_topes)
    print("r3.4:", cant_sin_obra_social)
    print("r3.5:", cod_mayor)
    print("r3.6:", dni_mayor_no_cubierto)


def mostrar_menu():
    print("1. Cargar afiliados")
    print("2. Cargar tratamientos")
    print("3. Mostrar resultados")
    print("0. Salir")


def principal():
    afiliados = None
    tratamientos = None
    opcion = -1

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese opción: "))

        if opcion == 1:
            afiliados = cargar_afiliados("coberturas.csv")
            print("Afiliados cargados:", len(afiliados))

        elif opcion == 2:
            tratamientos = cargar_tratamientos("tratamientos.csv")
            print("Tratamientos cargados:", len(tratamientos))

        elif opcion == 3:
            if afiliados is None or tratamientos is None:
                print("Error: primero debe cargar los afiliados (opción 1) y los tratamientos (opción 2).")
            else:
                mostrar_resultados(afiliados, tratamientos)

        elif opcion != 0:
            print("Opción inválida.")


if __name__ == "__main__":
    principal()