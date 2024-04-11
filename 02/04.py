"""
4. Polinomio de segundo grado

Desarrollar un programa que cargue por teclado los coeficientes 
a, b y c de un polinomio de segundo grado, 
y calcule y muestre el valor del polinomio en el punto x (cargando tambien x por teclado). 
Ademas, para el mismo polinomio, calcule y muestre el valor del discriminante
de la formula para el calculo de las raices de la ecuacion.
"""

a = float(input('Ingrese el coeficiente a: '))
b = float(input('Ingrese el coeficiente b: '))
c = float(input('Ingrese el coeficiente c: '))

x = float(input('Ingrese un valor para x: '))

y = a * x**2 + b * x + c

print(f'el valor de y cuando x sea {x} es: {y}')
