import Modulos_y_paquetes.Funciones as f

f.mostrar_menu()
flag = True
while(flag):
    opcion = f.pedir_opcion()
    match(opcion):
        case 1:
            radio = int(input("Ingrese el radio del círculo: "))
            print(f"El área del círculo es {f.calcular_area_circulo(radio)}")
        case 2:
            numero = int(input("Ingrese un número: "))
            f.verificar_par_o_impar(numero)
        case 3:
            n1 = int(input("Ingrese el primer número: "))
            n2 = int(input("Ingrese el segundo número: "))
            n3 = int(input("Ingrese el tercer número: "))
            print(f.buscar_maximo(n1, n2, n3))
        case 4:
            base = int(input("Ingrese el número base: "))
            potencia = int(input("Ingrese el número exponente: "))
            print(f.calcular_potencia_de_numero(base, potencia))
        case 0:
            flag = False
exit()