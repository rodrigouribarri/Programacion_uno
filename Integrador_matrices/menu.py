import datetime
from funciones import *

registro_mascotas = [
    ["12345678", "Luna", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"],
    ["23456789", "Max", 7, "Gato", "Macho", 5.2, "28/04/2024", "Control de pulgas"],
    ["34567890", "Kiwi", 1, "Dragón", "Hembra", 88000, "02/05/2024", "Recorte de alas"],
    ["45678901", "Rocky", 5, "Perro", "Macho", 12.1, "30/04/2024", "Revisión dental"],
    ["56789012", "Coco", 2, "Gato", "Hembra", 4.8, "03/05/2024", "Desparasitación"]
]

while(True):
    mostrar_menu()
    opcion = int(input("Elija una opción: "))
    match opcion:
        case 1:
            print("Registrar mascota.")
            registro_mascotas.append(ingresar_mascota())
        case 2:
            print("Dar consulta medica.")
            indice_mascota = pedir_numero("Ingrese el índice de la mascota: ")
            actualizar_datos(registro_mascotas, indice_mascota)
        case 3:
            print("Mostrar todas las mascotas.")
            listar_mascotas(registro_mascotas)
        case 4:
            print("Mostrar solo mascotas que superen promedio de edad.")
            listar_mascotas_superan_promedio_edad(registro_mascotas, 2)
        case 5:
            print("Calcular el promedio de mascotas")
            mostrar_promedio_peso(registro_mascotas, 5)
        case 6:
            print("Contar cantidad de perros.")
            mostrar_cantidad(registro_mascotas, 3, "perro")
        case 7:
            print("Identificar tipo de mascota mas registrado.")
            mostrar_especie_mas_registrada(registro_mascotas, 3)
        case 8:
            print("Saliendo del sistema.")
            break
    

