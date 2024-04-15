"""
7. Tirada de moneda

Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. 
Permitir que un jugador apueste a cara o cruz y luego informar si acerto 
o no con su apuesta.
"""

import random

moneda = random.choice(('cara', 'cruz'))
apuesta = input("Ingrese su apuesta (cara o cruz): ")

if moneda == apuesta:
    print("¡Acertaste!")
else:
    print("¡Fallaste!")