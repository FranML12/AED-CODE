"""
4. Temperatura diaria

Se solicita realizar un programa que permita ingresar tres temperaturas 
correspondientes a diferentes momentos de un dia y determinar:

    Cual es el promedio de las temperaturas.
    Si existe alguna temperatura que sea mayor al promedio.
"""

temp1 = float(input("Ingrese la temperatura del primer momento del día: "))
temp2 = float(input("Ingrese la temperatura del segundo momento del día: "))
temp3 = float(input("Ingrese la temperatura del tercer momento del día: "))

promedio = (temp1 + temp2 + temp3) / 3
max_temp = max(temp1, temp2, temp3)
print("El promedio de las temperaturas es:", round(promedio, 2), "°C")

if max_temp > promedio:
    print("Hay una temperatura mayor al promedio:", max_temp, "°C")
else:
    print("No hay ninguna temperatura mayor al promedio.")