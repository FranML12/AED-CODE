"""
4. Ultimos digitos

¿Como usaria el operador resto (%) para obtener el valor del ultimo digito de un numero entero?
¿Y como obtendria los dos ultimos digitos? Desarrolle un programa que cargue un numero entero por teclado,
y muestre el ultimo digito del mismo (por un lado) y los dos ultimos digitos (por otro lado) 

[Ayuda: ¿cuales son los posibles restos que se obtienen de dividir un numero cualquiera por 10?] 
"""

# Mostrar el ultimo digito
d = int(input('Ingrese un numero entero'))
ud = d%10
print(f'El ultimo digito del numero es: {ud}')
ud = d%100
print(f'Los 2 ultimos digitos del numero son: {ud}')