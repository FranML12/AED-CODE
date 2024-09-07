class Envio:
    def __init__(self, cp:str, destino:str, tipo:int, pago:int):
        self.codigo_postal = cp
        self.destino = destino
        self.tipo_envio = tipo
        self.forma_pago = pago
#inicializo la clase de envios y agregro los objetos respectivos y les asigno las variables de los futuros atributos
    def __str__(self) -> str:
        return f"{self.codigo_postal},{self.destino},{self.tipo_envio},{self.forma_pago}"
#escribo el __str__ para cuando se quiera printear o coso 


def menu():
#creo una funcion menu donde printeo el menu y mando la opcion seleccionada del vuelta a la funcion principal(flores_maximo) para hacer lo que se tenga que hacer
    menu = '1) cargar un arreglo con envios "enviostp3" (eliminando el viejo y si o si muestra un cartel de esta seguro ?) \n2) cargar por teclado datos de envio(se guarda al final del array sin eliminar ninguno previo)\n3) mostrar todos los array ordenados por codigo postal de menor a mayor\n4) Buscar si existe en el arreglo un registro/objeto cuya dirección de envío sea igual a d y que sea del tipo de envío e, siendo d y e dos valores que se cargan por teclado\n5) Buscar si existe en el arreglo un registro/objeto cuyo código postal sea igual a cp, siendo cp un valor que se carga por teclado\n0)Salir'
    # usa \n apra bajar de linea
    print(menu)
    opcion = int(input('Introducir alguna opcion: '))
    return opcion


def validar_num(minn, maxx, mensaje ):
    op = int(input(mensaje))
    while minn > op > maxx:
        op = int(input("\n  Valor incorrecto, ingrese nuevamente la opción: "))
    return op


def es_letra(c):
    return 'A' <= c <= 'Z' or 'a' <= c <= 'z'

def es_mayus(c):
    return 'A' <= c <= 'Z'

def es_digito(c):
    return '0' <= c <= '9'

# aca
def pais(cp):
    if len(cp) == 9 and cp[5] == '-' and es_letra(cp[:5]) and es_letra(cp[6:]):
        pais = 'Brasil'
    elif len(cp) == 8 and es_letra(cp[0]) and es_letra(cp[5:]) and es_digito(cp[1:5]):
        pais = 'Argentina'
    elif es_digito(cp):
        if len(cp) == 7:
            pais = 'Chile'
        elif len(cp) == 6:
            pais = 'Paraguay'
        elif len(cp) == 5:
            pais = 'Uruguay'
            if cp[0] == '1':
                pais = 'Montevideo'
        elif len(cp) == 4:
            pais = 'Bolivia'
        else:
            pais = 'Otros países'
    else:
        pais = 'Otros países'
        
    return pais


def final_amount(cp, destino, tipo, pago):
    # determinación del importe inicial a pagar.
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]

    if destino == 'Argentina':
        inicial = monto
    else:
        if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    # determinación del valor final del ticket a pagar.
    # asumimos que es pago en tarjeta...
    final = inicial

    # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
    if pago == 1:
        final = int(0.9 * inicial)

    return final


def check_dir(direccion):
    cl = cd = 0
    td = False
    ant = " "
    for car in direccion:
        if car in " .":
            # fin de palabra...
            # un flag si la palabra tenia todos sus caracteres digitos...
            if cl == cd:
                td = True

            # resetear variables de uso parcial...
            cl = cd = 0
            ant = " "

        else:
            # en la panza de la palabra...
            # contar la cantidad de caracteres de la palabra actual...
            cl += 1

            # si el caracter no es digito ni letra, la direccion no es valida... salir con False...
            if not car.isdigit() and not car.isalpha():
                return False

            # si hay dos mayusculas seguidas, la direccion no es valida... salir con False...
            if ant.isupper() and car.isupper():
                return False

            # contar digitos para saber si hay alguna palabra compuesta solo por digitos...
            if car.isdigit():
                cd += 1

            ant = car

    # si llegamos acá, es porque no había dos mayusculas seguidas y no habia caracteres raros...
    # ... por lo tanto, habria que salir con True a menos que no hubiese una palabra con todos digitos...
    return td

def borrar_espacios(rango):
    resultado = ''
    for i in rango:
        if i != ' ':
            resultado += i
            
    return resultado

def arr(data):
    data_line = data.readline()  # Lee la siguiente línea
    if data_line:
        cp = borrar_espacios(data_line[:9])  # Código postal
        direccion = borrar_espacios(data_line[9:29])  # Dirección
        tipo = borrar_espacios(data_line[29:30])  # Tipo de envío
        pago = borrar_espacios(data_line[30:31])  # Método de pago
        
        # ACA TIENE QUE DEVOLVERLO COMO CLASS
        return Envio(cp, direccion, tipo, pago) # Devuelve una tupla con los datos
    else:
        data.close()
        return None  # Si no hay más líneas, devuelve None
    
"""Crear el arreglo de registros/objetos de forma que contenga todos los datos de todos los envíos guardados en el archivo de texto que se provee junto con este enunciado.
 Cada vez que se elija esta opción, el arreglo debe ser creado de nuevo desde cero, perdiendo todos los registros/objetos que ya hubiese contenido.
 Asegúrese de que antes de eliminar el viejo arreglo, se muestre en pantalla un mensaje de advertencia al usuario de forma que tenga la opción de cancelar la operación.
   Si el arreglo no existiese, debe ser creado y luego agregar los registros según indique el archivo de texto.
 Si se elige esta opción, los datos anteriores deben ser eliminados sin importar si fueron originalmente cargados desde el archivo o fueron cargados manualmente desde la opción 2:
   elimine lo que haya en el arreglo, vuelva a levantar los datos del archivo de texto Y YA."""

def uno(registros):
    while True:
        envio = arr(data)
        if envio:
            envios.append(envio)
            # Puedes hacer más procesamiento aquí si es necesario
        else:
            break
    if registros:
        respuesta = input("Hay registros cargados. ¿Desea eliminar los registros existentes y cargar de nuevo desde el archivo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada por el usuario.")
            return registros 


    return registros

def flores_maximo():
    registros = []
    m = open('envios-tp3.txt', 'rt')

    linea = m.readline()
    control = 'Soft Control'
    if 'HC' in linea:
        control = 'Hard Control'
    m.close()

    futura_lista = []
    op = None
    while op != 0:
        op = menu()      
        if op == 1:
            def uno(registros):
                pass
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 8:
            pass
        elif op == 9:
            pass
        else:
            print('\n  Valor incorrecto, ingrese nuevamente la opción, no seas bobi: ')
            op = menu()

        


if __name__ == "__main__":
    flores_maximo()
    #elijo el nombre maximo flores o sino recomiendo planta de sombra
#fran uso snake case porque me comento un porfe que la camel baja puntos >:(
    #chomasaso