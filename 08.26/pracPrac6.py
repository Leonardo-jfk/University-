def file_opener(name):

    file = open(name, 'r')
    archivo = file.readline()
    file.close()
    return archivo

def car_compare(car, code):
    # is_digit, is_vocal, is_conson = False, False, False


    if code == "digit":
        return car.isdigit()
            # return True

    if code == "vocal":
        return  car.lower() in "aeiouéúáíó"
            # return True

    if code == "consonant":
        return car.isalpha() and not car.lower() in "aeiouéúáíó"
            # return True



def main():

    name = "entrada.txt"
    archivo = file_opener(name)
    count_car, count_a, count_words, count_b, count_voc, count_digit = 0, 0, 0, 0, 0, 0
    r1, r2, r3, r4 = 0, 0, 0, 0
    contain_voc, contain_n, menor, first_call = False, False, 0, True
    count_3er, contain_digit, contain_g, count_3er_words,count_3er_car = 0, False, False, 0, 0
    start_with_voc, last_car, contain_pe = False, "", False

    for car in archivo:


        if car != " " and car != ".":
            count_car += 1

        #1er
            if car_compare(car, "consonant"):
                count_a += 1

        #2do
            if count_car == 2 and car_compare(car, "vocal"):
                contain_voc = True
            if car.lower() == "n":
                contain_n = True


        # 3er
            if count_car == 2 and car.lower() == "g":
                contain_g = True
            if car_compare(car, "digit"):
                contain_digit = True


        # 4to
            if count_car == 1 and car_compare(car, "vocal"):
                start_with_voc = True
            if car.lower() == "e" and last_car.lower() == "p":
                contain_pe = True



            last_car = car

        else:
            #1er
            if count_car % 2 != 0 and count_a == 1:
                r1 += 1

            # 2do
            if contain_voc and not contain_n:
                if first_call:
                    menor = count_car
                    first_call = False
                if count_car < menor:
                    menor = count_car

            #3er
            if not contain_digit and contain_g:
                count_3er_car += count_car
                count_3er_words += 1


            #4to
            if not start_with_voc and contain_pe:
                r4 += 1






            count_words += 1
            count_car, count_a, contain_voc, contain_n, contain_g, contain_digit = 0, 0, False, False, False, False,
            start_with_voc, contain_pe = False, False

    r2 = menor
    if count_3er_words != 0:
        r3 = count_3er_car // count_3er_words
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)





if __name__ == "__main__":
    main()
