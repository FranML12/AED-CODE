"""
7. Calculo presupuestario

En un hospital existen 3 areas de servicios: Urgencias, Pediatria y Traumatologia. 
El presupuesto anual del hospital se reparte de la siguiente manera:

Area-Presupuesto

Urgencias 37%

Pediatria 42%

Traumatologia 21%

Cargar por teclado el monto del presupuesto total del hospital, 
y calcular y mostrar el monto que recibira cada area.
"""

presupuesto = int(input('Ingrese el presupuesto del hospital: '))
urgencias_p = presupuesto/100 * 37
pediatria_p = presupuesto/100 * 42
traumatologia_p = presupuesto/100 * 21

print(f'Area - Presupuesto\nUrgencias: {urgencias_p}\nPediatria: {pediatria_p}\nTraumatologia: {traumatologia_p}')