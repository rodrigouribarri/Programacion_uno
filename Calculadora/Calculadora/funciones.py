def ingresar_numero(operando:str):
    numero = int(input(f"Ingrese {operando} Operando: "))
    return numero

def sumar(A:int,B:int):
    return A + B

def restar(A:int, B:int):
    return A - B

def multiplicar(A:int, B:int):
    return A * B

def dividir(A:int, B:int):
    if B == 0:
        return "No es posible dividir por cero"
    else:
        return A / B

def calcular_potencia(A:int, B:int):
    return A ** B

def calcular_resto(A:int, B:int):
    if B == 0:
        return "No es posible dividir por cero"
    else:
        return A % B

def calcular_factorial(numero):
    for i in range(numero-1,1,-1):
        numero *= i
    return numero

