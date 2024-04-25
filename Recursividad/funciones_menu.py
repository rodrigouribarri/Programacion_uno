from recursividad import *

def pedir_opcion():
    opcion = input("Seleccione la opción deseada: ")
    while not opcion.isdigit():
        opcion = input("La opción debe ser un número entre 1 y 4. Ingrese nuevamente: ")
    return opcion

def pedir_numero(mensaje:str):
    numero = input(f"Ingrese {mensaje}: ")
    while not numero.isdigit():
        numero = input("Debe ingresar números")
    return int(numero)

def mostrar_menu():
    menu = '''
    1 - Sumar numeros naturales hasta el ingresado
    2 - Calcular Potencia
    3 - Sumar los dígitos del número
    4 - Calcular Fibonacci'''
    print(menu)
    

def iniciar_app():
    mostrar_menu()
    while True:
        match pedir_opcion():
            case "0":
                print("Gracias por utilizar la app")
                break
            case "1":
                numero = pedir_numero("un número: ")
                resultado = sumar_naturales(numero)
                print(f"La suma de números naturales hasta el ingresado es: {resultado}")
            case "2":
                base = pedir_numero("la base: ")
                exponente = pedir_numero("el exponente: ")
                resultado = calcular_potencia(base, exponente)
                print(f"El resultado de elevar {base} a {exponente} es: {resultado}")
            case "3":
                numero = pedir_numero("un número: ")
                resultado = sumar_digitos(numero)
                print(f"La suma de los dígitos del número({numero}) ingresado es: {resultado}")
            case "4":
                numero = pedir_numero("un número: ")
                resultado = calcular_fibonacci(numero)
                print(f"El número de Fibonacci del número ingresado es: {resultado}")
            case _:
                print("Opción incorrecta, ingrese otra")

                