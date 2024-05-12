from funciones import *
#La lista_montos va de lunes a domingos
lista_montos = [0] * 7



while True:
    mostrar_menu()
    opcion_ingresada = pedir_opcion()
    match opcion_ingresada:
        case 1:
            contador = 0
            while contador < 7:
                dia = pedir_dia()
                ingreso = pedir_monto()
                contador += 1
                match dia.lower():
                    case "lunes":
                        lista_montos[0] = ingreso
                    case "martes":
                        lista_montos[1] = ingreso
                    case "miércoles":
                        lista_montos[2] = ingreso
                    case "jueves":
                        lista_montos[3] = ingreso
                    case "viernes":
                        lista_montos[4] = ingreso
                    case "sábado":
                        lista_montos[5] = ingreso
                    case "domingo":
                        lista_montos[6] = ingreso
        case 2:
            if lista_montos == [0] * 7:
                print("Debe cargar los datos para poder calcular las estadísticas")
            else:
                print(f"El día con más ingresos fue {determinar_día_de_mayor_o_menor_ingreso(lista_montos)}")
                print(f"El día con menos ingresos fue {determinar_día_de_mayor_o_menor_ingreso(lista_montos,False)}")
                print(f"El promedio de ingresos semanal fue de: {calcular_promedio_ingresos(lista_montos)}")
                print(f"El total de ingresos semanal fue de: {calcular_ingresos(lista_montos)}")
                print(f"El promedio de ingresos de lunes a viernes fue de {calcular_promedio_ingresos(lista_montos, False, True, False)} y del fin de semana fue de {calcular_promedio_ingresos(lista_montos, False, False, True)}")
                print(f"El día con más variación de ingresos fue: {calcular_variacion_diaria(lista_montos)}")
        case 3: 
            print("Cerrando aplicación...")
            break
