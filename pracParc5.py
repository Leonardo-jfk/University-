def file_opener(name):
    file = open(name, "r")
    archivo = file.read()
    file.close()
    return archivo

def car_checker(car, code):
    if code == "vocal":
        return car.lower() in "aeiouáéúíó"

    if code == "consonant":
        return not car.lower() in "aeiou" and car.isalpha()

    if code == "digit":
        return car.isdigit()

    if code == "letra":
        return car.isalpha()

    else:
        return False

def main():

    file_name = "entrada.txt"
    archivo = file_opener(file_name)
    count_car, count_words, last_car = 0, 0, ""
    r1, r2, r3, r4 = 0, 0, 0, 0
    start_with_letra, continue_with_digit, first_call, menor = False, False, True, float('inf')
    count_cons, count_voc, count_words, count_words_3er = 0, 0, 0, 0
    contain_tu, contain_b, contain_digit = False,  False, False


    for car in archivo:

        if car != " " and car != ".":
            count_car += 1

            #1er
            if car_checker(last_car, "letra") and car_checker(car, "letra"):
                start_with_letra = True
            if count_car >= 3 and start_with_letra:
                if car.isdigit():
                    aux_car = car
                    if int(aux_car) % 2 == 0:
                        continue_with_digit = True
                else:
                    continue_with_digit = False

            #3er
            if car_checker(car, "vocal"):
                count_voc += 1
            if car_checker(car, "consonant"):
                count_cons += 1



            # 4to
            if last_car.lower() == "t" and car.lower() == "u":
                contain_tu = True
            if car.lower() == "b":
                contain_b = True

            if car_checker(car, "digit"):
                contain_digit = True


            last_car = car

        else:

            # 1er
            if start_with_letra and continue_with_digit:
                r1 += 1



            # 2do
            if count_car > 3:

                if count_car < menor:
                    menor = count_car

            #3er
            if count_voc > count_cons:
                count_words_3er += 1

            #4to
            if not contain_b and not contain_digit and contain_tu:
                r4 += 1



            count_words += 1
            count_car, start_with_letra, continue_with_digit, first_call = 0, False, False, False
            count_cons, count_voc, contain_tu, contain_b, contain_digit = 0, 0, False, False, False


    r2 = menor
    r3 = (count_words_3er * 100) // count_words

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    main()