"""
10. Calculo de Ganancias de Pelicula

Una empresa dedicada al pago de ganancias por las peliculas que se realizan en los estudios, 
necesita un sistema que permita cargar el total que la pelicula recaudo, 
el nombre del participante de la pelicula que se tiene que abonar, 
el porcentaje que se le debe pagar. Con esos datos mostrar el nombre del actor 
y el monto que recibira de las ganancias
"""

total = int(input('Inserte ganancia total: '))
participante = input('Inserte nombre del participante: ')
participante_porcentaje = int(input('Inserte % para el participante: '))

participante_ganancia = participante_porcentaje*total/100
print(f'El participante {participante} ganó ${participante_ganancia}')