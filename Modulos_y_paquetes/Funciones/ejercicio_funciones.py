'''
Escribe una función que calcule el área de un círculo. La función debe recibir
el radio como parámetro y devolver el área.
'''
def calcular_area_circulo(radio):
    #recibe un numero entre o flotante
    #calcula el area de un circulo
    #retorna el area
    return 3.14 * (radio**2)

'''
Crea una función que verifique si un número dado es par o impar. La función
debe imprimir un mensaje indicando si el número es par o impar.
'''
def verificar_paridad(numero:int):
    #recibe un numero
    #verifica e imprime si en numero es par o impar
    if(numero % 2 == 0):
        print("El numero es par.")
    else:
        print("El numero es impar.")


respuesta = 1

while(respuesta != 0):
    respuesta = int(input("elija una opcion:\nopcion_1\nopcion_2\nopcion_3\nopcion_4\n ingrese 0 para salir. "))
    match(respuesta):
        case 1:
            radio = int(input("ingrese el radio de un circulo"))
            print(f"El area del circulo es: {calcular_area_circulo(radio)}")
        case 2:
            numero = int(input("ingrese un numero"))
            verificar_paridad(numero)
        case 3:
            pass
        case 4:
            pass
        case _:
            pass


            
        




