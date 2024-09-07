import os.path
from funciones import *
from datetime import *
import pickle


def procesar_archivo(vec_usuario):
    if not os.path.exists("proyectos.csv"):
        print('Error: No existe el archivo...')
        return

    m = open("proyectos.csv", mode="rt", encoding="UTF-8")
    vec_eliminados = 0
    lineas = 0

    for linea in m:
        lineas += 1
        # ignora primera linea
        if lineas != 1:
            linea = linea[:-1]
            tokens = linea.split('|')
            repos = reg_iguales(vec_usuario, tokens[1])

            if tokens[4] != "" and repos == -1:
                # ignoran los que no tienen lenguaje
                usser = import_linea(tokens)
                add_in_order(vec_usuario, usser)
            else:
                vec_eliminados += 1

    n = len(vec_usuario)
    print(str('\n') + '-' * 122)
    print(str("\t" * 10) + "Cantidad de registros almacenados: ", n)
    print(str('\n') + '-' * 122)
    print(str("\t" * 10) + "Cantidad de registros omitidos:    ", vec_eliminados, '\n' + '-' * 122)
    m.close()


def reg_iguales(vec, valor):  # repositorios iguales
    i = -1
    izq, der = 0, (len(vec) - 1)
    while izq <= der:
        c = (izq + der) // 2
        if valor == vec[c].repositorio:
            i = c
            break
        if valor < vec[c].repositorio:
            der = c - 1
        else:
            izq = c + 1

    return i


def validar_num(minn, maxx, mensaje):
    op = int(input(mensaje))
    while minn > op or op > maxx:
        op = int(input("\n  Valor incorrecto, ingrese nuevamente la opción: "))

    return op


# ---------------------------------------------------------------------------------------------------------------------


def opcion_2(v, mensaje):
    print(str('\n') + '-' * 122)
    x = input(mensaje)
    print('-' * 122)

    namm = []
    for i in range(len(v)):
        if x in v[i].tags:
            to_string_2(v[i])
            namm.append(v[i])

    return namm


def estrellas_likes(vec):
    for i in range(len(vec)):
        vec[i].likes = float(vec[i].likes)
        if 0 <= vec[i].likes <= 10:
            vec[i].likes = 1
        elif 10.1 <= vec[i].likes <= 20:
            vec[i].likes = 2
        elif 20.1 <= vec[i].likes <= 30:
            vec[i].likes = 3
        elif 30.1 <= vec[i].likes <= 40:
            vec[i].likes = 4
        else:
            vec[i].likes = 5

    return vec


def crear_archivo_pto2(w):
    m = open("Listado.txt", mode="w", encoding="UTF-8")
    b = "|Nombre de Usuario | Repositorio | Fecha de actualización |  lenguajes  |  estrellas  |  tags  |  url "
    m.write(b)
    m.write("\n\n")

    for usser in range(len(w)):
        n = f"{w[usser].nombre_usuario}| {w[usser].repositorio}| {w[usser].fecha_act}| {w[usser].lenguaje}| " \
            f"{w[usser].likes}| {w[usser].tags}| {w[usser].url}"
        m.write(n)
        m.write("\n")
    m.close()


# ---------------------------------------------------------------------------------------------------------------------


def opcion_3(vector):
    nombres = []
    contador = []

    for i in range(len(vector)):
        if not nombres:
            nombres.append(vector[i].lenguaje)
            contador.append(1)
        else:
            for j in range(len(nombres)):
                if vector[i].lenguaje == nombres[j]:
                    contador[j] += 1

            if vector[i].lenguaje not in nombres:
                nombres.append(vector[i].lenguaje)
                contador.append(1)

    return contador, nombres


