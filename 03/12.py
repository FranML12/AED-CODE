"""
12. Calculo de Posta de Natacion

En la disciplina olimpica una de las pruebas mas esperadas en la natacion es la posta 4x100. 
En esta disciplina el equipo ganador registro los siguientes tiempos en cada estilo:

    Espalda: 52 segundos 15 centesimas.
    Pecho: 1 minuto 2 segundos 75 centesimas.
    Mariposa: 59 segundos 80 centesimas.
    Libre: 48 segundos 15 centesimas.

Usted debe averiguar el tiempo total de la carrera del equipo ganador y 
representarlo en minutos, segundos y centesimas.


Para recordar:

    1 minutos son 60 segundos.
    1 segundo son 100 centesimas.

"""

# Estilos en centesimas:
espalda = 52*100+15
pecho = 1*60*100+2*100+75
mariposa = 59*100+80
libre = 48*100+15

total = espalda+pecho+mariposa+libre
min_tot = int((total/100)//60)
seg_tot = int((total/100)%60)
cent_tot = int(((total%100)%60))

print(total)
print(min_tot, seg_tot, cent_tot)