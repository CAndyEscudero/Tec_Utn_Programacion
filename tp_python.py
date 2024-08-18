'''1. ) La asociación de vinicultores tiene como política fijar un precio inicial 
al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
se requiere determinar cuánto recibirá un productor por la uva que entre ga en un embarque,
considerando lo siguiente: si es de tipo A, se le cargan 20¢ al precio inicial 
cuando es de tamaño 1; y 30¢ si es de tamaño 2. Si es de tipo B, se rebajan 30¢ 
cuando es de tamaño 1, y 50¢ cuando es de tamaño 2. Realice un algoritmo para 
determinar la ganancia obtenida y represéntelo mediante diagrama de flujo y su 
correspondiente script(programa) en python.'''

'''while(True):
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
'''

'''2.) El director de una escuela está organizando un viaje de estudios, y 
    requie re determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la
    compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 
    alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos, el costo es 
    de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta del autobús
    es de $4000.00, sin importar el número de alumnos. Entregar Diagrama de flujo y
    script en python.'''
'''
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
        print('ingrese un numero')'''

'''
3.) La política de la compañía telefónica “chimefón” es: “Chismea + x -”. 
Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma 
que los primeros cinco minutos cuestan $ 1.00 c/u, los siguientes tres, 80¢ c/u, 
los siguientes dos minutos, 70¢ c/u, y a partir del décimo minuto, 50¢ c/u. Además, 
se carga un impuesto de 3 % cuando es domingo, y si es día hábil, en turno matutino, 
15 %, y en turno vespertino, 10 %. Realice un algoritmo para determinar 
cuánto debe pagar por cada concepto una persona que realiza una llamada.'''
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
'''
4.) Realice un algoritmo para generar e imprimir los números pares que se 
encuentran entre 0 y 100.
'''
'''
def es_par():
    
    for numero in range(101):
       
        if numero % 2 == 0:
            
            print(numero)
es_par()
'''