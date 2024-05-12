'''
        Uribarri Rodrigo Martin Div A311
listado_alumnos = [["rodrigo",20,36399999,"m",4],
                   ["martina",30,46399999,"f",10], 
                   ["Juan", 22, 20204040, "M", 5], 
                   ["Alma", 22, 30307070, "F", 10], 
                   ["Alex", 21, 10108080, "NB", 6]]
'''
listado_alumnos = []


def pedir_string(mensaje):
    variable = input(mensaje)
    while not variable.isalpha():
        variable = input("Ingreso incorrecto, debe ingresar letras, ingrese nuevamente: ")

    return variable

def pedir_numero(mensaje):
    variable_numerica = input(mensaje)
    while not variable_numerica.isdigit():
        variable_numerica = input("Ingreso incorrecto, solo números, ingrese nuevamente: ")

    return variable_numerica

def validar_genero(genero:str):
    genero = genero.lower()
    while not (genero == "m" or genero == "f" or genero == "nb"):
        genero = input("El género debe ser M, F ó NB: ")
        genero = genero.lower()
    return genero

def validar_nota(nota):
    while float(nota) < 1 or float(nota) > 10:
        nota = input("La nota debe estar entre 1 y 10, reingresela: ")

    return nota

def validar_dni(dni):
    while len(dni) != 8 and len(dni) != 9:
        dni = input("DNI incorrecto, ingrese nuevamente: ")
    
    return dni

# 1. Listado de todos los alumnos con un formato similar al siguiente:
def imprimir_lista_alumnos(lista_alumnos:list):
    for i in range(len(lista_alumnos)):
        mensaje = ""
        alumno = lista_alumnos[i]
        for j in range(len(alumno)):
            mensaje += f"|| {alumno[j]} "
        mensaje += " ||"
        print(mensaje)

# 2. El promedio de edades de los alumnos.
def calcular_promedio_edad(lista_alumnos:list):
    acumulador = 0
    for i in range(len(lista_alumnos)):
        acumulador += lista_alumnos[i][1]

    promedio_edad = acumulador / len(lista_alumnos)
    return promedio_edad

def calcular_cantidad_por_nota(lista_alumnos:list, nota_min:int, nota_max:int, indice:int):
    contador = 0
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i][indice] >= nota_min and lista_alumnos[i][indice] <= nota_max:
            contador += 1            
    return contador

def listar_por_genero(lista_alumnos:list, genero:str, indice:int):
    lista_genero = []
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i][indice].lower() == genero:
            lista_genero.append(lista_alumnos[i])

    return lista_genero

def calcular_promedio_nota_genero(lista_alumnos_genero:list, indice:int):
    acumulador = 0
    for i in range(len(lista_alumnos_genero)):
        acumulador += int(lista_alumnos_genero[i][indice])
    promedio = acumulador / len(lista_alumnos_genero)
    return promedio

def calcular_porcentaje_promocionados_por_genero(lista_alumnos_genero:list, indice:int):
    contador = 0
    porcentaje = 0
    for i in range(len(lista_alumnos_genero)):
        if lista_alumnos_genero[i][indice] >= 6:
            contador += 1
    
    if contador != 0:
        porcentaje = (contador / len(lista_alumnos_genero)) * 100

    return porcentaje

def alumnos_app():
    print("A continuación deberá ingresar los datos de los alumnos...")
    for i in range(1):
        alumno = []
        nombre = pedir_string("Nombre: ")
        edad = pedir_numero("Edad: ")
        dni = validar_dni(pedir_numero("DNI: "))
        genero = validar_genero(pedir_string("Género: "))
        nota = validar_nota(pedir_numero("Nota: "))

        alumno.append(nombre)
        alumno.append(int(edad))
        alumno.append(int(dni))
        alumno.append(genero)
        alumno.append(float(nota))

        listado_alumnos.append(alumno)
    
    imprimir_lista_alumnos(listado_alumnos)
    print(f"El promedio de edad de los alumnos es de {calcular_promedio_edad(listado_alumnos)} años")
    print(f"La cantidad de alumnos promocionados fue: {calcular_cantidad_por_nota(listado_alumnos, 6, 10, 4)}")
    print(f"La cantidad de alumnos aprobados fue: {calcular_cantidad_por_nota(listado_alumnos, 6, 10, 4)}")
    print(f"La cantidad de alumnos desaprobados fue: {calcular_cantidad_por_nota(listado_alumnos, 6, 10, 4)}")
    print(f"El promedio de nota de masculinos es: {calcular_promedio_nota_genero(listar_por_genero(listado_alumnos,'m',3),4)}")
    print(f"El procentaje de alumnas promocionadas es de: {calcular_porcentaje_promocionados_por_genero(listar_por_genero(listado_alumnos,'f',3),4)} %")


alumnos_app()