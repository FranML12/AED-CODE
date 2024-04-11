"""
6. Calculo de sueldo

Se conoce el monto del salario actual de un empleado, el nombre del empleado y 
el area funcional al cual pertenece. Se pide calcular el nuevo salario del empleado 
sabiendo que obtuvo un incremento del 8% sobre su salario actual y un descuento de 
2.5% por servicios, informando los resultados con el formato que se especifica a 
continuacion:

       Nombre Empleado:  xxxxxxxxx            Nuevo Salario: $ xxx             

       Area Funcional:  xxxxxxxxxxxx

       Salario Actual: $ xxxx                      
"""

nombre_e = input('Nombre del empleado: ')
area_e = input('Area funcional del empleado: ')
salario_e = int(input('Salario del empleado: '))
nuevo_salario_e = salario_e + (salario_e * 0.08)
salario_servicio = nuevo_salario_e - nuevo_salario_e *0.025

print(f'Nombre Empleado: {nombre_e}\tNuevo Salario: ${salario_servicio}\nArea Funcional: {area_e}\nSalario Actual: ${salario_e}')