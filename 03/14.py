"""
14. Sumador de Angulos

Se desea un programa que dados 2 angulos expresados en grados minutos y segundos, 
informe la suma de ambos en grados minutos y segundos.

A modo de ejemplo se agrega la siguiente grafica:

Tener en cuenta que en el algoritmo implementado no necesariamente hay que seguir 
el mecanismo empirico propuesto por la imagen.
"""

angulo_a = input('Ingrese el angulo en gg mm ss (respetando el espaciado): ')
angulo_b = input('Ingrese el angulo en gg mm ss (respetando el espaciado): ')

angulo_c_grad = int(angulo_a[:2])+int(angulo_b[:2])
angulo_c_min = int(angulo_a[3:5])+int(angulo_b[3:5])
angulo_c_seg = int(angulo_a[6:])+int(angulo_b[6:])

angulo_c_seg_calc = angulo_c_seg%60 # Funciona
angulo_c_min_calc = (angulo_c_min + angulo_c_seg // 60)%60
angulo_c_grad_calc = angulo_c_grad+(angulo_c_min + angulo_c_seg // 60)//60

print(angulo_c_grad_calc)
print(angulo_c_min_calc)
print(angulo_c_seg_calc)


