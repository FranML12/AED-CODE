from funcs import *

class Envio:
    def __init__(self, cp: str, destino: str, tipo: int, pago: int):
        self.codigo_postal = cp
        self.destino = destino
        self.tipo_envio = tipo
        self.forma_pago = pago
#inicializo la clase de envios y agregro los objetos respectivos y les asigno las variables de los futuros atributos
    def __str__(self) -> str:
        return f"{self.codigo_postal}, {self.destino}, {self.tipo_envio}, {self.forma_pago}"
#escribo el __str__ para cuando se quiera printear o coso 


def leer_archivo():
    data = open('envios-tp3.txt', 'rt')
    data_line = data.readline()
    tipo_control = control(data_line)
    print(tipo_control)    

    envios = []
    while True:
        envio = arr(data)
        if envio:
            envios.append(envio)
        else:
            break

    data.close()  # Cierra el archivo al terminar
    return envios


def menu():
    #creo una funcion menu donde printeo el menu y mando la opcion seleccionada del vuelta a la funcion principal(flores_maximo) para hacer lo que se tenga que hacer
    menu = '1) cargar un arreglo con envios "enviostp3" (eliminando el viejo y si o si muestra un cartel de esta seguro ?) \n2) cargar por teclado datos de envio(se guarda al final del array sin eliminar ninguno previo)\n3) mostrar todos los array ordenados por codigo postal de menor a mayor\n4) Buscar si existe en el arreglo un registro/objeto cuya dirección de envío sea igual a d y que sea del tipo de envío e, siendo d y e dos valores que se cargan por teclado\n5) Buscar si existe en el arreglo un registro/objeto cuyo código postal sea igual a cp, siendo cp un valor que se carga por teclado\n0)Salir'
    # usa \n apra bajar de linea
    print(menu)
    opcion = input('Introducir alguna opcion: ')
    if not es_digito(opcion):
        while not es_digito(opcion):
            opcion = input('Introducir alguna opcion (Número): ')
    return int(opcion)


def control(data_line):
    if 'HC' in data_line:
        return 'Hard Control'
    elif 'SC' in data_line:
        return 'Soft Control'
    return 'Tipo de control desconocido'


def arr(data):
    data_line = data.readline()
    if data_line:
        cp = borrar_espacios(data_line[:9])  # Código postal
        direccion = borrar_puntos(borrar_espacios(data_line[9:29]))  # Dirección
        tipo = int(borrar_espacios(data_line[29:30]))  # Tipo de envío (convertido a int)
        pago = int(borrar_espacios(data_line[30:31]))  # Método de pago (convertido a int)
        return Envio(cp, direccion, tipo, pago)
    else:
        return None

# FUNCION MAL PLANTEADA REVISAR!!!!

# La opcion 1 es el postre (G. Golds) !IMPORTANT
def guada_goldmorthi1(registro):
    # registro = leer_archivo()# aqui se lee y se completa el registro
    if registro != []:
        respuesta = input("Hay registros cargados. ¿Desea eliminar los registros existentes y cargar de nuevo desde el archivo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada por el usuario.")
        else:
            print("Registros eliminados.")
            registro = leer_archivo()# aqui se lee y se completa el registro
    else:
        registro = leer_archivo()# aqui se lee y se completa el registro
    return registro