def ordenar_leng(cantidad, nombres):
    b = f"|{'LENGUAJE':^50}     |{'CANTIDAD':^60}  | "
    print("\n" + str(' -' * 60) + '\n', b, "\n" + str(' -' * 60))
    n = len(cantidad)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if cantidad[i] < cantidad[j]:
                cantidad[i], cantidad[j] = cantidad[j], cantidad[i]
                nombres[i], nombres[j] = nombres[j], nombres[i]

    for k in range(len(nombres)):
        print(" |", '{:^49}'.format(nombres[k]), "    |", '{:^60}'.format(cantidad[k]), "|")
    print(str(' -' * 60))

# ---------------------------------------------------------------------------------------------------------------------


def opcion_4(vec):  # genera matriz
    mes = mes_4(vec)
    mat = [[0] * 5 for _ in range(12)]

    for k in range(len(vec)):
        fecha = int(mes[k]) - 1
        estrella = int(vec[k].likes) - 1
        mat[fecha][estrella] += 1

    return mat


def mes_4(vec):
    mes = []
    for i in range(len(vec)):
        if vec[i].fecha_act[5] == '0':
            mes.append(str(vec[i].fecha_act[6]))
        else:
            mes.append(str(vec[i].fecha_act[5] + vec[i].fecha_act[6]))

    return mes


def buscar_m(matriz):
    total = 0
    n = validar_num(1, 12, "\nIngrese el numero del mes: ")
    for i in range(12):
        if n == i+1:

            for j in range(5):
                total += matriz[i][j]
            break
    print("\nEn el mes:", n, "se actualizaron:", total, "proyectos")


def mostrar_matriz(matriz):
    b = f"{'  ':^15} |{'Estrella 1':^15}|{'Estrella 2':^15}| {'Estrella 3':^16} | {'Estrella 4':^17} |  {'Estrella 5':^18} \t\t\t| "
    print("\n" + str(' -' * 60) + '\n', b, "\n" + str(' -' * 60))
    m, n = len(matriz), len(matriz[0])
    res = ''

    for f in range(m):
        if f == 0:
            res += f"|{'Enero':^15}"
        if f == 1:
            res += f"|{'Febrero':^15}"
        if f == 2:
            res += f"|{'Marzo':^15}"
        if f == 3:
            res += f"|{'Abril':^15}"
        if f == 4:
            res += f"|{'Mayo':^15}"
        if f == 5:
            res += f"|{'Junio':^15}"
        if f == 6:
            res += f"|{'Julio':^15}"
        if f == 7:
            res += f"|{'Agosto':^15}"
        if f == 8:
            res += f"|{'Septiembre':^15}"
        if f == 9:
            res += f"|{'Octubre':^15}"
        if f == 10:
            res += f"|{'Noviembre':^15}"
        if f == 11:
            res += f"|{'Diciembre':^15}"
        res += ' |  '
        for c in range(n):
            res += str(matriz[f][c]) + '\t' * 5
        res += '|\n'
    res += str(' -' * 60)

    return res


# ---------------------------------------------------------------------------------------------------------------------


def opcion_5(vec):  # busca proyecto actualizado
    fecha_actual = date.today()
    print(str('\n') + '-' * 122)
    rep = input('Ingrese el nombre del repositorio: ')

    for i in range(len(vec)):
        if rep == vec[i].repositorio:
            a = to_string(vec[i])
            print(a)
            url = input('Ingrese el nuevo URL: ')
            vec[i].fecha_act = str(fecha_actual)
            vec[i].url = url
            return
        else:
            continue
    print('¡ERROR! No existe el repositorio buscado.')


# ---------------------------------------------------------------------------------------------------------------------


def opcion_6(a):  # guardar populares
    vec = []
    vec_mese = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                'Noviembre', 'Diciembre']
    m = open('Populares.dat', 'wb')

    for i in range(5):
        for j in range(12):
            mes = vec_mese[j]
            estrella = i + 1
            cantidad = a[j][i]
            if cantidad != 0:
                todo = Populares(mes, estrella, cantidad)
                vec.append(todo)

    for k in range(len(vec)):
        pickle.dump(vec[k], m)
    print("  El archivo se creo correctamente!")


# ---------------------------------------------------------------------------------------------------------------------


