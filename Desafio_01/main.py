"""
Desarrolle un programa o script Python que permita cargar por teclado 
un numero entero que representa la  cantidad de segundos que pasaron 
desde un evento dado.  El programa debe convertir esa cantidad de 
segundos  a la cantidad de horas, minutos y segundos que transcurrieron. 
Por ejemplo, si la cantidad de segundos  ingresada es 4452 debera mostrar 
un mensaje que informe que el tiempo transcurrido fue de 1 hora, 14 minutos  
y 12 segundos. Pero la conversion solo debe mostrarse si la cantidad de horas 
totales obtenida es menor o igual a 24. Si esa cantidad de horas totales es 
mayor a 24, el programa debe mostrar un mensaje de la forma "Excedido". 
Se le pedira comprobar su programa para cuatro cantidades de segundos, 
que debera cargar por teclado.

Ademas, el desafio incluye una consigna adicional, en la cual se le pedira 
que haga el proceso inverso: debera tomar tres datos, que seran el valor en horas, 
el valor en minutos y el valor en segundos transcurridos desde un evento dado, 
y su programa debera calcular la cantidad total de segundos a partir de esos datos. 
Por ejemplo, si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 
entonces el resultado a obtener es que la cantidad total de segundos es 16568.
"""

cantidad_segundos = int(input("Ingrese la cantidad de segundos: "))
# Conversion de segundos a horas, minutos y segundos
horas = cantidad_segundos // 3600
minutos = (cantidad_segundos % 3600) // 60
segundos = (cantidad_segundos % 3600) % 60
hhmmss = f"{horas}:{minutos}:{segundos}"

if horas <= 24:
    print(hhmmss)
else:
    print("Excedido")

# Conversion de horas, minutos y segundos a segundos
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))

cantidad_segundos = horas * 3600 + minutos * 60 + segundos
print(cantidad_segundos)