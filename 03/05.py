"""
5. Control electoral

Desarrollar un programa de control electoral en un centro vecinal, 
en el que se ingresen, para cierto candidato: apellido, nombre y cantidad de votos. 
Luego presentar en pantalla un resumen que muestre: iniciales del candidato, 
cantidad de votos entre parentesis, y debajo una linea con tantas  "x" 
como votos obtenidos (por ejemplo, el candidato obtuvo 4 votos, 
debera aparecer una linea como esta:  "xxxx"  con cuatro letras "x") 
(Asumimos que en el centro vecinal no hay demasiados electores, 
de forma que podamos estar seguros que no habra miles o millones de votos... 
solo unos pocos para darle sentido al enunciado).
"""

apellido = input('Ingresar apellido del candidato: ')
nombre = input('Ingresar nombre del candidato: ')
votos = int(input('Ingresar nro de votos candidato: '))

inicial_a = apellido[0]
inicial_n = nombre[0]

votos_x = 'x' * votos

print(f'El candidato {inicial_n}{inicial_a}, obtuvo {votos} votos.\n{votos_x}')