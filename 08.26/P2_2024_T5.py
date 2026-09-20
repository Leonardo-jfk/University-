def leer_archivo(nombre_archivo):
    m = open(nombre_archivo, 'rt')
    texto = m.read()
    m.close()
    return texto


def es_mayuscula(car):
    return 'A' <= car <= 'Z' or car == 'Ñ' or car in 'ÁÉÍÓÚÄËÏÖÜ'


def es_consonante(car):
    return car.lower() in 'qwrtypsdfghjklñzxcvbnm'


def es_vocal(car):
    return car.lower() in 'aeiouáéíóúäëïöü'


def calcular_promedio(acumulador, contador):
    promedio = 0
    if contador != 0:
        promedio = acumulador // contador
    return promedio


def principal():
    texto = leer_archivo('entrada.txt')

    # Creación de variables
    c_caracteres = c_cons = 0
    tiene_mayuscula = ultimo_digito = tiene_impar = empieza_vocal = False
    b = tiene_ba = tiene_t = False

    # Variables intermedias no reiniciables
    c_pp3 = a_pp3 = 0

    # Variables finales
    r1 = r3 = r4 = 0
    r2 = None

    # x4g5

    for car in texto:
        if car != ' ' and car != '.':
            # Adentro de la palabra
            c_caracteres += 1

            # r1
            if es_mayuscula(car):
                tiene_mayuscula = True

            if car in '1234567890':
                ultimo_digito = True
            else:
                ultimo_digito = False

            # r2
            if car in '13579':
                tiene_impar = True

            # r3
            if es_vocal(car) and c_caracteres == 1:
                empieza_vocal = True
            elif es_consonante(car):
                c_cons += 1

            # r4
            if car in 'bB':
                b = True
            elif b:
                if car.lower() in 'aáä':
                    tiene_ba = True

                b = False

            if car in 'tT':
                tiene_t = True
        else:
            # Afuera de la palabra

            # r1
            if not tiene_mayuscula and ultimo_digito:
                r1 += 1

            # r2
            if tiene_impar:
                if r2 is None or c_caracteres > r2:
                    r2 = c_caracteres

            # r3
            if empieza_vocal and c_cons >= 3:
                c_pp3 += 1
                a_pp3 += c_caracteres

            # r4
            if tiene_ba and not tiene_t:
                r4 += 1


            # Reinicio de variables
            c_caracteres = c_cons = 0
            tiene_mayuscula = ultimo_digito = tiene_impar = False
            empieza_vocal = b = tiene_ba = tiene_t = False
            pos_sec = 0

    # Cálculo de porcentajes y promedios
    # Promedio -> acumulador / contador
    # Porcentaje -> c_parcial * 100 / c_total
    r3 = calcular_promedio(a_pp3, c_pp3)

    # Muestra de resultados

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    principal()
