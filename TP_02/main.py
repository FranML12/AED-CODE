# Programa en desarrollo: Quitar inputs a la hora de entregar

cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

'''
TENER EN CUENTA:

Insistimos: el programa que tienen que realizar no debe tomar datos desde el teclado por ninguna razón, ni
debe tener un menú de opciones (eso implicaría cargar por teclado la opción elegida). Tampoco debe haber
en ninguna parte nada que solicite al usuario presionar una tecla para continuar. Todos los datos que el
programa debe procesar (y solo esos datos) estarán en el archivo de texto envios.txt cuyo formato y
contenido se describe más abajo
'''

# Determinar el destino en base al formato del cp
def formato_cp(cp):
    def es_letra(c):
        return 'A' <= c <= 'Z' or 'a' <= c <= 'z'

    def es_digito(c):
        return '0' <= c <= '9'

    if len(cp) == 8 and es_letra(cp[0]) and all(es_digito(c) for c in cp[1:5]) and all(es_letra(c) for c in cp[5:]):
        return 'Argentina'
    elif len(cp) == 4 and all(es_digito(c) for c in cp):
        return 'Bolivia'
    elif len(cp) == 9 and all(es_digito(c) for c in cp[0:5]) and cp[5] == '-' and all(es_digito(c) for c in cp[6:]):
        return 'Brasil'
    elif len(cp) == 7 and all(es_digito(c) for c in cp):
        return 'Chile'
    elif len(cp) == 6 and all(es_digito(c) for c in cp):
        return 'Paraguay'
    elif len(cp) == 5 and all(es_digito(c) for c in cp):
        return 'Uruguay'
    else:
        return 'Formato desconocido'
destino = formato_cp(cp)

# Determinar el precio inicial
def tipo_precio(tipo):
    if tipo == 0:
        precio = 1100
    elif tipo == 1:
        precio = 1800
    elif tipo == 2:
        precio = 2450
    elif tipo == 3:
        precio = 8300
    elif tipo == 4:
        precio = 10900
    elif tipo == 5:
        precio = 14300
    elif tipo == 6:
        precio = 17900
    else:
        precio = 0
        print("Tipo de envío inválido.")
    return precio
precio = tipo_precio(tipo)

# Calcular el precio inicial
def precio_inicial():
    if destino == 'Argentina':
        inicial = precio
    elif destino == 'Bolivia' or destino == 'Paraguay':
        inicial = (precio * 0.20) + precio 
    elif destino == 'Uruguay':
        if cp[0] == '1':
            inicial = (precio * 0.20) + precio
        else:
            inicial = (precio * 0.25) + precio
    elif destino == 'Chile':
        inicial = (precio * 0.25) + precio
    elif destino == 'Brasil':
        if cp[0] == '8' or cp[0] == '9':
            inicial = (precio * 0.20) + precio
        elif cp[0] == '4' or cp[0] == '5' or cp[0] == '6' or cp[0] == '7':
            inicial = (precio * 0.30) + precio
        else:
            inicial = (precio * 0.25) + precio
    else:
        inicial = (precio * 0.5) + precio
    return inicial
inicial = precio_inicial()

# Calcular el precio final
def precio_final():
    if pago == 1:
        final = inicial - (inicial * 0.1)
    elif pago == 2:
        final = inicial
    else:
        final = 'Tipo de pago no admitido'
    return final
final = precio_final()

print("País de destino del envío:", destino)
print("Importe inicial a pagar:", int(inicial))
print("Importe final a pagar:", int(final)) 