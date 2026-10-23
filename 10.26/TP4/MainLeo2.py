import os
import ClassLeo2

def insertar_ordenado_afiliado(v, afiliado):
    izq, der = 0, len(v) - 1
    pos = len(v)
    while izq <= der:
        c = (izq + der) // 2
        if v[c].dni == afiliado.dni:
            pos = c
            break
        if afiliado.dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [afiliado]

def busqueda_binaria_afiliado(v, dni):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].dni == dni:
            return v[c]
        if dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1
    return None

def cargar_afiliados(filename):
    v = []
    if not os.path.exists(filename):
        return v
    
    archivo = open(filename, "rt")
    primer_linea = True
    
    for linea in archivo:
        if primer_linea:
            primer_linea = False
            continue
            
        campos = linea.strip().split(',')
        if len(campos) == 4:
            a = ClassLeo2.Afiliado(campos[0], campos[1], campos[2], campos[3])
            insertar_ordenado_afiliado(v, a)
            
    archivo.close()
    return v

def cargar_tratamientos(filename):
    v = []
    if not os.path.exists(filename):
        return v
        
    archivo = open(filename, "rt")
    primer_linea = True
    
    for linea in archivo:
        if primer_linea:
            primer_linea = False
            continue
            
        campos = linea.strip().split(',')
        if len(campos) == 7:
            t = ClassLeo2.Tratamiento(campos[0], campos[1], campos[2], campos[3], campos[4], campos[5], campos[6])
            v.append(t)
            
    archivo.close()
    return v

def obtener_porcentaje_cobertura(nivel, complejidad):
    if nivel == 1:
        if complejidad == 'R': return 0.50
        elif complejidad == 'A': return 0.40
    elif nivel == 2:
        if complejidad == 'R': return 0.70
        elif complejidad == 'A': return 0.60
    elif nivel == 3:
        if complejidad == 'R': return 0.90
        elif complejidad == 'A': return 0.80
    return 0.0

def mostrar_resultados(afiliados, tratamientos):
    if len(afiliados) == 0 or len(tratamientos) == 0:
        print("Error: Primero debe cargar los afiliados y tratamientos.")
        return

    total_cubierto = 0.0
    total_no_cubierto = 0.0
    tope_aplicado_count = 0
    no_afiliados_count = 0
    
    # Arreglo para almacenar lo cubierto por cada OS (índices 1 al 20)
    acumuladores_os = [0.0] * 21
    
    mayor_monto_no_cubierto = -1.0
    dni_mayor_monto_no_cubierto = -1

    for t in tratamientos:
        monto_final = t.calcular_monto_final()
        afiliado = busqueda_binaria_afiliado(afiliados, t.dni)
        monto_cubierto = 0.0
        
        if afiliado is None:
            no_afiliados_count += 1
            monto_cubierto = 0.0
        else:
            porcentaje = obtener_porcentaje_cobertura(afiliado.nivel, t.complejidad)
            monto_cubierto = monto_final * porcentaje
            
            if monto_cubierto > afiliado.tope:
                monto_cubierto = afiliado.tope
                tope_aplicado_count += 1
                
            acumuladores_os[afiliado.cod_os] += monto_cubierto
            
        monto_no_cubierto = monto_final - monto_cubierto
        
        total_cubierto += monto_cubierto
        total_no_cubierto += monto_no_cubierto
        
        # Guardar paciente con mayor monto no cubierto
        if monto_no_cubierto > mayor_monto_no_cubierto:
            mayor_monto_no_cubierto = monto_no_cubierto
            dni_mayor_monto_no_cubierto = t.dni

    # Buscar la Obra Social (OS) que cubrió más monto
    max_os_monto = -1.0
    max_os_codigo = -1
    for i in range(1, 21):
        if acumuladores_os[i] > max_os_monto:
            max_os_monto = acumuladores_os[i]
            max_os_codigo = i

    print("r3.1:", round(total_cubierto, 2))
    print("r3.2:", round(total_no_cubierto, 2))
    print("r3.3:", tope_aplicado_count)
    print("r3.4:", no_afiliados_count)
    print("r3.5:", max_os_codigo)
    print("r3.6:", dni_mayor_monto_no_cubierto)

def principal():
    afiliados = []
    tratamientos = []
    opcion = -1

    while opcion != 0:
        print("1. Cargar afiliados")
        print("2. Cargar tratamientos")
        print("3. Mostrar resultados")
        print("0. Salir")
        opcion = int(input("Ingrese opción: "))

        if opcion == 1:
            afiliados = cargar_afiliados("coberturas.csv")
        elif opcion == 2:
            tratamientos = cargar_tratamientos("tratamientos.csv")
        elif opcion == 3:
            mostrar_resultados(afiliados, tratamientos)

if __name__ == "__main__":
    principal()