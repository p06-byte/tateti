from modulo_archivos import *
from determinar_resultados import *

############################################################

def main():
    resultados = cargar_resultados() # abre el archivo donde se van a guardar los resultados

    archivo = open("partidas.txt", "r") # abre el archivo de las partidas

    partida = leer_archivo(archivo) # lee una linea (partida) y la convierte en una matriz
    while partida != False: # si partida == False, entonces es el final del archivo (ver leer_archivo)
        mostrar_matriz(partida) # muestra la partida
        resultado = determinar_resultado_final(partida) # dice explicitamente quien gano
        print(resultado)

        actualizar_contadores(partida, resultados) # actualiza los contadores

        print() # esto es para que deje un espacio en medio nada mas
        partida = leer_archivo(archivo) # para que pase a la siguiente linea

    archivo.close() # cierra partidas.txt

    mostrar_contadores(resultados) # muestra los contadores

if __name__ == "__main__":
    main()