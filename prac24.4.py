def car_checks(car, code):
    if code == "vocal":
        return car.lower() in "aeiouáéúíó"
    if code == "digit":
        return car.isdigit()
    if code == "conson":
        return car.isalpha() and not car.lower() in "aeiouáéúíó"
    else:
        return False

def file_opener(name):
    file = open(name, "r")
    archivo = file.read()
    file.close()
    return archivo

def main():
    archivo = file_opener("entrada.txt")
    r1, r2, r3, r4 = 0, 0, 0, 0
    count_car, count_cons, count_vocal, count_words, count_digit = 0, 0, 0, 0, 0
    contain_cs = False
    menor, contain_s, contain_c, words_without_d = float("inf"), False, False, 0
    start_with_vi, last_car, contain_n = False, "", False

    for car in archivo:
        if car != " " and car != ".":
            count_car += 1
        # 1er
            if car_checks(car, "digit"):
                count_digit += 1
            if car_checks(car, "conson"):
                count_cons += 1
            if car_checks(car, "vocal"):
                count_vocal += 1

        # 2do
        # if car.lower() in "cs":
        #     contain_cs = True
            if car.lower() == "c":
                contain_c = True
            if car.lower() == "s":
                contain_s = True


        # 3er
            if car_checks(car, "digit"):
                count_digit += 1

        # 4to
            if last_car.lower() == "v" and car.lower() == "i" and count_car == 2:
                start_with_vi = True
            if car.lower() == "n":
                contain_n = True

            last_car = car

        else:
            #1er
            if count_digit > count_vocal and count_cons == 1:
                r1 += 1
            #2do
            if contain_c or contain_s:
                if menor > count_car:
                    menor = count_car
                    print(count_car)

            #3er
            if count_digit == 0:
                words_without_d += 1

            #4to
            if start_with_vi and contain_n:
                r4 += 1



            count_words += 1
            count_vocal, count_car, count_cons, count_digit = 0, 0, 0, 0
            contain_cs, contain_s, contain_c, start_with_vi, contain_n = False, False, False, False, False

    r2 = menor
    r3 = (words_without_d * 100) // count_words
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    main()