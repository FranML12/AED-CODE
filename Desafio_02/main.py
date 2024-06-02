def numSol():
    global num # Declaro que la variable num es global
    num = int(input('Ingrese un numero entero positivo: '))

numSol()

while num < 1:
    print('Se solicito un numero entero positivo.')
    numSol()

def collatz(num):
    if num % 2 == 0:
        num = num//2
    else:
        num = 3*num+1
    return num 

orbita = [num]

while num != 1:
    num = collatz(num) # Actualiza el valor devuelto
    orbita.append(num)

orbitaAv = 0

for i in orbita:
    orbitaAv += i

orbitaLength = len(orbita)
orbitaMax = max(orbita)
orbitaAv = round(orbitaAv/orbitaLength, 1)

print(num, orbita, orbitaLength, orbitaMax, orbitaAv)