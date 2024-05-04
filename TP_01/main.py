cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

# Determinar el país y la provincia de destino
if len(cp) == 4:
    destino = 'Bolivia'
    provincia = 'No aplica'
elif len(cp) == 5:
    if cp[0] == 1:
        destino = 'Uruguay'
        provincia = 'Montevideo'
    else:
        destino = 'Uruguay'
        provincia = 'No aplica'
elif len(cp) == 6:
    destino = 'Paraguay'
    provincia = 'No aplica'
elif len(cp) == 7:
    destino = 'Chile'
    provincia = 'No aplica'
elif len(cp) == 8:
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
    else:
        provincia = 'No aplica'
elif len(cp) == 9:
    destino = 'Brasil'
    provincia = 'No aplica'
else:
    destino = 'Otro país'
    provincia = 'No aplica'

# Determinar el precio inicial
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

# Calcular el precio inicial
if destino == 'Argentina':
    inicial = precio
elif destino == 'Bolivia' or destino == 'Paraguay':
    inicial = (precio * 0.20) + precio 
elif destino == 'Uruguay':
    if provincia == 'Montevideo':
        inicial = (precio * 0.20) + precio
    else:
        inicial = (precio * 0.25) + precio
elif destino == 'Chile':
    inicial = (precio * 0.25) + precio
elif destino == 'Brasil':
    if cp[0] == 8 or cp[0] == 9:
        inicial = (precio * 0.20) + precio
    else:
        inicial = (precio * 0.25) + precio
else:
    inicial = (precio * 0.5) + precio

# Calcular el precio final
if pago == 1:
    final = inicial - (inicial * 0.1)
elif pago == 2:
    final = inicial
else:
    final = 'Tipo de pago no admitido'

print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", int(inicial))
print("Importe final a pagar:", int(final)) 