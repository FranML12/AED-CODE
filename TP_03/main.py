from funcs import *

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
    return envios, tipo_control


def menu():
    #creo una funcion menu donde printeo el menu y mando la opcion seleccionada del vuelta a la funcion principal(main) para hacer lo que se tenga que hacer
    menu = '\n1) Procesar archivo cargado \n2) Cargar por teclado datos de envio\n3)Mostrar registros ordenados por CP\n4) Busqueda por direccion y tipo de envio\n5)Busqueda por Codigo Postal\n6) Contar cantidad de envios con direccion valida\n7) Mostrar importe final acumulado por tipo de envio\n8) Determinar el mayor tipo de envio\n9) Caulcular importe final promedio e importe por debajo   \n0)Salir\n'
    # usa \n apra bajar de linea
    print(menu)
    opcion = input('Introducir alguna opcion: ')
    if not es_digito(opcion):
        while not es_digito(opcion):
            opcion = input('Introducir alguna opcion (Número): ')
    return int(opcion)


def arr(data):
    data_line = data.readline()
    if data_line:
        cp = str(borrar_espacios(data_line[:9]))  # Código postal
        direccion = borrar_puntos(borrar_espacios(data_line[9:29]))  # Dirección
        tipo = int(borrar_espacios(data_line[29:30]))  # Tipo de envío (convertido a int)
        pago = int(borrar_espacios(data_line[30:31]))  # Método de pago (convertido a int)
        return Envio(cp, direccion, tipo, pago)
    else:
        return None


def opcion(registro):
    # registro = leer_archivo()# aca se lee y se completa el registro
    if registro != []:
        respuesta = input("Hay registros cargados. ¿Desea eliminar los registros existentes y cargar de nuevo desde el archivo? (s/n): ")
        if respuesta.lower() != 's':
            print("Operación cancelada por el usuario.")
        else:
            print("Registros eliminados.")
            registro, tipo_control = leer_archivo()# aca se lee y se completa el registro
    else:
        registro, tipo_control = leer_archivo()# aca se lee y se completa el registro
    return registro, tipo_control


def opcion2(registro):
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


def opcion3(registro):
    ordenamiento_cp(registro)
    # Pregunta cuántos registros se deben mostrar
    mostrar_todo = input("¿Mostrar todos los registros? (s/n): ").lower()
    
    if mostrar_todo == 'n':
        m = int(input("¿Cuántos registros desea mostrar?: "))
    else:
        n = len(registro) 
        m = n  # Muestra todos si selecciona 's'
    
    # Muestra los primeros m registros ordenados
    for i in range(min(m, n)):
        envio = registro[i]
        pais_envio = pais(envio.codigo_postal)
        print(f"{envio}, País: {pais_envio}")


def opcion4(registro):
    d = input('Ingrese una dirrecion de envio (Todo junto, sin espacios ni puntos): ')
    e = int(input('Ingrese un tipo de envio: '))
    # se ingresan los datos pedidos
    for i in range(len(registro)):
        if registro[i].destino.lower() == d.lower() and registro[i].tipo_envio == e: 
            print(f'{registro[i]} existe')
            break
        # con ayuda de la ingeniosa busqueda secuencial se 'busca' si aparece en el arreglo sino suelta un mensaje 
    else:
        print(f'No se encontró ese tipo {d} con el tipo de envío {e} en el arreglo')
            

def opcion5(registro):
    ordenamiento_cp(registro)
    # en esta parte se ordena el registro para aplicar posteirormente una busqueda binaria
    cp_buscar = input("Ingrese el código postal a buscar: ")
    encontrado = False
    izq = 0
    der = len(registro)
    # se asignan los valores de izq y derecha 
    while izq <= der:
        mid = (izq + der) // 2
        if registro[mid].codigo_postal == cp_buscar:
            encontrado = True
            if registro[mid].forma_pago == 1:
                registro[mid].forma_pago = 2
            elif registro[mid].forma_pago == 2:
                registro[mid].forma_pago = 1
            print(f'El registro fue encontrado {registro[mid].codigo_postal}')
            break
            # aca se switchean las formas de pago de 1 a 2 y viceversa
        if cp_buscar < registro[mid].codigo_postal:
            der = mid - 1 # aca vemos que si el valor del que buscamos es menor al del medio, se cambia el limite derecho
        else:
            izq = mid + 1
    if not encontrado:
        print("No se encontró ningún registro con ese código postal.") 

