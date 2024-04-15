"""
5. Tarjeta de Bingo

Realizar un programa que genere 15 numeros aleatorios enteros en el rango 
del 1 al 100, que representaria la tarjeta de bingo de una persona. 
Una vez generados los numeros aleatorios solicitar al usuario que ingrese 
3 numeros enteros y a partir de alli mostrar los siguientes mensajes:

    Si el usuario no marco ninguno de los numeros indicarlo diciendo 
    "El jugador tiene mala suerte, no marco ninguna casilla"
    
    Caso contrario mostrar "El jugador marco algun numero de la tarjeta".
"""
import random

tarjeta = tuple(random.sample(range(1, 101), 15))
print("Tarjeta de Bingo:", tarjeta)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Tengo entendido que esta ficha no incluye "in" pero para evitar lios, lo dejo
if num1 not in tarjeta and num2 not in tarjeta and num3 not in tarjeta:
    print("El jugador tiene mala suerte, no marco ninguna casilla")
else:
    print("El jugador marco algun numero de la tarjeta")