import json

def leer_archivo(archivo):
    '''
    lee una linea del archivo (una partida)

    si llega al final del archivo, retorna otra cosa (para permitirle parar)

    crea la matriz donde se van a ir guardando las partidas y establece un indice para poder navegar el archivo

    para obtener la matriz:
        va a repetir el proceso 3 veces para tener las 3 filas.
        crea la fila (todavia vacia)
        primera vuelta:
            agarra 3 caracteres: indice hace 0 -> 1 -> 2
            termina el segundo for, agrega la fila a la matriz, vuelve al primero
        segunda vuelta:
            agarra 3 caracteres: indice hace 3 -> 4 -> 5
            termina el segundo for, agrega la fila a la matriz, vuelve al primero
        tercera (ultima) vuelta:
            agarra 3 caracteres: indice hace 6 -> 7 -> 8
            termina el segundo for, agrega la fila a la matriz, vuelve al primero
        el primer for ya dio 3 vueltas, asi que se termina tambien.

    retorna la matriz.
    '''
    linea = archivo.readline()

    if linea == "":
        return False

    matriz = []
    indice = 0

    for partida in range(3):
        fila = []
        for elemento in range(3):
            fila.append(linea[indice])
            indice += 1
        matriz.append(fila)

    return matriz

def mostrar_matriz(matriz):
    '''
    muestra una matriz

    i es una fila (ej: ['X', 'X', 'O'])
    j es cada elemento de esa fila
    imprime cada elemento (borrando el enter para que esten al lado unos de otros)
    el ultimo print sirve para que la siguiente fila este abajo de la anterior.
    '''
    for i in matriz:
        for j in i:
            print(j, end = "")
        print()

def cargar_resultados():
    '''
    carga los resultados

    los resultados de las partidas se van guardando en un archivo json. esta funcion sirve para abrirlo y leerlo.
    '''
    with open("resultados.json", "r") as archivo:
        return json.load(archivo)

def mostrar_contadores(resultados):
    '''
    muestra los contadores

    en el archivo json, el diccionario esta compuesto por claves y los valores de esas claves.
    rescata ambos y los imprime ordenadamente, para saber que significa cada contador.
    '''
    for clave, valor in resultados.items():
        print(f"{clave}: {valor}")