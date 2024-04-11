"""
8. Perimetro de un cuadrado

Desarrollar un programa que, conociendo el valor del area (o superficie) de un cuadrado, 
obtenga y muestre el valor del perimetro de ese cuadrado. 
"""

# Importo el modulo de funciones matematicas de python
import math 

area = float(input('Area del cuadrado: '))
lado = math.sqrt(area)

print(f'Lado del cuadrado: {lado}')