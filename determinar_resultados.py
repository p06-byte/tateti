from modulo_archivos import *

def determinar_resultado_h(matriz):
    '''
    se fija si hay un ganador horizontal

    usa una bandera para cada simbolo, busca en un rango de 3.
    se va fijando cada fila y, si coinciden las 3 posiciones, pregunta:
        es x? entonces la bandera para x es True
        es o? entonces la bandera para o es True

    retorna ambas banderas.
    '''
    banderaX = False
    banderaO = False
    for i in range(3):
        # horizontal
        if matriz[i][0] == matriz[i][1] == matriz[i][2]:
            if matriz[i][0] == "X":
                banderaX = True
            if matriz[i][0] == "O":
                banderaO = True

    return banderaX, banderaO

def determinar_resultado_v(matriz):
    '''
    se fija si hay un ganador vertical

    usa una bandera para cada simbolo, busca en un rango de 3.
    se va fijando cada columna y, si coinciden las 3 posiciones, pregunta:
        es x? entonces la bandera para x es True
        es o? entonces la bandera para o es True
        
    retorna ambas banderas.
    '''
    banderaX = False
    banderaO = False
    for i in range(3):
        # vertical
        if matriz[0][i] == matriz[1][i] == matriz[2][i]:
            if matriz[0][i] == "X":
                banderaX = True
            if matriz[0][i] == "O":
                banderaO = True

    return banderaX, banderaO

def determinar_resultado_d(matriz):
    '''
    se fija si hay un ganador diagonal

    usa una bandera para cada simbolo.
    diagonal principal:
        se va fijando cada posicion (i,j) donde i = j y, si coinciden las 3 posiciones, pregunta:
            es x? entonces la bandera para x es True
            es o? entonces la bandera para o es True
    
    diagonal secundaria:
        hace el mismo proceso que con la diagonal principal, pero con las posiciones que corresponden.
        
    retorna ambas banderas.
    '''
    banderaX = False
    banderaO = False
    # diagonal
    if matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[1][1] == "X":
            banderaX = True
        if matriz[1][1] == "O":
            banderaO = True

    elif matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[1][1] == "X":
            banderaX = True
        if matriz[1][1] == "O":
            banderaO = True

    return banderaX, banderaO

def determinar_resultado_final(matriz):
    '''
    determina el resultado final

    deja el default de resultado (que es lo que retorna) como empate
    hace dos banderas: una para si gano x, y otra para si gano o.
    rescata cada bandera de las funciones anteriores, dandoles nombres distintos para poder diferenciarlas entre si
    va preguntando por cada bandera: si alguna de las banderas de x es True, se la asigna a la bandera gano_x.
    hace lo mismo con las de o.

    al final, dependiendo de si gano_x o gano_o es True, actualiza el resultado para que refleje la realidad. lo retorna.
    '''
    resultado = "Empate"
    gano_x = False
    gano_o = False

    h_banderaX, h_banderaO = determinar_resultado_h(matriz)
    v_banderaX, v_banderaO = determinar_resultado_v(matriz)
    d_banderaX, d_banderaO = determinar_resultado_d(matriz)

    if h_banderaX == True:
        gano_x = h_banderaX
    if v_banderaX == True:
        gano_x = v_banderaX
    if d_banderaX == True:
        gano_x = d_banderaX
    
    if h_banderaO == True:
        gano_o = h_banderaO
    if v_banderaO == True:
        gano_o = v_banderaO
    if d_banderaO == True:
        gano_o = d_banderaO

    if gano_x == True:
        resultado = "Ganó X"
    elif gano_o == True:
        resultado = "Ganó O"

    return resultado

def actualizar_contadores(partida, resultados):
    '''
    va actualizando los contadores segun corresponda

    si gano o, aumenta el contador de las o.
    si gano x, aumenta el contador de las x.
    si fue un empate, aumenta el contador del empate.

    tambien va aumentando la cantidad de partidas procesadas indiscriminadamente.
    '''
    resultado = determinar_resultado_final(partida)

    if resultado == "Ganó O":
        resultados["Gano O"] += 1

    elif resultado == "Ganó X":
        resultados["Gano X"] += 1

    else:
        resultados["Empate"] += 1

    resultados["Partidas procesadas"] += 1