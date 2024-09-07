""" 
#primero eliminar espacios
#segundo procesar del 0 al 8 (codigo postal)
#tercero del 9 al 28 direccion fisica del destino (cadena de caracteres)

# envios.txt -> proceso:
# quitar espacios, definir tipo de envio, forma de pago, etc
# Todo eso lo pusheo a un array "ENVIO"
# [id=1, pais, tipo, cp, etc..]
# envios [[id=1, pais, tipo, cp, etc..], 
#         [id=2, pais, tipo, cp, etc..]]

# MENU :
    1) cargar un arreglo con envios "enviostp3" (eliminando el viejo y si o 
      si muestra un cartel de esta seguro ?)
    2) cargar por teclado datos de envio(se guarda al final del array sin eliminar ninguno previo)
    3) mostrar todos los array ordenados por codigo postal de menor a mayor
    4) Buscar si existe en el arreglo un registro/objeto cuya dirección de 
      envío sea igual a d y que sea del tipo de envío e, siendo d y e dos valores 
      que se cargan por teclado
    5) Buscar si existe en el arreglo un registro/objeto cuyo código 
      postal sea igual a cp, siendo cp un valor que se carga por teclado
"""
"""if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print('Revise, y reinicie el programa...')
        exit(1)"""
# primero determinar cantidad de datos
# pasar los datos a las listas paralelas 
# empezar con el menu

data = open('envios-tp3.txt', 'rt')
data_line = data.readline()

def main():
    control_type = control(data_line)  # Procesa la primera línea
    print(f"Tipo de control: {control_type}")

    # Procesa el resto de las líneas
    envios = []
    while True:
        envio = arr(data)
        if envio:
            envios.append(envio)
            # Puedes hacer más procesamiento aquí si es necesario
        else:
            break
    print(envios)
    

def es_letra(c):
    return 'A' <= c <= 'Z' or 'a' <= c <= 'z'


def es_mayus(c):
    return 'A' <= c <= 'Z'


def es_digito(c):
    return '0' <= c <= '9'


def borrar_espacios(rango):
    resultado = ''
    for i in rango:
        if i != ' ':
            resultado += i
            
    return resultado

def control(data_line):
    if 'HC' in data_line:
        return 'Hard Control'
    elif 'SC' in data_line:
        return 'Soft Control'
    return 'Tipo de control desconocido'

def arr(data):
    data_line = data.readline()  # Lee la siguiente línea
    if data_line:
        cp = borrar_espacios(data_line[:9])  # Código postal
        direccion = borrar_espacios(data_line[9:29])  # Dirección
        tipo = borrar_espacios(data_line[29:30])  # Tipo de envío
        pago = borrar_espacios(data_line[30:31])  # Método de pago
        return [cp, direccion, tipo, pago]  # Devuelve una tupla con los datos
    else:
        data.close()
        return None  # Si no hay más líneas, devuelve None

def pais(cp):
    if len(cp) == 9 and cp[5] == '-' and es_letra(cp[:5]) and es_letra(cp[6:]):
        pais = 'Brasil'
    elif len(cp) == 8 and es_letra(cp[0]) and es_letra(cp[5:]) and es_digito(cp[1:5]):
        pais = 'Argentina'
    elif es_digito(cp):
        if len(cp) == 7:
            pais = 'Chile'
        elif len(cp) == 6:
            pais = 'Paraguay'
        elif len(cp) == 5:
            pais = 'Uruguay'
            if cp[0] == '1':
                pais = 'Montevideo'
        elif len(cp) == 4:
            pais = 'Bolivia'
        else:
            pais = 'Otros países'
    else:
        pais = 'Otros países'
        
    return pais

def precio_tipo(tipo):
    if tipo == '0':
        precio_tipo = 1100
    elif tipo == '1':
        precio_tipo = 1800
    elif tipo == '2':
        precio_tipo = 2450
    elif tipo == '3':
        precio_tipo = 8300
    elif tipo == '4':
        precio_tipo = 10900
    elif tipo == '5':
        precio_tipo = 14300
    elif tipo == '6':
        precio_tipo = 17900
    else:
        precio_tipo = 0  # Default value if tipo is not valid
    
    return precio_tipo

def precio(pais, cp, precio):
    veinte = ('Bolivia', 'Paraguay', 'Montevideo')
    veintecinco = ('Chile', 'Uruguay')
    
    if pais == 'Brasil':
        if cp[0] in '0123':
            precio += precio * 0.25
        elif cp[0] in '4567':
            precio += precio * 0.3
        else:
            precio += precio * 0.2
    elif pais in veinte:
        precio += precio * 0.2
    elif pais in veintecinco:
        precio += precio * 0.25
    else:
        precio += precio * 0.5
    
    return precio

if __name__ == "__main__":
    main()
    