#clean
def opcion6(registro, tipo_control):
    tipos_envio = [0] * 7  # Conteo para cada tipo de envío
    
    if tipo_control == "Hard Control":
        registro_hc = HC(registro)    
        for envio in registro_hc:
            if 0 <= envio.tipo_envio < len(tipos_envio):
                tipos_envio[envio.tipo_envio] += 1
    else:
        for envio in registro:
            if 0 <= envio.tipo_envio < len(tipos_envio):
                tipos_envio[envio.tipo_envio] += 1
        
    for i in range(len(tipos_envio)):
        count = tipos_envio[i]
        print(f"Tipo de envío {i}: {count} pesos")

#clean
def opcion7(registro, tipo_control):
    tipos_envio = [0] * 7  # Conteo para cada tipo de envío
    
    if tipo_control == "Hard Control":
        registro_hc = HC(registro)    
        for envio in registro_hc:
            if 0 <= envio.tipo_envio < len(tipos_envio):
                tipos_envio[envio.tipo_envio] += final_amount(envio.codigo_postal, pais(envio.codigo_postal), envio.tipo_envio, envio.forma_pago)
    else:
        for envio in registro:
            if 0 <= envio.tipo_envio < len(tipos_envio):
                tipos_envio[envio.tipo_envio] += final_amount(envio.codigo_postal, pais(envio.codigo_postal), envio.tipo_envio, envio.forma_pago)
    
    p = []
    
    for i in range(len(tipos_envio)):
        count = tipos_envio[i]
        p.append(f"Tipo de envío {i}: {count} pesos")
    
    return tipos_envio, p

#clean
def opcion8(vector_acumulacion):
    # Verificar si el vector de acumulación existe
    if not vector_acumulacion:
        print("El vector de acumulación no existe. Operación cancelada.")
        return

    # Inicializar variables para encontrar el tipo de envío con el mayor importe final acumulado
    tipo_mayor_importe = None
    mayor_importe = 0

    # Calcular el monto total
    monto_total = 0
    for importe in vector_acumulacion:
        monto_total += importe

    for i in range(len(vector_acumulacion)):
        importe = vector_acumulacion[i]
        if importe > mayor_importe:
            mayor_importe = importe
            tipo_mayor_importe = i

    # Calcular el porcentaje del monto mayor sobre el monto total
    porcentaje_mayor = (mayor_importe / monto_total) * 100

    # Mostrar los resultados
    print(f"Tipo de envío con mayor importe final acumulado: {tipo_mayor_importe}")
    print(f"Importe final acumulado: {mayor_importe}")
    print(f"Porcentaje sobre el monto total: {porcentaje_mayor:.2f}%")

#clean
def opcion9(registro):
    acu = cont = 0 
    for envio in registro:
        acu += int(final_amount(envio.codigo_postal, pais(envio.codigo_postal), envio.tipo_envio, envio.forma_pago)) # una vez iniciado el enumerador, vamos a sumarle el monto final 
    promedio = acu // (len(registro))

    for envio in registro:
        if final_amount(envio.codigo_postal, pais(envio.codigo_postal) , envio.tipo_envio, envio.forma_pago) < promedio:
            cont += 1
    
    print(f'Importe final promedio entre todos los envíos: {int(promedio,)} y {cont} de envíos tuvieron un importe menor a ese promedio.')

    
def main():
    registro = []
    # Inicializamos una variable para almacenar el tipo de control
    tipo_control = None
    op = None

    while op != 0:
        op = menu()      
        if op == 1:
            registro, tipo_control = opcion(registro)
            vector_acumulacion, p = opcion7(registro, tipo_control)
        elif op == 2:
            opcion2(registro)         
        elif str(op) in '3456789':
            if registro == []:
                print("El registro se encuentra vacío y no se pueden realizar búsquedas !.")
            else:
                if op == 3:
                    opcion3(registro)
                elif op == 4:
                    opcion4(registro)
                elif op == 5:
                    opcion5(registro)
                elif op == 6:
                    # Solo llamamos a la función si se ha definido el tipo de control
                    if tipo_control:  
                        opcion6(registro, tipo_control)
                    else:
                        print("No se ha definido el tipo de control.")
                elif op == 7:
                    for i in range(len(p)):
                        print(p[i])
                elif op == 8:
                    opcion8(vector_acumulacion)
                elif op == 9:
                    opcion9(registro)
        else:
            print('\nFinalizado con éxito')


if __name__ == '__main__':
    main()