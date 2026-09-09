import random
import classProducto

def crear_arreglo():
    n = int(input("Give us the quantity of products: "))
    vector = n * [None]
    descriptions = ["banana", "pizza", "asado", "naranja", "burger"]

    for i in range(n):
        codigo = random.randint(1000, 9999)
        description = random.choice(descriptions)
        calories = random.randint(100, 9999)
        type = random.randint(1, 30)
        price = random.randint(10,999)

        vector[i] = classProducto.Producto(codigo, description, calories, type, price)


    print("Vector is created! ")
    print()

    return vector


def mostrar_arreglo(vector):
    n = len(vector)

    for i in range(n):
        print(vector[i])


def ordenar_vector(vector, type):
    n = len(vector)
    total_calories = 0

    for i in range(n - 1):
        ordenado = True

        for j in range(n - i - 1):
            if getattr(vector[j], type) > getattr(vector[j + 1], type):
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                ordenado = False

        if ordenado:
            break

    mostrar_arreglo(vector)

    for i in range(n):
        total_calories += vector[i].calories

    promedio_calories = total_calories / n

    print("promedio_calories es: ", promedio_calories)
    print()


    return vector





def crear_vector_types(vector):
    vector_types = 30 * [0]
    n = len(vector)

    for i in range(30):
        for j in range(n):
            if vector[j].type - 1 == i:
                vector_types[i] += 1


    for i in range(30):
        if 0 < vector_types[i] < 3:
            print(f"The type {i + 1} has {vector_types[i]} products ")



    return vector_types



def check_value(vector, type):
    n = len(vector)
    cod = int(input("Give us the code to check: "))

    for i in range(n):
        if getattr(vector[i], type) == cod:
            print("description: ", vector[i].description)
            print("precio: ", vector[i].price)
            print()
            return

    print("didn't find the number ")
    print()






def main():

    response = -1
    vector = list()

    while response != 0:
        print("0: Salir")
        print("1: crear arreglo")
        print("2: mostrar arreglo")
        print("3: mostrar según la cantidad de calorías")
        print("4: cantidad de productos de cada tipo ")
        print("5: Determinar si existe un producto cuyo código sea igual cod")

        response = int(input("Give us a number to continue: "))

        if response == 1:
            vector = crear_arreglo()

        if response == 2:
            if vector:
                mostrar_arreglo(vector)
            else:
                print("go to the 1st step")


        # b)  ordenado de menor a
        # mayor según la cantidad de calorías del producto
        if response == 3:
            if vector:
                vector_ordenado = ordenar_vector(vector, "calories")
            else:
                print("go to the 1st step")

        # c)
        # cantidad de productos que hay en el arreglo por cada tipo
        if response == 4:
            if vector:
                vector_types = crear_vector_types(vector)
            else:
                print("go to the 1st step")

        # c)
        # Determinar si existe un producto cuyo código sea igual cod,
        if response == 5:
            if vector:
                check_value(vector, "codigo")

        else:
            print("go to the 1st step")



if __name__ == "__main__":
    main()