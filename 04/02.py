"""
2. Suma - Division - Potencia

Se necesita desarrollar un programa que permita calcular la suma de tres numeros. 
Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), 
en caso contrario elevar el resultado al cubo.
"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

suma = num1 + num2 + num3

if suma > 10:
    resultado = suma // 2
else:
    resultado = suma ** 3

print("El resultado es:", resultado)