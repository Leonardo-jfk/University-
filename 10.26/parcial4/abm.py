import io
import os
import pickle
import os.path


class Estudiante:
    def __init__(self, leg, nom, prom):
        self.legajo = leg
        self.nombre = nom
        self.promedio = prom
        self.activo = True

    def __str__(self):
        r = ''
        r += '{:<20}'.format('Legajo: ' + str(self.legajo))
        r += '{:<30}'.format('Nombre: ' + self.nombre.strip())
        r += '{:<20}'.format('Promedio: ' + str(self.promedio))
        return r


def validar_legajo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup) + ' por favor: '))
        if n < inf or n > sup:
            print('Se pidió entre', inf, 'y', sup, '... cargue de nuevo...')
    return n


def validar_promedio():
    n = -1.0
    while n < 0.0 or n > 10.0:
        n = float(input('Valor entre 0 y 10 por favor (puede tener decimales): '))
        if n < 0 or n > 10:
            print('Error... se pidió entre 0 y 10... cargue de nuevo...')
    return n


def buscar(m, leg):
    """Busca un registro cuyo legajo coincida con leg en el archivo de estudiantes.

    Si lo encuentra, retorna su posición (como número de byte). Si no lo encuentra, retorna
    el valor -1.

    :param m: El manejador del archivo donde se debe buscar.
    :param leg: El legajo a buscar.
    :return la posición de byte donde fue encontrado el registro.
    """
    global FD
    t = os.path.getsize(FD)

    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)

    posicion = -1
    while m.tell() < t:
        fp = m.tell()
        est = pickle.load(m)
        if est.activo and est.legajo == leg:
            posicion = fp
            break

    m.seek(fp_inicial, io.SEEK_SET)
    return posicion


def alta():
    """Agrega el registro de un estudiante al archivo.

    Los datos del estudiante se toman por teclado. El registro será grabado sólo si el
    archivo no contenía ya un estudiante con el mismo legajo.
    """
    global FD
    m = open(FD, 'a+b')

    print()
    print('Legajo del estudiante a registrar (cargue 0 para salir): ')
    leg = validar_legajo(0, 99999)
    while leg != 0:
        # buscamos el registro con ese legajo...
        pos = buscar(m, leg)
        if pos == -1:
            # no estaba repetido... lo cargamos por teclado...
            nom = input('Nombre: ')

            # ...ajustamos a 30 caracteres, rellenando con blancos al final...
            nom = nom.ljust(30, ' ')

            print('Promedio...')
            pro = validar_promedio()

            est = Estudiante(leg, nom, pro)

            # ...lo grabamos...
            pickle.dump(est, m)

            # ...volcamos el buffer de escritura
            # para que el sistema operativo REALMENTE
            # grabe en disco el registro...
            m.flush()

            print('Registro grabado en el archivo...')

        else:
            print('Legajo repetido... alta rechazada...')

        print()
        print('Otro legajo de estudiante a registrar (cargue 0 para salir): ')
        leg = validar_legajo(0, 99999)

    m.close()

    print()
    print('Operación de altas finalizada...')
    input('Presione <Enter> para seguir...')


def baja():
    """Elimina (por marcado lógico) el registro de un estudiante del archivo.

    El legajo del estudiante a eliminar se toma por teclado. El registro será eliminado sólo si el
    usuario confirma que está seguro de querer hacerlo, y el registro será en ese caso marcado en forma
    lógica y vuelto a grabar.
    """
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    m = open(FD, 'r+b')

    print()
    print('Legajo del estudiante a borrar (cargue 0 para salir): ')
    leg = validar_legajo(0, 99999)
    while leg != 0:
        # buscamos el registro con ese legajo...
        pos = buscar(m, leg)
        if pos != -1:
            # encontrado... procedemos a cargarlo...
            m.seek(pos, io.SEEK_SET)
            est = pickle.load(m)

            # ...mostramos el registro tal como estaba...
            print()
            print('El registro actualmente grabado es:')
            print(est)

            # ...chequemos si el usario está seguro de lo que hace...
            r = input('Está seguro de querer borrarlo (s/n)?: ')
            if r in ['s', 'S']:
                # lo marcamos como borrado, y ya...
                est.activo = False

                # ...reubicamos el file pointer...
                m.seek(pos, io.SEEK_SET)

                # ...y lo volvemos a grabar...
                pickle.dump(est, m)

                print()
                print('Registro eliminado del archivo...')

        else:
            print('Ese registro no existe en el archivo...')

        print()
        print('Otro legajo de estudiante a borrar (cargue 0 para salir): ')
        leg = validar_legajo(0, 99999)

    m.close()

    print()
    print('Operación de bajas finalizada...')
    input('Presione <Enter> para seguir...')


