def es_digito(car):
    return car in "0123456789"

def es_mayuscula(car):
    return car in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"

def es_consonante(car):
    return car.lower() in "qwrtypsdfghjklñzxcvbnm"

def principal():
    #Contadores...
    r1, r2, r3, r4 = 0, 0, 0, 0
    cl, cc, parcial, total = 0, 0, 0, 0
    mayus, impar, vocal, ba, t = False, False, False, False, False
    ant = ""


    #archivo = open("entrada.txt")
    #texto = archivo.read()
    #archivo.close()
    texto = "El ancho de bastos es banca y pasaba el Beagle y Santa Barbara."

    for car in texto:
        #DENTRO de la palabra:
        if car not in " .":
            cl += 1

            #1)
            if es_mayuscula(car):
                mayus = True

            #2)
            if es_digito(car) and int(car) % 2 != 0:
                impar = True

            #3)
            if cl == 1 and car.lower() in "aeiouáéíóú":
                vocal = True
            elif es_consonante(car):
                cc += 1

            #4)
            if car in "tT":
                t = True
            # elif car.lower() in "aá" and ant.lower() == "b":
            elif car.lower() in "aá" and ant in "bB":
                # print(ant, )
                ba = True

            ant = car

        #FUERA de la palabra:
        else:
            #1)
            if mayus == False and es_digito(ant):
                r1 += 1

            #2)
            if impar and cl > r2:
                r2 = cl

            #3)
            if vocal and cc >= 3:
                parcial += cl
                total += 1

            #4)
            if not t  and ba:
                r4 += 1

            #Reinicio contadores...
            cl, cc = 0, 0
            mayus, impar, vocal, ba, t = False, False, False, False, False
            ant = " "

    if total > 0:
        r3 = parcial // total
    else:
        r3 = 0

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == "__main__":
    principal()