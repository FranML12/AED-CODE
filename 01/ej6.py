"""
6. Viaje Cordoba-Rosario

Un vehiculo parte de la ciudad de Cordoba y se dirige a Rosario por autopista. 
La distancia aproximada entre ambas ciudades es de 400 kilometros. 
El vehiculo se desplaza con velocidad promedio de 122 km/h.
Desarrolle un programa que calcule el tiempo total en horas que demorara ese vehiculo en llegar a Rosario. 
De nuevo, no es necesario convertir a horas, minutos y segundos: 
exprese en resultado como un numero real, tal cual lo haya obtenido del calculo.
"""

dist = 400
vel = 122
tiem = 400/122
roundT = "%.2f" % tiem # Redondea a 2 decimales el tiempo
print(f'El tiempo que tarda el auto en llegar es de {roundT} horas') 