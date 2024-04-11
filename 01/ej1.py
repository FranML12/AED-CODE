""" 
1. División con resto

Plantear un script (directamente en el shell de Python) que permita informar, 
para dos valores a y b el resultado de la división a/b y el resto de esa divisón. 
"""

a = int(input('Inserta el dividendo'))
b = int(input('Inserta el divisor'))

div = a/b
res = a%b

print(f'Resultado: {div}; Resto: {res}')