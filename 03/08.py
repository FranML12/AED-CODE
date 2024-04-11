"""
8. Calculo Distancia de Viaje

Un persona cautivada por los paisajes argentinos se le ocurrio la loca idea de 
unir los puntos mas extremos (Ushuahia y La Quiaca) en bicicleta, es decir se 
propuso hacer 3641.3 Km en bicicleta.

Nuestro aventurero efectivamente inicio la travesia pero se accidento y solo 
recorrio x metros segun su GPS. 

Usted debe solicitar ese valor x e informar cuantos kilometros y metros recorrio 
nuestro aventurero y que porcentaje represento lo recorrido del total de kms a 
recorrer de Ushuahia a La Quiaca (para el porcentaje usted debera realizar los 
calculos en metros).
"""

distancia = 3641.3
recorrido = float(input('Ingrese la cantidad recorrida (metros): '))
recorrido_km = recorrido/1000
porcentaje = round(100*recorrido_km/3641.3, 2)

print(f'Ha recorrido {recorrido}m, {recorrido_km}km, {porcentaje}% de la distancia total.')