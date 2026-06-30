from colorama import Fore, Style

def ingresar_entero(mensaje, minimo, maximo):
    numero = int(input(mensaje))
    #condicion base
    if minimo <= numero <= maximo:
        return numero
    #recursion
    else:
        print(Fore.RED + f"Por favor, ingrese un número entre {minimo} y {maximo}." + Style.RESET_ALL)
        return ingresar_entero(mensaje, minimo, maximo)
        
        
def ingresar_flotante(mensaje, minimo, maximo):
    numero = float(input(mensaje))
    #condicion base
    if minimo <= numero <= maximo:
        return numero
    #recursion
    else:
        print(Fore.RED + f"Por favor, ingrese un número entre {minimo} y {maximo}." + Style.RESET_ALL)
        return ingresar_flotante(mensaje, minimo, maximo)
    
def ingresar_texto(mensaje):
    texto = input(mensaje)
    while texto == "":
        print(Fore.RED + "Por favor, ingrese un dato no vacío." + Style.RESET_ALL)
        texto = input(mensaje)
    return texto

def pedir_si_no(mensaje: str):
    respuesta = input(mensaje)
    while respuesta not in ("si", "no"):
        respuesta = input(Fore.RED + "Ingresó mal el si o no. Inténtelo de nuevo, todo en minúsculas." + Style.RESET_ALL)
    return respuesta

def mostrar_menu(opciones_menu):
    for i in range(len(opciones_menu)):
        print(f"{i + 1}. {opciones_menu[i]}")
    opcion = ingresar_entero("Ingrese una opcion: ", 1, len(opciones_menu))
    
    return opcion

def criterio_generico(elemento_1, elemento_2): # SOLO FUNCIONA PARA DOS PERSONAS!!!
    retorno = None # si son iguales (default)

    if elemento_1 > elemento_2: # caso mayor que
        retorno = True
    elif elemento_1 < elemento_2: # caso menor que
        retorno = False

    return retorno

def criterio_edad(diccionario_1, diccionario_2):
    return criterio_generico(diccionario_1["edad"], diccionario_2["edad"])

def ordenar_gen(lista: list, criterio, bool: bool): # no quiero estar cambiando True o False segun quiera ordenar, asi que paso como parametro el bool
    for i in range(0, len(lista) - 1, 1):
        for j in range(i + 1, len(lista), 1):
            if criterio(lista[i], lista[j]) == bool: # si pongo True ordena de menor a mayor y si pongo False ordena de mayor a menor
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar

# def guardar_data(data):
#     with open("data.json", "w") as archivo:
#         json.dump(data, archivo, indent=4)

# def cargar_data():
#     with open("data.json", "r") as archivo:
#         return json.load(archivo)


# def determinar_simbolos(matriz):
#     simbolos = set()

#     for fila in matriz:
#         for elemento in fila:
#             simbolos.add(elemento)

#     return simbolos

# simbolos = determinar_simbolos(partida)

# if simbolos == {"X", "O"}:
#     print("Símbolos válidos.")
# else:
#     print("La partida tiene caracteres inválidos.")


# def calcular_estadisticas(resultados):
#     partidas_validas = (resultados["Partidas procesadas"] - resultados["Partida invalida"])

#     estadisticas = {}

#     estadisticas["Partidas procesadas"] = resultados["Partidas procesadas"]
#     estadisticas["Partidas válidas"] = partidas_validas
#     estadisticas["Gano X"] = resultados["Gano X"]
#     estadisticas["Gano O"] = resultados["Gano O"]
#     estadisticas["Empates"] = resultados["Empate"]
#     estadisticas["Inválidas"] = resultados["Partida invalida"]
#     estadisticas["Porcentaje X"] = resultados["Gano X"] * 100 / partidas_validas
#     estadisticas["Porcentaje O"] = resultados["Gano O"] * 100 / partidas_validas
#     estadisticas["Porcentaje Empates"] = resultados["Empate"] * 100 / resultados["Partidas procesadas"]

#     return estadisticas

# mostrar_contadores(resultados)

# estadisticas = calcular_estadisticas(resultados)

# guardar_estadisticas(estadisticas)


# numero = int(input("Ingrese el número de partida: "))

# archivo = open("partidas.txt")

# contador = 1
# partida = leer_archivo(archivo)

# while partida != False:
#     if contador == numero:
#         mostrar_matriz(partida)
#         print(determinar_resultado_final(partida))
#         actualizar_contadores(partida, resultados)
#     contador += 1
#     partida = leer_archivo(archivo)


# while partida != False:
#     if determinar_resultado_final(partida) == "Gano O":
#         mostrar_matriz(partida)
#         break


# if determinar_resultado_final(partida) == "Partida inválida":
#     mostrar_matriz(partida)


            # if elemento == "X":
            #     contador_X += 1
            # if elemento == "O":
            #     contador_O += 1