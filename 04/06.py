"""
6. Analisis de palabra

Se pide un programa que le solicite al usuario que ingrese una palabra. 
Con esa palabra calcular los siguientes puntos:

    Determinar la cantidad de letras que tiene  la palabra.
    Mostrar un mensaje que informe si la palabra termina en vocal.
"""

palabra = input("Ingrese una palabra: ")
palabra_largo = len(palabra)
vocales = ('a', 'e', 'i', 'o', 'u')

# Como dije en 04/05.py, no se si se puede usar "in" en este caso
if palabra[-1] in vocales:
    print(f"La palabra termina en vocal.")
else:
    print(f"La palabra no termina en vocal.")

# Codigo sin utilizacion de in:
""" 
if palabra[-1] == 'a' or palabra[-1] == 'e' or palabra[-1] == 'i' or palabra[-1] == 'o' or palabra[-1] == 'u':
    print(f"La palabra termina en vocal.")
else:    
    print(f"La palabra no termina en vocal.") 
"""