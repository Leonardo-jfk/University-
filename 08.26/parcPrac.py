def file_opener():
    archivo = open("entrada.txt", "r")
    file = archivo.readline()
    archivo.close()
    return file

def prints(r1, r2, r3, r4, r5, r6):
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

def main():
    archivo = file_opener()

    r1, r2, r3, r4, r5, r6 = 0, 0, 0, 0, 0, 0
    count_car, count_w, contain_voc, contain_digit, contain_6_car, = 0, 0, False, False, False
    promedio, contain_r, contain_e, cant_car_2do, cant_2do = 0, 0, 0, 0, 0
    start_voc, end_voc, voc_exact_1, voc_exact_2, cant_word_3er = False, False, 0, 0, 0
    car_before, contain_fi, contain_f_n = "", False, False

    for car in archivo:
        if car != " " and car != ".":
            count_car += 1
            #1er
            if car.isdigit():
                contain_digit = True
            if car.lower() in "aeiou":
                contain_voc += 1


            # 2do
            if car.lower() == "r":
                contain_r += 1
            if car.lower() == "e":
                contain_e += 1




        # 3er

            if car.lower() in "aeuio" and count_car == 1:
                start_voc = True
                voc_exact_1 = car.lower()

            # 4to
            if car.lower() == "i" and car_before.lower() == "f":
                contain_fi = True
            if car.lower() in "tn":
                contain_f_n = True




            voc_exact_2 = car
            car_before = car

        else:
            #1er
            if count_car == 6 and (contain_voc == 1 or contain_voc == 2) and contain_digit:
                r1 += 1

            #2do
            if contain_r == 1 and  contain_e >= 2:
                cant_2do += 1
                cant_car_2do += count_car

            # r2 = cant_car_2do // cant_2do


            #3er
            if start_voc and voc_exact_2.lower() in "aeuio":
                if voc_exact_1 != voc_exact_2:
                    r3 += 1




            #4to
            if contain_fi and contain_f_n:
                r4 += 1

            count_w += 1
            count_car, contain_digit, contain_voc, contain_r, contain_e = 0, False, 0, 0, 0
            start_voc, end_voc, voc_exact_1 = False, False, False
            contain_fi, contain_f_n = False, False
    if cant_2do != 0:
        r2 = cant_car_2do // cant_2do



    prints(r1, r2, r3, r4, r5, r6)






if __name__ == "__main__":
    main()