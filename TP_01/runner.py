import subprocess
import sys
import os
import io

# Directorio donde se almacenan los programas entregados por los estudiantes
SOURCES = "TP_01"

with os.scandir(SOURCES) as entries:
    for entry in entries:
        print(entry.name.encode('latin-1', errors='replace').decode('latin-1'), entry.is_file(), entry.is_dir())



# Lotes de prueba contra los que serán corridos los programas de los estudiantes.
# ("CP\nDirección\nTipo de envío\nForma de pago\n", Contexto, r1, r2, r3, r4)
BATCH = (
  ("L2445LHG\nSan Martin 856\n0\n1\n", "01.) Argentina - Tipo 0 - Pago 1", "Argentina", "La Pampa", "1100", "990"),
  ("V8621PRT\nBelgrano 219\n1\n2\n", "02.) Argentina - Tipo 1 - Pago 2", "Argentina", "Tierra del Fuego", "1800", "1800"),
  ("E4272WSG\nRoca 1734\n2\n2\n", "03.) Argentina - Tipo 2 - Pago 2", "Argentina", "Entre Ríos", "2450", "2450"),
  ("C2365CQR\nSarmiento 26\n3\n1\n", "04.) Argentina - Tipo 3 - Pago 1", "Argentina", "Ciudad Autónoma de Buenos Aires", "8300", "7470"),
  ("S3375LKE\nGuemes 27\n4\n2\n", "05.) Argentina - Tipo 4 - Pago 2", "Argentina", "Santa Fe", "10900", "10900"),
  ("G8537AFY\nGeneral Paz 7\n5\n2\n", "06.) Argentina - Tipo 5 - Pago 2", "Argentina", "Santiago del Estero", "14300", "14300"),
  ("Q8363AWJ\nAlvear 9836\n6\n1\n", "07.) Argentina - Tipo 6 - Pago 1", "Argentina", "Neuquén", "17900", "16110"),
  ("5561\nSucre 345\n4\n1\n", "08.) Bolivia - Tipo 4 - Pago 1", "Bolivia", "No aplica", "13080", "11772"),
  ("235528\nTacuarí 1376\n5\n1\n", "09.) Paraguay - Tipo 5 - Pago 1", "Paraguay", "No aplica", "17160", "15444"),
  ("12742\nArtigas 6\n6\n2\n", "10.) Uruguay (Montevideo) - Tipo 6 - Pago 2", "Uruguay", "No aplica", "21480", "21480"),
  ("3359437\nO'Higgins 3387\n0\n2\n", "11.) Chile - Tipo 0 - Pago 2", "Chile", "No aplica", "1375", "1375"),
  ("57485\nViana 4\n4\n1\n", "12.) Uruguay (no Montevideo) - Tipo 4 - Pago 1", "Uruguay", "No aplica", "13625", "12262"),
  ("88437-989\nPelé 65\n3\n1\n", "13.) Brasil (Región 8) - Tipo 3 - Pago 1", "Brasil", "No aplica", "9960", "8964"),
  ("13517-503\nCardoso 288\n6\n2\n", "14.) Brasil (Región 1) - Tipo 6 - Pago 2", "Brasil", "No aplica", "22375", "22375"),
  ("52178-105\nPedro II 77\n1\n1\n", "15.) Brasil (Región 5) - Tipo 1 - Pago 1", "Brasil", "No aplica", "2340", "2106"),
  ("2XA410\nRome 1276\n2\n2\n", "16.) Otro País - Tipo 2 - Pago 2", "Otro", "No aplica", "3675", "3675"),
  ("I8374KER\nWaterloo 341\n3\n1\n", "17.) Otro País (HAY TRAMPA... MIREN BIEN...) - Tipo 3 - Pago 1", "Otro", "No aplica", "12450", "11205"),
)


# Muestra los valores contenidos en "text" en una línea de color rojo intenso.
def print_red(*text, end="\n"):
    for t in text:
        print(f"\033[91m{t}\033[00m", end=" ")
    print(end=end)


# Ejecuta el programa "script" y captura las salidas que sean dirigidas a la consola estándar.
def run(script):
    proc = subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return proc


def show_and_count(lines, results, data):
    # Índice para recorrer la lista "data" de resultados...
    # ... en esa lista, los resultados comienzan en la posición 2...
    k = 2

    # Contador de resultados correctos...
    ok = 0

    # print()
    for i in range(len(lines)):
        # ... mostrar el contexto del lote, si corresponde (líneas con número de orden divisible por 4)...
        if i % 4 == 0:
            print(f"\033[94mPrueba {data[1]}\033[00m")

        # ... mostrar el resultado tal como se mostró en el programa original...
        print("\t", lines[i], end="")

        # ... e informar correctos e incorrectos...
        if results[i].strip() == data[k]:
            ok += 1
            print(f"\033[92m --> Correcto\033[00m")
        else:
            print(f"\033[91m --> Incorrecto (esperado: {data[k]})\033[00m")

        if i % 4 == 3:
            print()

        k += 1

    # ...retornar el contador de respuestas correctas y salir...
    return ok


def collect_results(lines):
    # ... recolectar los resultados desde la consola estándar...
    results = []
    for i in range(len(lines)):
        # ...los resultados vienen luego de una secuencia ': '...
        r = lines[i].split(': ')
        results.append(r[1].strip())

    # ...retornar los resultados y salir...
    return results


# Procesa cada tupla "data" del lote "BATCH" con el programa "script" y analiza los resultados.
def start(script):
    print_red("\n---------------------------------")
    print_red("Programa:", script.name)
    print_red("---------------------------------")

    ok = 0
    for data in BATCH:
        # Ejecutar el programa entregado por el estudiante...
        process = run(script.path)

        # Si hay datos tomados desde la línea de órdenes en la variable data, va esta línea...
        stdout_value = process.communicate(data[0].encode('utf-8'))[0].decode('utf-8')

        # Si NO hay datos desde la línea de órdenes, va esta otra...
        # ... para capturar lo que sea que se haya enviado a la consola de salida...
        # stdout_value = process.communicate()[0].decode('utf-8')

        # ... dividir en líneas esa salida...
        lines = stdout_value.splitlines()

        # ... eliminar los mensajes de input de la primera línea...
        r = lines[0].split(": ")[-2:]
        lines[0] = r[0] + ": " + r[1]

        # ...recolectar los resultados desde la consola estándar...
        results = collect_results(lines)

        # Mostrar las salidas del programa tal cual fueron generadas por los estudiantes...
        # ...pero indicando y contando los resultados correctos o no...
        ok += show_and_count(lines, results, data)

    ct = 4 * len(BATCH)
    prc = ok * 100 // ct
    print()
    print(f"\033[95mCantidad de resultados correctos: {ok}\033[00m")
    print(f"\033[95mPorcentaje de resultados correctos: {prc}%\033[00m")


# Inicia el test para todos los programas contenidos en el directorio "SOURCES".
def init():
    with os.scandir(SOURCES) as programs:
        for script in programs:
            if script.name.endswith(".py"):
                try:
                    start(script)
                except Exception as ex:
                    print()
                    print(f"\033[1;93;41m--> Error al ejecutar: ({ex})\033[00m")
                print()
                # input("Presione <Enter> para continuar con el siguiente trabajo...")


if __name__ == '__main__':
    init()
