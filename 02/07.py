"""
7. Votacion en el Congreso

En el Congreso se vota la sancion de una ley muy importante. 
Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra, 
e informe el porcentaje obtenido en cada caso.
"""

vf = int(input('Votos a favor: '))
vc = int(input('Votos en contra: '))
vt = vf + vc

# Aplico regla de 3
porcentaje_fav = vf*100/vt
porcentaje_con = vc*100/vt
print(f'vf: {porcentaje_fav}, vc: {porcentaje_con}')