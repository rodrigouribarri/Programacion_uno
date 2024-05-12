lista_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def pedir_opcion():
    opcion = input("Ingrese la opción deseada: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Por favor ingrese una opción correcta: ")
    
    return int(opcion)

def pedir_dia():
    dia_ingresado = input("Por favor ingrese el día: ")
    while not dia_ingresado.capitalize() in lista_dias:
        dia_ingresado = input("Por favor ingrese un día correcto")
    return dia_ingresado.lower()

def pedir_monto():
    monto_dia = input("Por favor ingrese el monto total del día: ")
    while not monto_dia.isdigit():
        monto_dia = input("Por favor ingrese el monto en números: ")

    return float(monto_dia)

def mostrar_menu():
    menu = '''
1 - Ingresar datos de compras. 
2 - Calcular estadísticas.
3 - Cerrar aplicación.'''
    print(menu)

def retornar_nombre_dia(posicion_dia:int):
    match posicion_dia:
        case 0: 
            dia = "lunes"
        case 1:
            dia = "martes"
        case 2:
            dia = "miércoles"
        case 3:
            dia = "jueves"
        case 4:
            dia = "viernes"
        case 5: 
            dia = "sábado"
        case 6:
            dia = "domingo"
    
    return dia

def determinar_día_de_mayor_o_menor_ingreso(lista_ingresos: list, mayor = True):
    for i in range(len(lista_ingresos)):
        if mayor:
            if i == 0 or lista_ingresos[i] > mayor_ingreso:
                mayor_ingreso = lista_ingresos[i]
                posicion_dia = i
        else:
            if i == 0 or lista_ingresos[i] < menor_ingreso:
                menor_ingreso = lista_ingresos[i]
                posicion_dia = i

    return retornar_nombre_dia(posicion_dia)

def calcular_ingresos(lista_ingresos:list, total= True, semana = False, fin_s= False):
    #Calcula los ingresos de toda la semana, de lunes a viernes o del fin de semana
    acumulador_ingresos = 0
    if total and not semana and not fin_s:
        for i in lista_ingresos:
            acumulador_ingresos += i
    elif semana and not total and not fin_s:
        for i in lista_ingresos[0:5]:
                acumulador_ingresos += i
    elif fin_s and not total and not semana:
        for i in lista_ingresos[-2:]:
                acumulador_ingresos += i

    return acumulador_ingresos


def calcular_promedio_ingresos(lista_ingresos:list, total= True, semana = False, fin_s= False):
    if total and not semana and not fin_s:
        promedio_ingresos = calcular_ingresos(lista_ingresos) / 7
    elif semana and not total and not fin_s:
        promedio_ingresos = calcular_ingresos(lista_ingresos, False, True, False) / 5
    elif fin_s and not total and not semana:
        promedio_ingresos = calcular_ingresos(lista_ingresos, False, False, True) / 2

    return promedio_ingresos

#Calcular el día con la mayor variación en los ingresos respecto al día anterior.
def calcular_variacion_diaria(lista_ingresos:list):
    variacion = 0
    for i in range(1,len(lista_ingresos)):
        variacion_actual = lista_ingresos[i] - lista_ingresos[i - 1]
        if variacion_actual < 0:
            variacion_actual = -variacion_actual
        if i == 1  or variacion_actual > variacion:
            variacion = variacion_actual
            posicion_dia = i
            
    return posicion_dia

lista_prueba = [100,80,50,5,125,10,10]