def modificacion():
    """Modifica el contenido de un registro de un estudiante del archivo.

    El legajo del estudiante a modificar se toma por teclado. Sólo se permitirá modificar el valor
    de los campos nombre y promedio, cuyos nuevos valores serán tomados por teclado mediante un menú.
    Cuando el usuario disponga terminar de cargar los nuevos datos, el registro se vuelve a grabar con
    sus nuevos datos en su ubicación original.
    """
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    m = open(FD, 'r+b')

    print()
    print('Legajo del estudiante a modificar (cargue 0 para salir): ')
    leg = validar_legajo(0, 99999)
    while leg != 0:
        # buscamos el registro con ese legajo...
        pos = buscar(m, leg)
        if pos != -1:
            # encontrado... procedemos a cargarlo...
            m.seek(pos, io.SEEK_SET)
            est = pickle.load(m)

            # ...mostramos el registro tal como estaba...
            print()
            print('El registro actualmente grabado es:')
            print(est)

            # ...modificamos el valor de los campos...
            op = 0
            while op != 3:
                print('1. Modificar nombre.')
                print('2. Modificar promedio.')
                print('3. Terminar modificaciones.')
                op = int(input('\t\tIngrese opción: '))

                if op == 1:
                    nom = input('Nuevo nombre: ')
                    est.nombre = nom.ljust(30, ' ')

                elif op == 2:
                    print('Nuevo promedio:')
                    est.promedio = validar_promedio()

                elif op == 3:
                    pass

            # ...registro modificado en memoria...
            # ...ahora nos volvemos a su posición en el archivo...
            m.seek(pos, io.SEEK_SET)

            # ...y volvemos a grabar el registro modificado...
            pickle.dump(est, m)

            print()
            print('Los datos del registro se actualizaron en el archivo...')

        else:
            print('Ese registro no existe en el archivo...')

        print('Otro legajo de estudiante a modificar (cargue 0 para salir): ')
        leg = validar_legajo(0, 99999)

    m.close()

    print()
    print('Operación de modificaciones finalizada...')
    input('Presione <Enter> para seguir...')


def depuracion():
    """Optimiza el espacio físico del archivo.

    La función aplica un proceso de baja física generalizada: todos los registros que estaban
    marcados en forma lógica como eliminados, son físicamente eliminados del archivo.
    """
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(FD)

    original = open(FD, 'rb')
    temporal = open('temporal.dat', 'wb')

    print('Procediendo a optimizar el archivo', FD, '(eliminación física de registros borrados)')
    while original.tell() < tbm:
        # cargar un registro del archivo original...
        est = pickle.load(original)

        # ...y si no estaba marcado como eliminado, grabarlo en el archivo temporal...
        if est.activo:
            pickle.dump(est, temporal)

    # cerrar ambos archivos...
    original.close()
    temporal.close()

    # eliminar el archivo original...
    os.remove(FD)

    # y renombrar el temporal...
    os.rename('temporal.dat', FD)

    print('Optimización terminada... se eliminaron los registros marcados como borrados...')
    input('Presione <Enter> para seguir...')


def listado_completo():
    """Muestra el contenido completo del archivo.

    """
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(FD)

    m = open(FD, 'rb')

    print('Listado general de estudiantes registrados:')
    while m.tell() < tbm:
        est = pickle.load(m)
        if est.activo:
            print(est)

    m.close()

    print()
    input('Presione <Enter> para seguir...')


def listado_filtrado():
    """Muestra los registros de los estudiantes cuyo promedio sea >= 7.

    """
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(FD)

    m = open(FD, 'rb')

    print('Listado de estudiantes con promedio mayor o igual a 7:')
    while m.tell() < tbm:
        est = pickle.load(m)
        if est.activo and est.promedio >= 7:
            print(est)

    m.close()

    print()
    input('Presione <Enter> para seguir...')


def main():
    global FD
    FD = 'estudiantes.utn'

    op = 0
    while op != 7:
        print('Opciones ABM del archivo de estudiantes')
        print('   1. Alta de estudiantes')
        print('   2. Baja de estudiantes')
        print('   3. Modificación de estudiantes')
        print('   4. Listado completo de estudiantes')
        print('   5. Listado de estudiantes con promedio mayor o igual a 7')
        print('   6. Depuración del archivo de estudiantes')
        print('   7. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()

        if op == 1:
            alta()

        elif op == 2:
            baja()

        elif op == 3:
            modificacion()

        elif op == 4:
            listado_completo()

        elif op == 5:
            listado_filtrado()

        elif op == 6:
            depuracion()

        elif op == 7:
            pass


# script principal...
if __name__ == '__main__':
    main()
