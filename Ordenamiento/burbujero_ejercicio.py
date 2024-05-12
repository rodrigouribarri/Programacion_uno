lista_nombres = ["pepepepepeppepepe", "Amalia" , "Juan", "María", "Luis", "Ana", "Asabella", "Carlos", "Fernanda", "Santiago", "Teresa", "Oscar", "Benjamín", "Karla", "Héctor",
           "Verónica", "Gabriel", "Natalia", "Isabel", "Wilson", "Rosa", "Daniela", "Esteban", "Yolanda", "Zoila", "Ximena", "Patricia", "Ursula",
           "Quirino"]
'''
Listas simples:
'''
# 1- Realizar una función que ordene una lista de entero en orden ascendente o descendente dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de cambios que se realizaron.
def ordenar_lista(lista:list, ascendente:bool = True):
    contador = 0
    for i in range(len(lista)):
        for j in range(i +1, len(lista)):
            if ascendente:
                if lista[i] > lista[j]:
                    contador += 1
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux 
            else:
                if lista[i] < lista[j]:
                    contador += 1
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux 
    return contador

# 2- Realizar una función que ordene una lista de nombres de la A-Z o viceversa dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de cambios que se realizaron.
def ordenar_nombres(lista_nombres:list, A_Z:bool = True):
    contador = 0
    for i in range(len(lista_nombres)):
        for j in range(i + 1, len(lista_nombres)):
            if A_Z:
                if lista_nombres[i] > lista_nombres[j]:
                    contador += 1
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
            else:
                if lista_nombres[i] < lista_nombres[j]:
                    contador += 1
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux

    return contador

#3- Similar a la función anterior, se debe realizar otra que ordene una lista de nombres por su largo, de manera ascendente o descendente, la función debe retornar la cantidad de cambios que se realizaron
def ordenar_nombres_por_largo(lista_nombres:list, ascendente: bool = True):
    contador = 0
    for i in range(len(lista_nombres)):
        for j in range(i + 1, len(lista_nombres)):
            if ascendente:
                if len(lista_nombres[i]) > len(lista_nombres[j]):
                    contador += 1
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
            else:
                if len(lista_nombres[i]) < len(lista_nombres[j]):
                    contador += 1
                    aux = lista_nombres[i]
                    lista_nombres[i] = lista_nombres[j]
                    lista_nombres[j] = aux
    return contador


'''Matrices:
4- Ordenar una matriz de nombre-apellido de la A-Z o viceversa dependiendo de un parámetro que se le envíe, por otro lado, la función deberá recibir otro parámetro para indicar si la prioridad de ordenamiento la tendrá el nombre o el apellido.'''
matriz_personas = [
    ["Juan", "Perez"],
    ["Juan", "Gonzalez"],
    ["Maria", "Gonzalez"],
    ["Luis", "Sanchez"],
    ["Ana", "Martinez"],
    ["Pedro", "Gomez"],
    ["Laura", "Diaz"],
    ["Carlos", "Rodriguez"],
    ["Marta", "Lopez"],
    ["Diego", "Hernandez"],
    ["Elena", "Moreno"]
]
def ordenar_lista_personas(lista:list, prioridad:bool = 0, ascendente:bool = True):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if ascendente:
                if lista[i][prioridad] > lista[j][prioridad]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                elif lista[i][prioridad] == lista[j][prioridad] and lista[i][not prioridad] > lista[j][not prioridad]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if lista[i][prioridad] < lista[j][prioridad]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
                elif lista[i][prioridad] == lista[j][prioridad] and lista[i][not prioridad] < lista[j][not prioridad]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

print(matriz_personas)
ordenar_nombres(lista_nombres)
print(matriz_personas)

#print(lista_nombres)

#print(ordenar_lista_nombres_ascendente_descendente_por_largo(lista_nombres,True))

#print(lista_nombres)