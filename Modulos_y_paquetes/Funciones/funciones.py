#Ejercicio 1
def calcular_area_circulo(radio):
    # Recibe el radio de un circulo
    # calcula el área del mismo
    # Retorna el valor del area
    PI = 3.14
    area = PI * (radio ** 2)
    return area

#Ejercicio 2
def verificar_par_o_impar(numero):
    # Recibe un número
    # evalúa si es par o impar
    # Imprime por consola si el número es par o impar
    resultado = "impar"

    if(numero %2 == 0):
        resultado = "par"
    
    print(f"El número ingresado es {resultado}")

#Ejercicio 3
def buscar_maximo(num1, num2, num3):
    #Recibe 3 números
    # Busca el mayor entre ellos
    # Retorna el mayor número
    if(num1 > num2 and num1 > num3):
        numero_maximo = num1
    elif(num2 > num3):
        numero_maximo = num2
    else:
        numero_maximo = num3

    return f"El número más grande es: {numero_maximo}"

#Ejercicio 4
def calcular_potencia_de_numero(base, potencia):
    # Recibe un npumero base y otro exponente
    # realiza la potenciacion y 
    #retorna el resultado

    resultado = base ** potencia
    return f"{base} elevado a {potencia} da como resultado {resultado}"


def pedir_opcion():
    #Pide una opcion, si no es correcta la solicita nuevamente
    opcion_ingresada = int(input("Por favor ingrese el número de la opción: "))
    while(opcion_ingresada < 0 or opcion_ingresada > 4):
        opcion_ingresada = int(input("Por favor ingrese una opción correcta: "))
    return opcion_ingresada

def mostrar_menu():
    print('''
    Por favor elija una de las siguientes opciones:
          1 - Calcular área de un círculo.
          2 - Verificar si un número es par o impar
          3 - Encontrar número máximo
          4 - Calcular potencia de un número
          0 - Salir
    ''')



        
    