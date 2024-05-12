lista_ejemplo = [-1,30,30,4]
lista_nombres = ["rodrigo", "Yamila", "Rodrigo"]

#1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
def calcular_promedio(lista:list):
    acumulador = 0
    for i in lista:
        acumulador += i
    promedio = acumulador / len(lista)

    return promedio

#2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
#promedio de los números positivos.
def calcular_promedio_positivos(lista:list):
    acumulador_positivos = 0
    contador_positivos = 0
    for i in lista:
        if i > 0:
            acumulador_positivos += i
            contador_positivos += 1
    promedio_positivos = acumulador_positivos / contador_positivos
    
    return promedio_positivos

def calcular_promedio_positivos_reutilizando(lista_numeros:list):
    lista_positivos = []
    for i in range(len(lista_numeros)):
        if lista_numeros[i] > 0:
            lista_positivos.append(lista_numeros[i])

    return calcular_promedio(lista_positivos)
#3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
def calcular_producto(lista:list):
    resultado = 1
    for i in lista:
        resultado *= i
    return resultado

#4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
#del valor máximo encontrado.
def retornar_posicion_maximo_valor(lista:list):
    for i in range(len(lista)):
        if i == 0 or lista[i] > maximo_valor:
            maximo_valor = lista[i]
            posicion_maximo_valor = i
    return posicion_maximo_valor

#5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
#posiciones en donde se encuentra el valor máximo hallado.
def hallar_posiciones_maximo_valor(lista_numeros:list):
    lista_posiciones = []
    for i in range(len(lista_numeros)):
        if i == 0 or mayor < lista_numeros[i]:
            mayor = lista_numeros[i]
            lista_posiciones.clear()
            lista_posiciones.append(i)
        elif lista_numeros[i] == mayor:
            lista_posiciones.append(i)

    return lista_posiciones

#6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
# de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
# reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
# reemplazo y luego retornar la cantidad total de reemplazos realizados.
def pedir_nombre(mensaje:str):
    nombre = input(mensaje)
    return nombre

def reemplazar_nombres(lista_nombres:list):
    contador_reemplazos = 0
    nombre_a_reemplazar = pedir_nombre("Ingrese el nombre a reemplazar: ")
    nombre_reemplazo = pedir_nombre("Ingrese el nombre de reemplazo: ")
    for i in range(len(lista_nombres)):
        if lista_nombres[i].lower() == nombre_a_reemplazar.lower():
            lista_nombres[i] = nombre_reemplazo
            contador_reemplazos += 1
    
    return contador_reemplazos