def guada_boiero2(registro):
    # aca validamos si el registro existe o no, para cargar o no los datos que se piden cargar
    cp = input("ingrese el codigo postal: ")
    dirreccion = input('Ingrese la hermosisima dirrecion: ')
    while True:
            # cargamos datos de tipo de envio, si son validos devuelve el valor, sino devuelve un none
        tipo_de_envio = verificador(int(input("Ingrese el tipo de envio del 0 al 6 \nCarta Simple: 0 (menos de 20 gramos), 1 (20gr <= peso < 150gr), 2 (150gr <= peso < 500gr)\nCarta Certificada: 3 (peso < 150gr), 4 (150gr <= peso < 500gr)\nCarta Expresa: 5 (peso < 150gr), 6 (150gr <= peso < 500gr)\nIngrese el tipo: ")),0,6)
        if tipo_de_envio is None:
            print("Tipo de envio invalido, ingresar nuevamente: ")
            continue
        else:
            break
    while True:
        # cargamos la forma de pago, si es valida devuelve la forma (1 o 2), sino devuelve un none
        forma_de_pago = verificador(int(input("ingrese la forma de pago del 1 al 2 (1(efectivo), 2(carton)): ")),1,2)
        if forma_de_pago is None:
            print("Tipo de envio invalido, ingresar nuevamente")
            continue
        else:
            break
    registro.append(Envio(cp ,dirreccion ,tipo_de_envio , forma_de_pago))


def lucia_truco3(registro):
    """
    Muestra todos los registros del arreglo ordenados por código postal de menor a mayor.
    Cada registro se muestra en una sola línea junto con el país al que pertenece el código postal.
    Se puede elegir si mostrar todos los registros o solo los primeros m registros.
    """
    
    n = len(registro)
    
    # Ordenamiento tipo Bubble Sort aplicado al arreglo de envíos
    for i in range(n - 1):
        ordenado = True
        for j in range(n - i - 1):
            if registro[j].codigo_postal > registro[j + 1].codigo_postal:
                # Intercambia los objetos si el código postal es mayor
                registro[j], registro[j + 1] = registro[j + 1], registro[j]
                ordenado = False
        if ordenado:
            break  # Si ya está ordenado, termina el ciclo
    
    # Pregunta cuántos registros se deben mostrar
    mostrar_todo = input("¿Mostrar todos los registros? (s/n): ").lower()
    
    if mostrar_todo == 'n':
        m = int(input("¿Cuántos registros desea mostrar?: "))
    else:
        m = n  # Muestra todos si selecciona 's'
    
    # Muestra los primeros m registros ordenados
    for i in range(min(m, n)):
        envio = registro[i]
        pais_envio = pais(envio.codigo_postal)
        print(f"{envio}, País: {pais_envio}")


def I132qew44(registro):
    d = input('Ingrese una dirrecion de envio (TODO JUNTO SIN ESPACIOS NI SIQUIERA ENTRE EL NOMBRE Y LOS NUMEROS): ')
    e = int(input('Ingrese un tipo de envio: '))
    # se ingresan los datos pedidos
    for i in range(len(registro)):
        if registro[i].destino.lower() == d.lower() and registro[i].tipo_envio == e: 
            print(f'HENORABUENA, existe {registro[i]} y es mas, tecnicamente podriamos llegar a la conclucion de que, en efecto, se encuentra en el arreglo 🤓👆!!')
            break
        # con ayuda de la ingeniosa busqueda secuencial se 'busca' si aparece en el arreglo sino suelta un mensaje 
    else:
        print(f'No se encontro ese tipo {d} con el tipo de envio {e} en el arreglo')
            

def amerigo_jackson5(registro):#------------------>controlar si anda, teoricamente anda perfecto pero chequear
    cp_buscar = input("Ingrese el código postal a buscar: ")
    encontrado = False
    izq = 0
    der = len(Envio.codigo_postal)
    # se asignan los valores de izq y derecha
    while True:
        mid = izq + der // 2
        if Envio[mid].codigo_postal == cp_buscar:
            print(Envio)
            encontrado = True
            if Envio[mid].forma_pago == 1:
                Envio[mid].forma_pago = 2
            elif Envio[mid].forma_pago == 2:
                Envio[mid].forma_pago = 1 
            # aqui se switchean las formas de pago de 1 a 2 y viceversa
        if cp_buscar < Envio[mid].codigo_postal:
            der -= mid # aqui vemos que si el valor del que buscamos es menor al del medio, se cambia el limite derecho
        else:
            izq += mid
        break
    if not encontrado:
        print("No se encontró ningún registro con ese código postal.")


