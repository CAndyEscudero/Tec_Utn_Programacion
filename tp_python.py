'''1. ) La asociación de vinicultores tiene como política fijar un precio inicial 
al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
se requiere determinar cuánto recibirá un productor por la uva que entre ga en un embarque,
considerando lo siguiente: si es de tipo A, se le cargan 20¢ al precio inicial 
cuando es de tamaño 1; y 30¢ si es de tamaño 2. Si es de tipo B, se rebajan 30¢ 
cuando es de tamaño 1, y 50¢ cuando es de tamaño 2. Realice un algoritmo para 
determinar la ganancia obtenida y represéntelo mediante diagrama de flujo y su 
correspondiente script(programa) en python.'''
# < --------------------------------------------------------------------------- >

 
while(True):
    try:
    
        kg_uvas = int(input("ingrese los kilos de uva: "))
        tipo =input("Ingrese el tipo A o B ").upper()
        tamaño = int(input("Ingrese el tamaño 1 o 2 "))
        precio_inicial = int(input("Ingrese el precio "))
        ganancia_por_kilo = None
    
        if (tipo == 'A') and (tamaño == 1):
            ganancia_por_kilo = 0.20
        elif (tipo == 'A') and (tamaño == 2):
            ganancia_por_kilo = 0.30

        if(tipo == 'B') and (tamaño == 1):
            ganancia_por_kiloa = - 0.30
        elif (tipo == 'B') and (tamaño == 2):
            ganancia_por_kilo = - 0.50

        precio_final = (precio_inicial + ganancia_por_kilo)
        ganancia_total = (precio_final * kg_uvas)
        print(f'La ganancia total es: ${ganancia_total}')

    except: 
        print ('Debes ingresar valores correctos')

# <------------------------------------------------------------------------->
'''2.) El director de una escuela está organizando un viaje de estudios, y 
    requie re determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la
    compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 
    alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos, el costo es 
    de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta del autobús
    es de $4000.00, sin importar el número de alumnos. Entregar Diagrama de flujo y
    script en python.'''

# <------------------------------------------------------------------------->

try:
    cantidad_alumno = int(input('Ingrese la cantidad de Alumnos: '))
    costo_fijo = 4000
    
    if cantidad_alumno >= 100:
        costo_alumno = 65
    elif 50 <= cantidad_alumno <= 99:
        costo_alumno = 70
    elif 30 <= cantidad_alumno <= 40:
        costo_alumno = 95
    costo_total = (cantidad_alumno * costo_alumno)
    print (f'El costo total es de : ${costo_total}')
    if cantidad_alumno <30:
        costo_fijo
        print(f'El costo es : ${costo_fijo}')
except:
    if cantidad_alumno == 0:
        print('Ingrese un numero mayor a 0')
    elif cantidad_alumno == '':
        print('ingrese un numero')
        
# <------------------------------------------------------------------------->
'''

3.) La política de la compañía telefónica “chimefón” es: “Chismea + x -”. 
Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma 
que los primeros cinco minutos cuestan $ 1.00 c/u, los siguientes tres, 80¢ c/u, 
los siguientes dos minutos, 70¢ c/u, y a partir del décimo minuto, 50¢ c/u. Además, 
se carga un impuesto de 3 % cuando es domingo, y si es día hábil, en turno matutino, 
15 %, y en turno vespertino, 10 %. Realice un algoritmo para determinar 
cuánto debe pagar por cada concepto una persona que realiza una llamada.'''

# <------------------------------------------------------------------------->

from datetime import datetime
minutos = float(input("Ingrese la duración de la llamada en minutos: "))
fecha_hora_str = input("Ingrese la fecha y hora de la llamada (YYYY-MM-DD HH:MM): ")

def calcular_costo_llamada(minutos):
    costo = 0


    tarifas = {
        'primeros_5': 1.00,
        'siguientes_3': 80,
        'siguientes_2': 70,
        'primeros_10': 50
    }
    if minutos > 10:
        costo = (minutos -10)* tarifas['primeros_10']
        minutos = 10
    elif minutos > 7:
        costo = (minutos -7)* tarifas['siguientes_2']
        minutos = 7
    elif minutos > 5:
        costo = (minutos -5)* tarifas['primeros_3']
        minutos = 5
    costo = minutos * tarifas['primeros_5']
    print(costo)
    
def impuesto(fecha_hora):
    dia_semana = fecha_hora.weekday()
    hora = fecha_hora.hour
    if dia_semana == 6:
      return 0.03
    elif hora < 12:
        return 0.15
    else:
        return 0.10
    
fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
costo = calcular_costo_llamada(minutos)
impuesto_porcentaje = impuesto(fecha_hora)
impuesto_total = (costo * impuesto_porcentaje)
costo_final = (costo * impuesto_total)

print(costo_final)

# <------------------------------------------------------------------------->

'''
4.) Realice un algoritmo para generar e imprimir los números pares que se 
encuentran entre 0 y 100.
'''
# <------------------------------------------------------------------------->

def es_par():
    
    for numero in range(101):
       
        if numero % 2 == 0:
            
            print(numero)
es_par()

# <------------------------------------------------------------------------->
'''
5.) Una persona se encuentra en el kilómetro 70 de la carretera 
Aguascalientes Zacatecas, otra se encuentra en el km 150 de la misma carretera,
la primera viaja en dirección a Zacatecas, mientras que la segunda se dirige 
a Aguasca lientes, a la misma velocidad. Realice un algoritmo para determinar en qué 
kilometro de esa carretera se encontrarán '''

distancia_a = 70
distancia_b = 150
diferencia_encuentro = (distancia_a - distancia_b)
punto_encuentro = (diferencia_encuentro / 2)
print (f'Las dos personas se encontraran en el kilometro {punto_encuentro}')

# <------------------------------------------------------------------------->
'''
6.) La cadena de tiendas de autoservicio “El mandilón” cuenta con sucursa les en C 
ciudades diferentes de la República, en cada ciudad cuenta con T tiendas y cada tienda
cuenta con N empleados, asimismo, cada una regis tra lo que vende de manera individual
cada empleado, cuánto fue lo que vendió cada tienda, cuánto se vendió en cada ciudad y
cuánto recaudó la cadena en un solo día. Realice un algoritmo para determinar lo 
anterior.'''


cantidad_ciudades = int(input("Ingrese la cantidad de ciudades: "))
cantidad_tiendas = int(input("Ingrese la cantidad de tiendas por ciudad: "))
cantidad_empleados = int(input("Ingrese la cantidad de empleados por tienda: "))

total_cadenas = 0

for ciudad in range(cantidad_ciudades):
    total_ciudad = 0
    print(f"Ciudad {ciudad + 1}:")
    
    for tienda in range(cantidad_tiendas):
        total_tienda = 0
        print(f"Tienda {tienda + 1}:")
        
        for empleado in range(cantidad_empleados):
            ventas_empleado = float(input(f"Ingrese el monto vendido por el empleado {empleado + 1}: "))
            total_tienda += ventas_empleado
        
        print(f"Total vendido en la tienda {tienda + 1}: ${total_tienda}")
        total_ciudad += total_tienda
    
    print(f"Total vendido en la ciudad {ciudad + 1}: ${total_ciudad}")
    total_cadena += total_ciudad

print(f"Total vendido en la cadena: ${total_cadena}")
