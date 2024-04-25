'''
Ejercicio Integrador 01
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
contagio, de cada una debe obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
1000 unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
'''
precio_barbijo_mas_caro = 0
cantidad_unidades = 0
barbijo_mas_caro_cantidad = 0
barbijo_mas_caro_fabricante = None
mas_cantidad_fabricante = None
mas_unidades_fabricante = None
acumulador_jabones = 0
bandera_primer_barbijo = True


for i in range(2):
    #linea 31 a 46 solicito datos
    tipo_ingresado = input("Tipo de producto: ")
    while(tipo_ingresado.lower() != "barbijo" and tipo_ingresado.lower() != "jabón" and tipo_ingresado.lower() != "alcohol"):
        tipo_ingresado = input("Reingrese un tipo de producto válido: ")
        
    
    precio_ingresado = float(input("Precio: "))
    while(precio_ingresado < 100 or precio_ingresado > 300):
        precio_ingresado = float(input("Reingrese un precio entre 100 y 300: "))
    
    cantidad_ingresada = int(input("Cantidad de unidades: "))
    while(cantidad_ingresada <= 0 or cantidad_ingresada > 1000):
        cantidad_ingresada = int(input("La cantidad de unidades debe estar entre 1 y 1000: "))
    
    marca_ingresada = input("Ingrese Marca: ")
    fabricante_ingresado = input("Ingrese el Fabricante: ")
    

    #a continuacion evaluo lo solicitado en consigna  
    if(i == 0 or cantidad_ingresada > cantidad_unidades):
        cantidad_unidades = cantidad_ingresada
        mas_cantidad_fabricante = fabricante_ingresado

    if(tipo_ingresado.lower() == "jabón"):
        acumulador_jabones += cantidad_ingresada
    elif(tipo_ingresado.lower() == "barbijo"):
        if(bandera_primer_barbijo):
            precio_barbijo_mas_caro = precio_ingresado
            barbijo_mas_caro_cantidad = cantidad_ingresada
            barbijo_mas_caro_fabricante = fabricante_ingresado
            bandera_primer_barbijo = False     
        elif(precio_ingresado > precio_barbijo_mas_caro):
            precio_barbijo_mas_caro = precio_ingresado
            barbijo_mas_caro_cantidad = cantidad_ingresada
            barbijo_mas_caro_fabricante = fabricante_ingresado



print(f'''
    El más caro de los barbijos tiene una cantidad de: {barbijo_mas_caro_cantidad} unidades y es fabricado por {barbijo_mas_caro_fabricante}\n
    El fabricante del item con más unidades es: {mas_cantidad_fabricante}\n
    La cantidad total de jabones es: {acumulador_jabones}\n
    Gracias por utilizar el programa''')