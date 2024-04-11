"""
13. Triangulo Rectangulo

Desarrollar un programa que, ingresando los dos catetos de un 
triangulo rectangulo, informe:

    Valor de la hipotenusa (redondeado a 2 decimales)

    Valor del lado mayor

    Valor del lado menor
"""

from math import sqrt as raiz


a = float(input('Ingrese cateto a: '))
b = float(input('Ingrese cateto b: '))
max = max(a,b)
min = min(a,b)
c = round(raiz(a**2 + b**2), 2) # Utilizo la libreria para resolver raiz
c1 = round(pow((a**2 + b**2), 1/2), 2) # Aplico la propiedad de raiz
print('Hipotenusa: ', c)
print('Hipotenusa: ', c1)
print(f'Cateto mayor: {max}, cateto menor: {min}')