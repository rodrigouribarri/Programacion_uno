# 1. Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_naturales(numero:int)->int:
    if numero == 0:
        resultado = 0
    else:
        resultado = numero + sumar_naturales(numero - 1)
    
    return resultado


# Realizar una función recursiva que calcule la potencia de un número:
def calcular_potencia(base: int, exponente: int)->int:
    if base == 0:
        resultado = 0
    elif exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)

    return resultado

# 3. Realizar una función recursiva que la suma de los dígitos de un número:
def sumar_digitos(numero: int)->int:
    if numero < 10:
        resultado = numero
    else:
        resultado = numero % 10 + sumar_digitos(numero // 10)
    
    return resultado

# función deberá seguir el siguiente prototipo:
# Definición:
# La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de
# los dos anteriores:
# 4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La
def calcular_fibonacci(numero: int)->int:
    if numero < 2:
        resultado = numero
    else:
        resultado = calcular_fibonacci(numero - 2) + calcular_fibonacci(numero - 1)
    return resultado


    
#print(sumar_naturales(5))
#print(calcular_potencia(3,3))
#print(calcular_fibonacci(8))

