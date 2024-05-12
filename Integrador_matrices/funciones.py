import datetime

def mostrar_menu():
    menu = '''
1 - Registrar mascota
2 - Dar consulta médica
3 - Mostrar todas las mascotas
4 - Mostrar solo mascotas que superen promedio de edad
5 - Calcular el promedio de mascotas
6 - Contar cantidad de perros
7 - Identificar tipo de mascota mas registrado
8 - Salir del sistema
'''
    print(menu)


def pedir_string(mensaje:str):
    cadena = input(mensaje)
    while not cadena.isalpha():
        cadena = input("Dato incorrecto, debe ingresar letras: ")
    return cadena

def pedir_numero(mensaje:str):
    numero = input(mensaje)
    while not (numero.isdigit()) or int(numero) < 0:
        numero = input("Debe ingresar un número mayor a cero: ")
    return numero

def validar_dni(numero:int):
    while len(numero) != 8 and len(numero) != 9:
        numero = input("DNI incorrecto, ingrese uno válido: ")
    return numero

def validar_sexo(sexo:str):
    sexo = sexo.capitalize()
    while sexo != "Hembra" or sexo != "Macho":
        sexo = input("El sexo debe ser macho o hembra, reingrese: ")

    return sexo


def ingresar_mascota():
    mascota = []

    dni = validar_dni(int(pedir_numero("Ingrese DNI: ")))
    nombre = pedir_string("Nombre mascota: ")
    edad = int(pedir_numero("Edad mascota: "))
    especie = pedir_string("Especie mascota: ")
    sexo = pedir_string("Sexo mascota: ")
    peso = float(pedir_numero("Peso mascota: "))
    fecha_ultima_visita = datetime.date.today().strftime("%d,%m,%Y")
    historia_clinica = pedir_string("Historial médico: ")

    mascota.append(dni)
    mascota.append(nombre)
    mascota.append(edad)
    mascota.append(especie)
    mascota.append(sexo)
    mascota.append(peso)
    mascota.append(fecha_ultima_visita)
    mascota.append(historia_clinica)

    return mascota

def actualizar_datos(lista_mascotas:list, indice_mascota:int):
    edad_actual = int(pedir_numero("Ingrese edad: "))
    peso_actual = float(pedir_numero("Ingrese peso: "))
    fecha_actual = " | " + datetime.date.today().strftime("%d,%m,%Y")
    historial_nuevo = " | " + pedir_string("Ingrese detalle de la consulta: ")
    lista_mascotas[indice_mascota][2] = edad_actual
    lista_mascotas[indice_mascota][5] = peso_actual
    lista_mascotas[indice_mascota][6] += fecha_actual
    lista_mascotas[indice_mascota][7] += historial_nuevo



#1. Mostrar información completa de todas las mascotas: Esta función permitirávisualizar todos los datos registrados de todas las mascotas atendidas en la veterinaria.
def listar_mascotas(lista_mascotas:list):
    for i in range(len(lista_mascotas)):
        mensaje = ""
        mascota = lista_mascotas[i]
        for j in range(len(mascota)):
            mensaje += f"|| {mascota[j]} "
        mensaje += " ||"
        print(mensaje)


#2. Mostrar información completa solo de las mascotas que superen el promedio de edad: Esta opción mostrará únicamente los datos de las mascotas cuya edad supere el promedio de edad de todas las mascotas registradas.
def calcular_promedio(lista_mascotas:list, indice:int):
    acumulador = 0
    for i in range(len(lista_mascotas)):
        acumulador += lista_mascotas[i][indice]
    promedio = acumulador / len(lista_mascotas)
    return promedio

def listar_mascotas_superan_promedio_edad(lista_mascotas: list, indice:int):
    promedio_edad = calcular_promedio(lista_mascotas, indice)
    lista_mayores_promedio = []
    for i in range(len(lista_mascotas)):
        if lista_mascotas[i][indice] > promedio_edad:
            lista_mayores_promedio.append(lista_mascotas[i])
    print(listar_mascotas(lista_mayores_promedio))

#3. Calcular el promedio de peso de todas las mascotas: Esta función calculará y mostrará el promedio de peso de todas las mascotas registradas en la veterinaria.
def mostrar_promedio_peso(lista_mascotas:list, indice:int):
    promedio_peso = calcular_promedio(lista_mascotas, indice)
    print(f"El peso promedio de todas las mascotas es {format(promedio_peso,'.2f')} kg")

#4. Contar la cantidad de perros registrados: Permitirá obtener el número total de perros registrados en el sistema.
def mostrar_cantidad(lista_mascotas: list, indice:int, tipo:str):
    contador = 0
    for i in range(len(lista_mascotas)):
        if lista_mascotas[i][indice].lower() == tipo.lower():
            contador += 1
    print(f"De la especie {tipo} hay {contador}")


#5. Identificar el tipo de mascota más registrado: Esta función determinará cuál es el tipo de mascota (perro, gato, ave, etc.) que más se ha registrado en la veterinaria
def mostrar_especie_mas_registrada(lista_mascotas: list, indice:int):
    lista_tipos = []
    lista_mas_registrados = []        
    for i in range(len(lista_mascotas)):
        #lista_tipos = lista_mascotas[i][indice]
        if lista_mascotas[i][indice] not in lista_tipos:
            lista_tipos.append(lista_mascotas[i][indice])

    lista_contadores = [0] * len(lista_tipos)

    for i in range(len(lista_mascotas)):
        posicion = lista_tipos.index(lista_mascotas[i][indice])
        lista_contadores[posicion] += 1

    for i in range(len(lista_contadores)):
        if i == 0 or lista_contadores[i] >= mayor:
            mayor = lista_contadores[i]
            lista_mas_registrados.append(lista_tipos[i])
        

    if len(lista_mas_registrados) > 1:
        mensaje = "Las especies más registradas son: \n"
        for i in range(len(lista_mas_registrados)):
            mensaje += lista_mas_registrados[i] + "\n" 
    else:
        mensaje = f"La especie mas registrada es: {lista_mas_registrados[0]}"

    print(mensaje)
    