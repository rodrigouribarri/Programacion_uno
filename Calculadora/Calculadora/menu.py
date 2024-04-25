import os
from funciones import *

def menu():
    operando_1 = None
    operando_2 = None
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
      
        if opcion == 1:
            operando_1 = ingresar_numero("Primer")
        elif opcion == 2:
            operando_2 = ingresar_numero("Segundo")
        elif opcion == 3:
            print("Calculo todas las operaciones")
            if(operando_1 != None and operando_2 != None):
                suma = sumar(operando_1,operando_2)
                resta = restar(operando_1, operando_2)
                multiplicacion = multiplicar(operando_1, operando_2)
                division = dividir(operando_1, operando_2)
                resto = calcular_resto(operando_1, operando_2)
                potenciacion = calcular_potencia(operando_1, operando_2)
                if(operando_1 > 0 and operando_2 > 0):
                    factorial_operando_1 = calcular_factorial(operando_1)
                    factorial_operando_2 = calcular_factorial(operando_2)
                else:
                    print("No es posible calcular el factorial")
            else:
                print("Es necesario que ingrese los operandos")
        elif opcion == 4:
            print("Informo todos los resultados")
            print(f"El resultado de {operando_1} + {operando_2} es: {suma}")
            print(f"El resultado de {operando_1} - {operando_2} es: {resta}")
            print(f"El resultado de {operando_1} / {operando_2} es: {division}")
            print(f"El resultado de {operando_1} * {operando_2} es: {multiplicacion}")
            print(f"{operando_1} elevado a {operando_2} es: {potenciacion}")
            print(f"El resultado de {operando_1} % {operando_2} es: {resto}")
            print(f"Factorial de {operando_1} es: {factorial_operando_1} y de {operando_2} es: {factorial_operando_2}")

        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
            
        #os.system('clear')
    
    
menu()