""" def mateo_haro6(registro, tipo_control):
    # Creamos un contador para cada tipo de envío
    tipos_envio = [0] * 7  # Suponiendo que hay 7 tipos de envío (0 a 6)

    if tipo_control == "Hard Control":
        registro = obtener_registros_validos(registro)
    
    # Recorremos el registro de envíos y contamos cada tipo
    for envio in registro:
        tipo_envio = envio.tipo_envio  # Accedemos al atributo 'tipo' correctamente con notación de puntos
        if 0 <= tipo_envio < len(tipos_envio):
            tipos_envio[tipo_envio] += 1
    
    # Mostramos los resultados
    for i in range(len(tipos_envio)):
        print(f"Tipo de envío {i}: {tipos_envio[i]} envíos")
 """

def mateo_haro6(registro, tipo_control):
    tipos_envio = [0] * 7  # Conteo para cada tipo de envío
    
    if tipo_control == "Hard Control":
        registro =valida_para_hc(registro)
        print(registro)
    
    for envio in registro:
        if 0 <= envio.tipo_envio < len(tipos_envio):
            tipos_envio[envio.tipo_envio] += 1
    
    for i, count in enumerate(tipos_envio):
        print(f"Tipo de envío {i}: {count} envíos")


def luz_balastegui7(registro, tipo_control, envios_validos_hc=None):
    """
    Determina el importe final acumulado de cada uno de los siete tipos de envío.
    
    Si el tipo de control es 'Hard Control', solo considera los envíos con direcciones válidas.
    Si el tipo de control es 'Soft Control', considera todos los envíos, independientemente de la validez de la dirección.
    
    registro: lista de envíos.
    tipo_control: string que indica si es 'Hard Control' o 'Soft Control'.
    envios_validos_hc: lista de envíos con direcciones válidas en caso de 'Hard Control'.
    """
    # Creamos un acumulador para cada tipo de envío
    acumuladores = [0] * 7  # Un vector de acumuladores para los tipos de envío del 0 al 6

    if tipo_control == "Hard Control" and envios_validos_hc is not None:
        # Acumulamos solo los envíos con direcciones válidas
        for envio in envios_validos_hc:
            acumuladores[envio.tipo_envio] += envio.forma_pago

    elif tipo_control == "Soft Control":
        # Acumulamos todos los envíos, sin importar la validez de la dirección
        for envio in registro:
            acumuladores[envio.tipo_envio] += envio.forma_pago

    # Mostrar el resultado de los acumuladores
    for i in range(7):
        print(f"Acumulador del tipo de envío {i}: {acumuladores[i]} pagos acumulados")


def flores_maximo():
    registro = []
    tipo_control = None  # Inicializamos una variable para almacenar el tipo de control
    op = None

    while op != 0:
        op = menu()      
        if op == 1:
            registro = guada_goldmorthi1(registro)
            if registro:
                # Determina el tipo de control tras cargar el archivo
                d = open('envios-tp3.txt', 'rt')
                d_line = d.readline()
                tipo_control = control(d_line)
                d.close()
            print(tipo_control)
        elif op == 2:
            guada_boiero2(registro)         
        elif str(op) in '3456789':
            if registro == []:
                print("El registro se encuentra vacío y no se pueden realizar búsquedas, bobi !.")
            else:
                if op == 3:
                    lucia_truco3(registro)
                elif op == 4:
                    I132qew44(registro)
                elif op == 5:
                    amerigo_jackson5(registro)
                elif op == 6:
                    if tipo_control:  # Solo llamamos a la función si se ha definido el tipo de control
                        mateo_haro6(registro, tipo_control)
                    else:
                        print("No se ha definido el tipo de control.")
                elif op == 7:
                    luz_balastegui7()
                elif op == 8:
                    pass
                elif op == 9:
                    pass
        else:
            print('\nFinalizado con éxito')



if __name__ == '__main__':
    flores_maximo()

# TODO EMPEZO EN CRIMEA Y TERMINO EN CRIMEA!!! 
# NO MAS A LA GUERRA PORFAVOR!