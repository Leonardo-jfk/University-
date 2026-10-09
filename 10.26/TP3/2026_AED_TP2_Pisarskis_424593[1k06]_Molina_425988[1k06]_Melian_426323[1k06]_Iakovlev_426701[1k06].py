def prints(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10,r11):
    print('(r1) - Cantidad de tratamientos cargados:', r1)
    print('(r2) - Cantidad de tratamientos "A":', r2)
    print('(r3) - Cantidad de tratamientos "B":', r3)
    print('(r4) - Cantidad de tratamientos "C":', r4)
    print('(r5) - Cantidad de tratamientos "E":', r5)
    print('(r6) - Cantidad de tratamientos "P":', r6)
    print('(r7) – Importe final promedio (capítulo 19):', r7)
    print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final:', r8)
    print('(r9) - Mayor importe pagado por ese paciente:', r9)
    print(
        '(r10)- Porcentaje de tratamientos de alta complejidad '
        'con coste mayor al promedio:', r10
    )
def tiene_h(codigo):
    for i in codigo:
        if i.upper == "H":
            bandera = True
    return bandera
#def segundo(codigo,bandera,nombre,menor):
    if bandera :
        fcodigo=codigo[1:3]
        if int(fcodigo) < menor:
            nombremenor= nombre
            menor=int(fcodigo)
        else:
            bandera = False

            
    return(bandera, nombremenor, menor)

def principal():
    archivo = open("tratamientos.txt", "r")
    menor=100
    r1, r2, r3, r4, r5, r6, r7 = 0, 0, 0, 0, 0, 0, 0
    r10 = 0
    r8 =  ""
    r9 = -1
    bandera=False
    acummontos_st, contador_st, acummontos, base = 0, 0, 0, 0
    mayorespro, monto_u, contador_alta, porcentaje = 0, 0, 0, 0
    base, mayprom, costes, codigo, nombre = "", "", "", "", ""

    # hay que cambiar por readline
    linea = archivo.readline()

    monto_a_l = 0
    monto_m_z = 0

    while linea != "":

        # for linea in lineas:
        if linea[0] == "#":
            monto_a_l = int(linea[2:8])
            monto_m_z = int(linea[8:14])
            monto_u = int(linea[14:20])
        else:
            r1 += 1
            cespacio = 0
            linea1 = linea[0:25]
            nombre = ""
            for l in linea1:
                if cespacio <= 1:
                    nombre += l
                if l == " ":
                    cespacio += 1
            nombre = linea[0:25]

            # while nombre[-1] == ' ':
            #     nombre = nombre[:-1]

            linea2 = linea[25:31]
            codigo = ""
            for l in linea2:
                if l != " ":
                    codigo += l
                if l == " ":
                    codigo += " "
            if codigo[-1] == " ":
                porcentaje = int(codigo[-2])


            else:
                porcentaje = int(codigo[-2:])

            linea3 = linea[31:39]
            base = ""
            for i in linea3:
                if i != " ":
                    base += i

            if "A" <= linea[25] <= "L":
                monto = monto_a_l + int(base)
            elif "M" <= linea[25] <= "Z" and linea[25] != "U":
                monto = monto_m_z + int(base)
            else:
                monto = monto_u + int(base)
            montofinal = monto + (monto * porcentaje / 100)

            # if len(linea) == 41:
            if linea[39] == "X" and len(linea) > 39:
                montofinal1 = montofinal + (montofinal * 5 / 100)
                # montofinal *= 1.05
                contador_alta += 1
            else:
                montofinal1 = montofinal

            if (linea[25] == "S" or linea[25] == "T") and linea[0] != "#":
                acummontos_st += montofinal1
                contador_st += 1
            acummontos += montofinal1
            if montofinal1 > r9 and linea[25] != "U":
                r9 = round(montofinal1, 2)
                r8 = nombre
            if linea[25] == "A":
                r2 += 1
            if linea[25] == "B":
                r3 += 1
            if linea[25] == "C":
                r4 += 1
            if linea[25] == "E":
                r5 += 1
            if linea[25] == "P":
                r6 += 1
            
            if bandera :
                fcodigo=codigo[1:3]
                if int(fcodigo) < menor:
                    nombremenor= nombre
                    menor=int(fcodigo)
                else:
                    bandera = False
            for i in codigo:
                if i.upper == "H":
                    bandera = True
            r11=nombremenor
                    
    
            
        linea = archivo.readline()


    archivo.close()
    if contador_st != 0:
        r7 = acummontos_st // contador_st
    if r1 != 0:
        promedio = acummontos / r1

    archivo = open("tratamientos.txt", "r")
    linea = archivo.readline()

    while linea != "":
        if len(linea) > 39 and linea[39] == "X":
            if linea[0] == "#":
                monto_a_l = int(linea[2:8])
                monto_m_z = int(linea[8:14])
                monto_u = int(linea[14:20])
            else:
                linea3 = linea[31:39]
                numbase = False
                base = ""
                for l in linea3:
                    if l != " " or numbase:
                        base += l
                        numbase = True
                linea2 = linea[25:31]
                codigo = ""
                for l in linea2:
                    if l != " ":
                        codigo += l
                    if l == " ":
                        codigo += "0"
                if codigo[-1] == "0":
                    porcentaje = int(codigo[-2])
                else:
                    porcentaje = int(codigo[-2:])

                if "A" <= linea[25] <= "L":
                    monto = monto_a_l + int(base)
                elif "M" <= linea[25] <= "Z" and linea[25] != "U":
                    monto = monto_m_z + int(base)
                else:
                    monto = monto_u + int(base)

                montofinal = monto + (monto * (porcentaje / 100))
                montofinal1 = montofinal + (montofinal * 5 / 100)
                # montofinal *= 1.05

                if montofinal1 > promedio:
                    mayorespro += 1



        linea = archivo.readline()

    archivo.close()


   
    r11=nombremenor
    if contador_alta != 0:
        r10 = int((mayorespro / contador_alta) * 100)

    prints(r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11)

principal()