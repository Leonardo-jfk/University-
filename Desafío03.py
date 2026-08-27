

# longitud del primer sector (recursiva)
def longitud_primer_sector(text):
    firstCode = True
    cadenaLength = len(text)
    oldCar, countSector = "", 0
    # print(text, cadenaLength)

    if cadenaLength <= 1:
        return cadenaLength

    if text[0] == text[1]:
        countSector += 1
        return 1 + longitud_primer_sector(text[1:])
    else:
        return 1 + countSector

# 1.) Si la longitud de t es 0 o 1 retornar esa longitud y terminar.
# 2.) Si los dos primeros caracteres de t son iguales:
# 2.1.) Retornar 1 + la longitud del primer sector de t pero sin incluir el primer caracter.
# 3.) Retornar 1 si llegó hasta aquí.

# conteo de sectores (recursiva)
def contar_sectores(text):

        cadenaLength = len(text)
        countAllSectors = 0
        if cadenaLength <= 1:
            return cadenaLength

        if text[0] != text[1]:
            # countSector += 1
            countAllSectors = 1 + contar_sectores(text[1:])
            return countAllSectors
        return contar_sectores(text[1:])



# 1.) Si la longitud de t es 0 o 1 retornar esa longitud y terminar.
# 2.) Si los dos primeros caracteres de t son diferentes:
# 2.1.) Retornar 1 + la cantidad de sectores de t pero sin incluir el primer caracter.
# 3.) Retornar la cantidad de sectores de t pero sin incluir el primer caracter si llegó hasta aquí.


# longitud del sector más largo (recursiva)
def mayor_longitud(text):

    cadenaLength = len(text)
    countAllSectors, count1Sector, n = 0, 0, 1
    if cadenaLength <= 1:
        return cadenaLength

    n = longitud_primer_sector(text)
    mayorSector = mayor_longitud(text[n:])
    if mayorSector < n:
        return n
    else:
        return mayorSector

# 1.) Si la longitud de t es O retornar 0 y terminar.
# 2.) Sea n la longitud del primer sector de t.
# 3.) Retornar el mayor entre n y la mayor longitud en t pero sin incluir el primer

def main():
    with open("copia.txt", "r") as file:

        cadenaCheck = file.read()
    file.close()
    # cadenaCheck = "AAABBBCCCCCCCCBAAADD"

    # if longitud_primer_sector(cadenaCheck):
    print("Longitud del primer sector: ", longitud_primer_sector(cadenaCheck))
    print("Cantidad de sectores: ", contar_sectores(cadenaCheck))
    print("El sector más largo: ", mayor_longitud(cadenaCheck))

    # print("3er", mayor_longitud(cadenaCheck))


if __name__ == '__main__':
    main()