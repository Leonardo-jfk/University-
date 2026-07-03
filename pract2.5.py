def car_checks(car, code):
    if code == "vocal":
        return car.lower() in "aeiouáéúóí"
    if code == "consonant":
        return car.lower() not  in "aeiouáéúóí" and car.isalpha()
    if code == "digit":
        return car.isdigit()

    else:
        return False

def file_opener(name):
    file = open(name, "r")
    archivo = file.read()
    file.close()
    return archivo

def main():
    archivo = file_opener("entrada.txt")
    count_car, count_words, contain_upper, last_car = 0, 0, False, ""
    r1, r2, r3, r4 = 0, 0, 0, 0
    contain_impar, aux_car, max = False, "", 0
    start_with_vocal, count_consonant, count_car_3er, count_words_3er = False, 0, 0, 0
    contain_ba, contain_t = False, False

    for car in archivo:
        if car != " " and car != ".":
            count_car += 1

            #1er
            if car.isupper():
                contain_upper = True

            # 2do
            if car_checks(car, "digit"):
                aux_car = car
                if int(aux_car) % 2 != 0:
                    contain_impar = True

            # 3er

            if count_car == 1 and car_checks(car, "vocal"):
                start_with_vocal = True

            if car_checks(car, "consonant"):
                count_consonant += 1

            # 4to
            if car.lower() == "a" and last_car.lower() == "b":
                contain_ba = True
            if car.lower() == "t":
                contain_t = True

            last_car = car
        else:
            # 1er
            if not contain_upper and car_checks(last_car, "digit"):
                r1 += 1
                print(r1, last_car)

            #2do
            if contain_impar:
                if max < count_car:
                    max = count_car

            #3er
            if start_with_vocal and count_consonant >= 3:
                count_car_3er += count_car
                count_words_3er += 1
                print(count_car_3er, count_words_3er)


            #4to
            if not contain_t and contain_ba:
                r4 += 1





            count_words += 1
            count_car, contain_upper, contain_impar, count_consonant, start_with_vocal = 0, False, False, 0, False
            contain_ba, contain_t = False, False

    r2 = max
    if count_words_3er != 0:
        r3 = (count_car_3er ) // count_words_3er
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    main()