"""
9. Costos del Proyecto

Una pequena empresa de informatica tiene que desarrollar un sistema de 
informacion y para ello tiene un presupuesto de x pesos para cubrir los 
costos de crear el sistema. Sabiendo que tiene pensado ganar al menos 17% 
por el proyecto, determine cual es el valor maximo que pueden alcanzar los 
costos del proyecto.
"""

presupuesto = int(input('Presupuesto: '))
costo = presupuesto - (presupuesto * 0.17)
ganancia = presupuesto-costo

print(f'El costo del proyecto es: {costo}, la ganancia: {ganancia}')