"""
14. Tarifas de Peaje

La empresa de peajes AED Pase-Pase S.R.L, festeja su septimo aniversario y, 
por tal motivo, el dia de hoy ofrece premios a a sus clientes.

Estos premios se calculan de la siguiente manera:

1) Cada vez que pasa un cliente, se sortea un numero del 0 al 9. 
Si el numero coincide con el ultimo digito de la patente del vehiculo, 
se le cobra la tarifa promocional de $50, si no, se le cobra la tarifa estandar de $90

2) Independientemente de la tarifa que deba pagar, si el ultimo digito de la 
patente es 7, entonces recibe un descuento del 50%, en caso contrario un descuento del 10%.

Desarrolle un programa en Python que le solicite al usuario los digitos de 
su patente (unicamente los digitos), simule su paso por el peaje e indique 
el monto a abonar.
"""

import random
patente = input("Ingrese los digitos de su patente: ")
rand_num =  random.randint(0, 9)

# Asumiendo que el beneficio 2 se aplica sobre el beneficio anterior:
if rand_num == int(patente[-1]) and int(patente[-1]) == 7:
    tarifa = 50 * 0.5
    print(tarifa)
elif rand_num == int(patente[-1]):
    tarifa = 50 * 0.9
    print(tarifa)
elif int(patente[-1]) == 7:
    tarifa = 90 * 0.5
    print(tarifa)
else:
    tarifa = 90 * 0.9
    print(tarifa)