def opcion_7():  # mostrar archivo
    if not os.path.exists("Populares.dat"):
        print('Error: No existe el archivo...')
        return

    matriz = [[0] * 5 for _ in range(12)]
    vec = []
    m = open('Populares.dat', 'rb')
    largo = os.path.getsize('Populares.dat')
    while largo > m.tell():
        algo = pickle.load(m)
        vec.append(algo)

    m.close()

    for i in range(len(vec)):
        m = vec[i].mes
        n = meses(m)-1
        e = vec[i].estrellas-1
        matriz[n][e] = vec[i].cantidad
    a = mostrar_matriz(matriz)
    print(a)


def meses(m):
    vec_mese = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    for i in range(len(vec_mese)):
        if m == vec_mese[i]:
            a = i + 1
            return a


# ---------------------------------------------------------------------------------------------------------------------


def principal():
    a = 0
    vec_usuario = []
    op = -1
    band = False
    band_4 = False
    band_6 = False
    band_e = False

    while op != 8:
        print("\n" + str("_" * 43) + "  BIENVENID0/A AL MENÚ DE OPCIONES  " + str("_" * 43))
        print(str('\t' * 3) + "1 - Cargar: Cargar el contenido del archivo en un vector de registros de proyectos")
        print(str('\t' * 3) + "2 - Filtrar por tag")
        print(str('\t' * 3) + "3 - Determinar la cantidad de proyectos por cada lenguaje de programación")
        print(str('\t' * 3) + "4 - Determinar los meses en los que se actualizan los proyectos, de acuerdo a la cantidad de estrellas")
        print(str('\t' * 3) + "5 - Buscar proyecto actualizado")
        print(str('\t' * 3) + "6 - Guardar populares")
        print(str('\t' * 3) + "7 - Mostrar archivo en forma de tabla")
        print(str('\t' * 3) + "8 - Salir")
        op = validar_num(0, 8, "\n  Por favor, ingrese la opción elegida: ")

        if op == 1:
            procesar_archivo(vec_usuario)
            band = True
        else:
            if not band and op != 8:
                print("  \n  Cargue los datos antes de continuar...")
            else:
                if op == 2:
                    if not band_e:
                        e = estrellas_likes(vec_usuario)
                        a = opcion_2(e, "Ingrese el nombre del tag a buscar: ")
                        band_e = True
                    else:
                        a = opcion_2(vec_usuario, "Ingrese el nombre del tag a buscar: ")

                    b = f"{'REPOSITORIO':^28} | {'FECHA DE ACTUALIZACIÓN':^30} | {'ESTRELLAS':^27} | "

                    if len(a) == 0:
                        print("No se encontró el tag buscado.")
                    else:
                        print(b)
                        for i in range(len(a)):
                            z = to_string_2(a[i])
                            print(z)

                        print("\nDesea ingresar el listado en nuevo archivo?")
                        print("   1- Si")
                        print("   2- No")
                        n = validar_num(1, 2, "\nIngrese su respuesta: ")
                        if n == 1:
                            crear_archivo_pto2(a)
                            print("\nEl archivo fue creado con éxito!!! ")

                elif op == 3:
                    con, nom = opcion_3(vec_usuario)
                    ordenar_leng(con, nom)

                elif op == 4:
                    band_4 = True
                    if not band_e:
                        e = estrellas_likes(vec_usuario)
                        a = opcion_4(e)
                        band_e = True
                    else:
                        a = opcion_4(vec_usuario)
                    b = mostrar_matriz(a)
                    print(b)
                    buscar_m(a)

                elif op == 5:
                    opcion_5(vec_usuario)

                elif op == 6:
                    if not band_4:
                        print("  \nIngrese a la opcion 4 previamente")
                    else:
                        opcion_6(a)
                        band_6 = True

                elif op == 7 and not band_6:
                    print("El archivo no existe")

                elif op == 7 and band_6:
                    opcion_7()

    print(" \n  Espero que tenga un buen día!")


if __name__ == "__main__":
    principal()
