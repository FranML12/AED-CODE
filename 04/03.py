"""
3. Jornal de un Operario

Se necesita desarrollar un programa para el area de recursos humanos de una 
empresa que permita informar el jornal de un determinado operario. 
Usted debera cargar por teclado el codigo de turno que el operario trabajo ese 
dia (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.

La politica de trabajo en la empresa es que los operarios de la misma pueden 
trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno 
nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 
35.50 pesos la hora.
"""

codigo_turno = int(input("Ingrese el código de turno (1: Diurno, 2: Nocturno): "))
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

if codigo_turno == 1:
    jornal = horas_trabajadas * 35.50
else:
    jornal = horas_trabajadas * 40.60

print("El jornal del operario es:", jornal)