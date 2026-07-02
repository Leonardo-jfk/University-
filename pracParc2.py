def file_opener():
    file = open("entrada.txt", "r")
    archivo = file.readline()
    file.close()
    return archivo

def prints(r1, r2, r3, r4 ):
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


def main():
    archivo = file_opener()
    count_car, count_words, count_a, count_b, count_2do, count_3er = 0, 0, 0, 0, 0, 0
    contain_a, contain_digit, contain_voc, digit_at_end, last_car = False, False, False, False, ""
    r1, r2, r3, r4 = 0, 0, 0, 0

    contain_voc_start, contain_de, contain_4to = False, False, False


    for car in archivo:
        if car != " " and car != ".":
            count_car += 1

            # 1er

            if car.isdigit() and (count_car == 2 or count_car == 3):
                contain_digit = True
            if count_car >= 4 and car.isalpha() and car.lower() not in "aeuio":
                contain_a = True


        # 2do

            if car.lower() in "aeuio":
                contain_voc = True


            # 3er
            if car.lower() in "aeuio" and count_car < 4:
                contain_voc_start += 1


            # 4to
            if car.lower() == "e" and last_car.lower() == "d":
                contain_de = True
            if contain_de and car.lower() == "t":
                contain_4to = True



            last_car = car

        else:
            count_words += 1
            #1er
            if contain_a and contain_digit:
                r1 += 1

            #2do
            if contain_voc and last_car.isdigit():
                count_2do += 1


            #3er
            if contain_voc_start == 3 and count_car >= 4:
                r3 += 1

            #4to
            if contain_4to:
                r4 += 1


            count_car, count_b, count_a =0, 0, 0
            contain_digit,  digit_at_end, contain_a, contain_voc = False, False, False, False
            contain_voc_start, contain_de, contain_4to = 0, False, False

    r2 = (count_2do * 100) // count_words

    prints(r1, r2, r3, r4)

if __name__ == "__main__":
    main()