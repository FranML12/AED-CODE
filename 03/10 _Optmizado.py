"""
10. Tiempos de Triatlon

Un triatlon es una competicion deportiva en que los participantes realizan tres 
carreras: una de natacion, una ciclista y una pedestre.

Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos) 
logrados en cada etapa por uno de los deportistas participantes.

Con esos datos determinar:

    Tiempo total de la prueba (en formato hh:mm:ss)
    Tiempo maximo y minimo (en segundos)
    Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)

Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones
"""

tiempo_n = input('Ingrese el tiempo de natación en formato mm:ss ')
tiempo_c = input('Ingrese el tiempo de ciclismo en formato mm:ss ')
tiempo_p = input('Ingrese el tiempo pedestre en formato mm:ss ')

# Variables necesarias para calculos posteriores
tiempo_n = int(tiempo_n[:2])*60+int(tiempo_n[3:]) 
tiempo_c = int(tiempo_c[:2])*60+int(tiempo_c[3:])
tiempo_p = int(tiempo_p[:2])*60+int(tiempo_p[3:])

tiempo_segundos = tiempo_n+tiempo_c+tiempo_p

# Calcula tiempo total en (hh:mm:ss)
tiempo_tot = f'{tiempo_segundos//3600}:{(tiempo_segundos%3600)//60}:{(tiempo_segundos%3600)%60}'

tiempo_max = max(tiempo_n, tiempo_c, tiempo_p)
tiempo_min = min(tiempo_n, tiempo_c, tiempo_p)

tiempo_promedio = round(tiempo_segundos/3, 2)
print(f'Tiempo (hh:mm:ss): {tiempo_tot}\nTiempo maximo: {tiempo_max}s\nTiempo minimo: {tiempo_min}s\nTiempo promedio: {tiempo_promedio}s\n')