"""
5. Calculo de angulos

Se sabe que la suma de dos angulos desconocidos (alfa + beta) 
es igual a cierto valor x que se carga por teclado. 
Ademas se sabe que la diferencia entre esos mismos dos angulos (alfa - beta) 
es igual a otro valor y que tambien se carga por teclado. 
Desarrolle un programa que dados los valores x e y, 
determine el valor de los dos angulos alfa y beta. No es necesario convertir a grados, 
minutos y segundos el valor de cada angulo: 
expreselos como numeros reales, tal cual hayan sido obtenidos.
"""

x = float(input('Ingrese valor de x: '))
y = float(input('Ingrese valor de y: '))

b = (y-x)/-2
a = x-b
# a2 = y+b
print(a)
print(b)

"""
Para resolverlo planteamos:
x = a + b
y = a-b

Entonces, reemplazamos:
(Obtener Alfa)
x-b = a
y+b = a

(Obtener Beta)
x-b = y+b
x = y+2b

-2b = y-x
b = (y-x)/-2
"""