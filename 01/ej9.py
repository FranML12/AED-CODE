"""
9. Area de un rectangulo

Desarrollar un programa que, conociendo el valor del perimetro de un rectangulo y 
el valor de uno de los lados de ese rectangulo, 
calcule y muestre el valor del area (o superficie) de ese rectangulo.
"""

perimetro = float(input('Ingrese el valor del perimetro del rectangulo: '))
lado1 = float(input('Ingrese el valor del lado del rectangulo: '))
lado2 = perimetro-lado1
area = lado1*lado2

if lado1 > perimetro:
    print('El lado no puede medir mas que el perimetro')
else:
    print(f'El area del rectangulo es: {area}')