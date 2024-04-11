"""
4. Duracion de un vuelo

Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo 
(hora y minutos), determine cual es su duracion en minutos. Si el viajero necesita luego 
45 minutos mas para ir del aeropuerto al hotel que ha reservado, 
¿a que hora llegara al mismo?
"""

horario_salida = input('Ingrese horario de salida (hh:mm): ')
hora_salida = int(horario_salida[:2]) * 60 
min_salida = int(horario_salida[3:])
hora_salida = hora_salida+min_salida

horario_llegada = input('Ingrese horario de llegada (hh:mm): ')
hora_llegada = int(horario_llegada[:2]) * 60 
min_llegada = int(horario_llegada[3:])
hora_llegada = hora_llegada+min_llegada

duracion = hora_llegada-hora_salida+45
print(duracion//60, duracion%60)