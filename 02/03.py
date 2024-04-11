"""
3. Ecuacion de Einstein

La famosa ecuacion de Einstein para conversion de una masa m en energia 
viene dada por la formula: 

E = mc2

Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg. 
Desarrolle un programa que lea el valor una masa m en kilogramos y 
obtenga la cantidad de energia E producida en la conversion.
"""

print('--- Calculadora de energía ---')

m = float(input('Ingrese la masa: '))
c = 299792.458

e = m + c**2
print(f'Energía: {e}J')