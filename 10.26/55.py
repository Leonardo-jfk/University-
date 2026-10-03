import pickle
import os.path


class Libro:
    def __init__(self, cod, tit, aut):

        self.isbn = cod


        self.titulo = tit
        self.autor = aut


    def __str__(self):
        r = 'ISBN: ' + str(self.isbn)
        r += ' - Título: ' + self.titulo
        r += ' - Autor: ' + self.autor
        return r


def test():
    # print('Prueba de grabación de varios registros...')
    # lib1 = Libro(2134, 'Fundación', 'Isaac Asimov')
    # lib2 = Libro(5587, 'Fundación e Imperio', 'Isaac Asimov')
    # lib3 = Libro(3471, 'Segunda Fundación', 'Isaac Asimov')
    # lib4 = Libro(1122, 'Los Límites de la Fundación', 'Isaac Asimov')
    # lib5 = Libro(2286, 'Fundación y Tierra', 'Isaac Asimov')
    #
    # fd = 'libros.dat'
    # m = open(fd, 'wb')
    # pickle.dump(lib1, m)
    # pickle.dump(lib2, m)
    # pickle.dump(lib3, m)
    # pickle.dump(lib4, m)
    # pickle.dump(lib5, m)
    # m.close()

    # print('Se grabaron varios registros en el archivo', fd)
    # m = open(fd, 'rb')
    # t = os.path.getsize(fd)
    # print('Se recuperaron estos registros desde el archivo', fd, ':')
    #
    # while m.tell() < t:
    #     lib = pickle.load(m)
    #     print(lib)
    # m.close()
    #
    # t = os.path.getsize(fd)
    print('Tamaño del archivo al terminar:bytes')
    #

def crear_arreglo():
    print('Prueba de grabación de varios registros...')
    lib1 = Libro(2134, 'Fundación', 'Isaac Asimov')
    lib2 = Libro(5587, 'Fundación e Imperio', 'Isaac Asimov')
    lib3 = Libro(3471, 'Segunda Fundación', 'Isaac Asimov')
    lib4 = Libro(1122, 'Los Límites de la Fundación', 'Isaac Asimov')
    lib5 = Libro(2286, 'Fundación y Tierra', 'Isaac Asimov')

    fd = 'libros.dat'
    m = open(fd, 'wb')
    pickle.dump(lib1, m)
    pickle.dump(lib2, m)
    pickle.dump(lib3, m)
    pickle.dump(lib4, m)
    pickle.dump(lib5, m)
    m.close()

def mostrar_arreglo(nameOfFile):
    fileName = 'libros.dat'
    print('Se grabaron varios registros en el archivo', nameOfFile)
    m = open(nameOfFile, 'rb')
    t = os.path.getsize(nameOfFile)
    print('Se recuperaron estos registros desde el archivo', nameOfFile, ':')

    while m.tell() < t:
        lib = pickle.load(m)
        print(lib)
    m.close()

    t = os.path.getsize(nameOfFile)
    print('Tamaño del archivo al terminar:', t, 'bytes')


def nuevo_archivo(nameOfFile, logic_compare):
    # x = int(input('Ingrese x: los libros cuyo código sea menor que x: '))
    if logic_compare == "more":
        x = int(input('Ingrese x: los libros cuyo código sea mayor que x: '))
    elif logic_compare == "less":
        x = int(input('Ingrese x: los libros cuyo código sea menor que x: '))
    elif logic_compare == "iqual":
        x = int(input('Ingrese x: los libros cuyo código sea igual que x: '))
    else:
        return print("wrong logic sir")

    file = open(nameOfFile, 'rb')
    # lib = pickle.load(file)
    # file.close()
    # filePointer = file.tell()
    fileEndHelper = file.seek(0, 2)
    fileEnd = file.tell()

    # fileEndHelper = file.seek(0, 2)
    filePointerReset = file.seek(0,0)
    filePointer = file.tell()
    second_file = open("librosSecond.dat", 'wb')

    # while filePointer < fileEndHelper:
    while file.tell() < fileEndHelper:
        lib = pickle.load(file)
        print("g")
    #     pickle.load(file)
        if logic_compare == "more":
            # x = int(input('Ingrese x: los libros cuyo código sea mayor que x: '))
            if lib.isbn > x:
                pickle.dump(lib, second_file)
        elif logic_compare == "less":
            # x = int(input('Ingrese x: los libros cuyo código sea menor que x: '))
            if lib.isbn < x:
                pickle.dump(lib, second_file)

        elif logic_compare == "iqual":
            # x = int(input('Ingrese x: los libros cuyo código sea igual que x: '))
            if lib.isbn == x:
                pickle.dump(lib, second_file)
        else:
            return print("wrong logic sir")

    file.close()
    second_file.close()

    file2 = open("librosSecond.dat", 'rb')
    fileSize = os.path.getsize("librosSecond.dat")
    while file2.tell() < fileSize:
    # for libro in range(fileSize):
        print(pickle.load(file2))

    file2.close()

    return "librosSecond.dat"


def truncar(nameOfFile):
    crear_texto()
    archivo = open(nameOfFile, 'r+')
    archivo.truncate(20)
    archivo.flush()
    archivo.seek(0)
    print(archivo.read())
    archivo.close()

def crear_texto():
    archivo = open('librosThird.dat', 'wt')

    archivo.write("gggggggfgggggggggggfgg")

    archivo.close()
    archivo = open('librosThird.dat', 'rt')
    print(archivo.read(5))
    print(archivo.read())
    archivo.close()


def main():
    response = -1
    nameOfFile = 'libros.dat'
    arreglo_cambiado, seccondCreated = False, False
    newFile = None

    while response != 0:
        response = int(input("give us the number: "))
        if response == 1:
            crear_arreglo()

        if response == 2:
            mostrar_arreglo(nameOfFile)

        if response == 3:
            newFile = nuevo_archivo(nameOfFile, "less")

        if response == 4:
            if newFile:
                mostrar_arreglo(newFile)
                arreglo_cambiado = True
        if response == 5:
            if arreglo_cambiado:

                crear_arreglo()
                new2File = nuevo_archivo(nameOfFile, "more")
                mostrar_arreglo(new2File)
                seccondCreated = True
            else:
                print("no se puede cambiar")

        if response == 6:
            # if seccondCreated:
            truncar('librosThird.dat')
            # else:

                # print("no se puede cambiar")





    print('Programa finalizado com sucesso!')

if __name__ == '__main__':
    main()