import random

'''Ejercicio 1: Ejecuta el programa en tu sistema y observa qué números
obtienes.
La función random es solamente una de las muchas que trabajan con números
aleatorios. La función randint toma los parámetros inferior y superior, y
devuelve un entero entre inferior y superior (incluyendo ambos extremos).'''

for i in range(5):
    x = random.randint(5, 10)
    print(x)

#-----------------------------------------------------------------------#

'''Ejercicio 2: Desplaza la última línea del programa anterior hacia arriba,
de modo que la llamada a la función aparezca antes que las definiciones.
Ejecuta el programa y observa qué mensaje de error obtienes.'''

def muestra_estribillo():
    print('Soy un leñador, que alegría.')
    print('Duermo toda la noche y trabajo todo el día.')
    
repite_estribillo() 
def repite_estribillo():
    muestra_estribillo()
    muestra_estribillo()
    

'''Ejercicio 3: Desplaza la llamada de la función de nuevo hacia el final,
y coloca la definición de muestra_estribillo después de la definición de
repite_estribillo. ¿Qué ocurre cuando haces funcionar ese programa?'''

def muestra_estribillo():
    print('Soy un leñador, que alegría.')
    print('Duermo toda la noche y trabajo todo el día.')
      
def repite_estribillo():
 
    repite_estribillo() 
muestra_estribillo()
muestra_estribillo()

'''Ejercicio 4: ¿Cuál es la utilidad de la palabra clave “def” en Python?
a) Es una jerga que significa “este código es realmente estupendo”
b) Indica el comienzo de una función
c) Indica que la siguiente sección de código indentado debe ser almacenada para
usarla más tarde
d) b y c son correctas ambas
e) Ninguna de las anteriores
Respuesta: D    '''

'''Ejercicio 5: ¿Qué mostrará en pantalla el siguiente programa Python?
def fred():
print("Zap")
def jane():
print("ABC")
jane()
fred()
jane()
a) Zap ABC jane fred jane
b) Zap ABC Zap
c) ABC Zap jane
d) ABC Zap ABC
e) Zap Zap Zap

Respuesta : D '''



'''Ejercicio 6: Reescribe el programa de cálculo del salario, con tarifa-ymedia para las horas extras, y crea una función llamada calculo_salario
que reciba dos parámetros (horas y tarifa).
Introduzca Horas: 45
Introduzca Tarifa: 10
Salario: 475.0'''

horas = float(input("Introduzca Horas: "))
tarifa = float(input("Introduzca Tarifa: "))

def calculo_salario(horas, tarifa):
    
    horas_extra = 40
    tarifa_extra = tarifa * 1.5
    
    if horas <= horas_extra:
        salario = horas * tarifa
    else:
        horas_normales = horas_extra
        horas_extra = horas - horas_extra
        salario = (horas_normales * tarifa) + (horas_extra * tarifa_extra)
    
    return salario

salario = calculo_salario(horas, tarifa)

print(f"Salario: {salario}")

'''
Ejercicio 7: Reescribe el programa de calificaciones del capítulo anterior usando una función llamada calcula_calificacion, que reciba una
puntuación como parámetro y devuelva una calificación como cadena'''


def valores(valor):
        calificacion=valor
        while True:
            while True:
                b = input(valor)
                try:
                    valor = float(b) 
                    break   
                except :
                    print("ingrese un numero valido")
                    
            if(float(b)<0) or (float(b)>1.0):
                valor=calificacion
                print("Ingrese un valor del 0.0 al 1")
            else:
                return valor
def calcula_calificacion(nota):
    if(nota>0.9):
        print("Sobresaliente")
    elif(nota>0.8):
        print("Notable")
    elif(nota>0.7):
        print("Bien")
    elif(nota>0.6):
        print("Suficiente")
    elif(nota<=0.6):
        print("Insuficiente")
    else:
        print("error")

while True:
    nota=valores("notas: ")
    nota=calcula_calificacion(nota)