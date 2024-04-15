"""
9. Edad minima

Ingresar por teclado las edades de 3 participantes de un concurso.

Informar si todos cumplen con la edad minima establecida para el mismo, 
tambien ingresada por teclado.
"""

edad_minima = int(input("Ingrese la edad minima para el concurso: "))
edad1 = int(input("Ingrese la edad del primer participante: "))
edad2 = int(input("Ingrese la edad del segundo participante: "))
edad3 = int(input("Ingrese la edad del tercer participante: "))

if edad1 >= edad_minima and edad2 >= edad_minima and edad3 >= edad_minima:
    print("Todos cumplen con la edad minima.")
else:
    print("No todos cumplen con la edad minima.")