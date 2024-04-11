"""
2. Cuadrado de un binomio

Un binomio al cuadrado (suma) es igual al cuadrado del primer término,
más el doble producto del primero por el segundo más el cuadrado del segundo.

Plantear un script directamente en el shell de Python, que permita mostrar, 
para dos valores a y b, el valor del cuadrado del binomio.
"""

# Tener en cuenta que ^ representa una potencia ej: a^2 = a al cuadrado
a = int(input('Ingresa un numero entero'))
b = int(input('Ingresa otro numero entero'))
b2result = a**2 + 2*a*b + b**2
b2text = f'{a}^2 + 2*{a}*{b} + {b}^2'

print(f'El binomio cuadrado de ({a}+{b})^2 = {b2text} = {b2result}')