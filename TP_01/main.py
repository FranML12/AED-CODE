cp = input("Ingrese el código postal del lugar de destino: ")
#direccion = input("Dirección del lugar de destino: ")
# tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
#pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

# Determinar el precio inicial
""" if tipo == 0:
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
    print("Tipo de envío inválido.")"""

# 8 caracteres. La primera letra identifica a la provincia (las letras "I" y "O" no se utilizan), los cuatro dígitos a la ciudad, y las tres letras finales al frente de manzana o paraje o casilla de correo.
if len(cp) == 8:
    destino = 'Argentina'
    if cp[0] == 'A':
        provincia = 'Salta'
    elif cp[0] == 'B':
        provincia = 'Buenos Aires'
    elif cp[0] == 'C':
        provincia = 'Ciudad Autónoma de Buenos Aires'
    elif cp[0] == 'D':
        provincia = 'San Luis'
    elif cp[0] == 'E':
        provincia = 'Entre Ríos'
    elif cp[0] == 'F':
        provincia = 'La Rioja'
    elif cp[0] == 'G':
        provincia = 'Santiago del Estero'
    elif cp[0] == 'H':
        provincia = 'Chaco'
    elif cp[0] == 'J':
        provincia = 'San Juan'
    elif cp[0] == 'K':
        provincia = 'Catamarca'
    elif cp[0] == 'L':
        provincia = 'La Pampa'
    elif cp[0] == 'M':
        provincia = 'Mendoza'
    elif cp[0] == 'N':
        provincia = 'Misiones'
    elif cp[0] == 'P':
        provincia = 'Formosa'
    elif cp[0] == 'Q':
        provincia = 'Neuquén'
    elif cp[0] == 'R':
        provincia = 'Río Negro'
    elif cp[0] == 'S':
        provincia = 'Santa Fe'
    elif cp[0] == 'T':
        provincia = 'Tucumán'
    elif cp[0] == 'U':
        provincia = 'Chubut'
    elif cp[0] == 'V':
        provincia = 'Tierra del Fuego'
    elif cp[0] == 'W':
        provincia = 'Corrientes'
    elif cp[0] == 'X':
        provincia = 'Córdoba'
    elif cp[0] == 'Y':
        provincia = 'Jujuy'
    elif cp[0] == 'Z':
        provincia = 'Santa Cruz'
elif len(cp) == 4:
    destino = 'Bolivia'
elif len(cp) == 9:
    destino = 'Brasil'
elif len(cp) == 7:
    destino = 'Chile'
elif len(cp) == 6:
    destino = 'Paraguay'
elif len(cp) == 5:
    destino = 'Uruguay'
else:
    destino = 'Otro país'

"""
País destino Precio (en pesos)
Bolivia, Paraguay, Uruguay (Montevideo) +20%
Chile, Uruguay (no Montevideo) +25%
Brasil (regiones 8 y 9) +20%
Brasil (regiones 0, 1, 2 y 3) +25%
Brasil (regiones 4, 5, 6 y 7) +30%
Otros países +50%
"""


# """ print("País de destino del envío:", destino)
# print("Provincia destino:", provincia)
# print("Importe inicial a pagar:", inicial)
# print("Importe final a pagar:", final) """