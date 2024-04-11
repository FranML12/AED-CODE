"""
3. Area de un triangulo

Desarrolle un programa para calcular el area de un triangulo, 
cargando por teclado el valor de la base, 
pero sabiendo que su altura es igual al cuadrado de la base. 
(Observar que la altura no es un dato... 
solo se indica la forma de calcularla de acuerdo a la base que si es un dato).
"""

b = int(input('Ingrese el valor de la base en numeros enteros'))
h = b**2

# Area = base * altura / 2
a = b*h/2

print(f'El area del triangulo es: {a}')