"""
10. Terreno

Se ingresan las medidas de frente y fondo de un terreno.

Determinar si es cuadrado o rectangular y calcular su superficie.
"""

frente = float(input("Ingrese la medida de frente del terreno: "))
fondo = float(input("Ingrese la medida de fondo del terreno: "))
superficie = frente * fondo

if frente == fondo:
    print(f"El terreno es cuadrado y su superficie es de {superficie} m2.")
else:
    print(f"El terreno es rectangular y su superficie es de {superficie} m2.")